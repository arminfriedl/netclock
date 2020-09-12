// This file is packed by webpack into /static/dist/countdown.bundle.js
// Use with: `url_for('static', filename='dist/countdown.bundle.js')`
// See: webpack.common.js
import log from 'loglevel';
import $ from 'jquery';

import './countdown.scss';

let api_base = "/countdown/api/v1/";


const updateCountdown = () => $.getJSON({
    url: api_base+countdown_id,
    data: Date.now(),
    success: function(countdown) {
        if(countdown.left <= 0) {
            // clear interval, don't count below 0
            clearInterval(scheduledUpdater);
            $("#countdown").text("Time is up!");
            let end = new Date(Math.floor(countdown.start*1000 + countdown.total*1000));
            $("#subtext").text("This countdown ended on "+ end.toLocaleDateString()+" "+end.toLocaleTimeString());
            return;
        }

        // total seconds left
        let sec = Math.floor(countdown.left);
        // milliseconds left in seconds resolution
        let frac = countdown.left - sec;
        // milliseconds left in millisecond resolution
        let milli = Math.floor(frac * 1000);
        // seconds in hrs, minutes, seconds
        let h = Math.floor(sec/(60*60));
        let m = Math.floor(sec/60) - (h*60);
        let s = sec - (m*60) - (h*60*60);

        // let milliseconds pass, then set element to
        // amount of full seconds left
        let htext = padTime(h);
        let mtext = padTime(m);
        htext = htext !== "00" ? htext+":": "";
        mtext = mtext !== "00" ? mtext+":": "";
        setTimeout(() => $("#countdown").text(htext+mtext+padTime(s)), milli);
    }
});

let scheduledUpdater = setInterval(updateCountdown, 1000);
let padTime = t => `${"0".repeat(2-t.toString().length)+t}`;

