import '../css/netclock.scss';
import log from 'loglevel';
import $ from 'jquery';

if (process.env.LOG_LEVEL) {
    log.setDefaultLevel(process.env.LOG_LEVEL);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export {sleep};
