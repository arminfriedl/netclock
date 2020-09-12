import '../css/netclock.scss';
import log from 'loglevel';

if (process.env.LOG_LEVEL) {
    log.setDefaultLevel(process.env.LOG_LEVEL);
}
