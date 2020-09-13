// This file is packed by webpack into /static/dist/countdown_created.bundle.js
// Use with: `url_for('static', filename='dist/countdown_created.bundle.js')`
// See: webpack.common.js
import log from 'loglevel';
import $ from 'jquery';

import {sleep} from '../../../js/netclock.js';

import './created.scss';

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

    htext = htext + ":";
    mtext = mtext + ":";

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

let fillCountdown = (el) => {
    let x = el.attr("countdown-id");

    $.getJSON({
        url: api_base + el.attr('countdown-id'),
        success: function(resp) {
            let header = el.children(".created-countdown-header");

            let split = splitTimestamp(resp.total);
            header.children(".created-countdown-time")
                .text(formatTime(split.hours, split.minutes, split.seconds));

            let countdownInfo = header.children(".created-countdown-info");
            if(resp.start === "-1") {
                countdownInfo.text("Not started");
            } else if(resp.left <= 0) {
                countdownInfo.text("Ended");
            } else {
                countdownInfo.text("Running");
            }
        }
    });
};

let startCountdown = (el) => {
    $.ajax({
        url: api_base + "start/" + el.val(),
        method: 'PATCH'
    }).done(() => {
        $(".created-countdown").each((idx, el) => fillCountdown($(el)));
    });

};

let stopCountdown = (el) => {
    $.ajax({
        url: api_base + "stop/" + el.val(),
        method: 'PATCH'
    }).done(() => {
        $(".created-countdown").each((idx, el) => fillCountdown($(el)));
    });
};

let resetCountdown = (el) => {
    $.ajax({
        url: api_base + "reset/" + el.val(),
        method: 'PATCH'
    }).done(() => {
        $(".created-countdown").each((idx, el) => fillCountdown($(el)));
    });
};

$(".created-countdown").each((idx, el) => fillCountdown($(el)));
$(".created-countdown-start").each((idx, el) => $(el).click(() => startCountdown($(el))));
$(".created-countdown-stop").each((idx, el) => $(el).click(() => stopCountdown($(el))));
$(".created-countdown-reset").each((idx, el) => $(el).click(() => resetCountdown($(el))));
