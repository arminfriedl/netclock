import log from 'loglevel';
import $ from 'jquery';


const updateCountdown = () => $.getJSON({
    url: "api/v1/countdown/070f478f-e168-488c-918e-adb37c9c0cbd",
    data: Date.now(),
    success: function(countdown) {
        if(countdown.left <= 0) {
            clearInterval(scheduledUpdater);
            $('#clock').text(0);
            return;
        }

        let floor = Math.floor(countdown.left);

        let frac = countdown.left - floor;
        let milli = Math.floor(frac * 1000); // get in millisecond resolution

        setTimeout(() => $('#clock').text(floor), milli);
    }
});

let scheduledUpdater = setInterval(updateCountdown, 1000);
