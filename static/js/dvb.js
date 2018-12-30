'use strict'

function getJson(linenumber, callback) {
    $.ajax({
        dataType: 'json',
        url: '/data/dvb/' + linenumber,
        success: function(res) {
            callback(res)
        }
    })
}

function renderHtml(linenumber) {
    getJson(linenumber, function callback(line){ 

    let elem
    let ret = ''

    for (elem in line) {
        let rides = line[elem]
        let linenr = '<i class="fa fa-info"> ' + 'Linie ' + '<strong>' + rides['linenumber'] + '</strong></i><br>'
        let stop_line = '<i class="fa fa-home"> ' + rides['stop'] + ' - ' + rides['time'] + '</i><br><br>'
        ret += linenr + stop_line
    }
    if (elem == null) {
        ret = '<strong>No Data availabe</strong>'
    }

    $('#line' + linenumber).html(ret)
    setTimeout(function () {renderHtml(linenumber)}, 30000)
    })
}

$(document).ready(function(){
    let lines = ['85', '62', '63', '61', 'tharan']
    let x

    for (x in lines){
        renderHtml(lines[x])
    } 
})