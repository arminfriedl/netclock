import log from 'loglevel';
import $ from 'jquery';

import './create.scss';

let subclocks = $("#subclocks");

$("#subclock-selection-add").click((ev) => {
    let tz = $("#subclock-selection-timezone").val();
    subclocks.append(`<input type="text" value="${tz}" readonly>`);
});
