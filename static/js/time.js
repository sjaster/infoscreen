'use strict'

function getTime() {
    let date = new Date()
    return date.toLocaleTimeString()
}

function getDate() {
    let date = new Date()
    let options = { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit' };
    let ret = date.toLocaleString('de-DE', options)
    return ret
}

function setHtml() {
    let time = getTime()
    let date = getDate()

    $('#time').html(time)
    $('#date').html(date)
}

$(document).ready(function(){
    setHtml()
    setInterval(setHtml, '1000')
})