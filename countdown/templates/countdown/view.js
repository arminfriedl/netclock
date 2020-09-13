// This file is packed by webpack into /static/dist/countdown_view.bundle.js
// Use with: `url_for('static', filename='dist/countdown_view.bundle.js')`
// See: webpack.common.js
import log from 'loglevel';
import $ from 'jquery';

import {sleep} from '../../../js/netclock.js';

import './view.scss';

let api_base = "/countdown/api/v1/";

let padTime = (t) => {
    let t_s = t.toString();
    // Pads to at least two digits filling with 0
    let leftPad = t_s.length < 2 ?
        "0".repeat(2 - t.toString().length) :
        "";

    return `${leftPad+t_s}`;
};

let formatTime = (h, m, s) => {
    let htext = padTime(h);
    let mtext = padTime(m);
    let stext = padTime(s);

    htext = htext !== "00" ? htext + ":" : "";
    mtext = mtext !== "00" || htext !== "00" ? mtext + ":" : "";

    return htext + mtext + stext;
};

let splitTimestamp = (t) => {
    // Timestamp as full seconds
    let seconds = Math.floor(t);

    return {
        "hours": ~~(seconds / 3600),
        "minutes": ~~((seconds % 3600) / 60),
        "seconds": ~~(seconds % 60),
        "milliseconds": ~~((t % 1) * 1000)
    };
};

// amount of seconds since last sync
let unsyncedSeconds = 0;
let countdown = undefined;

let updateCountdown = () => {
    if(!countdown) return;

    // Not started
    if (countdown.start === "-1") {
        let split = splitTimestamp(countdown.total);
        $("#countdown").text(formatTime(split.hours, split.minutes, split.seconds));
        $("#subtext").text("Countdown has not started");
        return;
    }

    let unsyncedLeft = countdown.left - unsyncedSeconds;

    // Countdown already over
    if (unsyncedLeft <= 0) {
        if(countdownTimer) clearInterval(countdownTimer);
        if(syncTimer) clearInterval(syncTimer);

        $("#countdown").text("Time is up!");
        let end = new Date(Math.floor(countdown.start * 1000 + countdown.total * 1000));
        $("#subtext").text("This countdown ended on " + end.toLocaleDateString() + " " + end.toLocaleTimeString());
        return;
    }

    let time = splitTimestamp(unsyncedLeft);
    let text = formatTime(time.hours, time.minutes, time.seconds);

    sleep(time.milliseconds)
        .then(() => {
            $("#countdown").text(text);
            $("#subtext").text();
        });
};

let unsyncTimer = undefined;

let sync = () => {
    $.getJSON({
        url: api_base + countdown_id,
        success: async function(resp) {
            if(unsyncTimer) clearInterval(unsyncTimer);

            let time = splitTimestamp(resp.left);
            await sleep(time.milliseconds);

            countdown = resp;
            countdown.left = ~~countdown.left;
            unsyncedSeconds = 0;
            unsyncTimer = setInterval(() => unsyncedSeconds++, 1000);
        }
    });
};



// initialize the countdown
sync();

// update countdown from last sync and unsyncedSeconds in regular intervals
let countdownTimer = setInterval(updateCountdown, 100);
// sync in regular intervals
let syncTimer = setInterval(sync, 5000);
