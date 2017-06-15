setInterval('go()',1000);
function go(){
    var content = $('#webapp').text();
    var firstchar=content.charAt(0);
    var sub = content.substring(1,content.length);
    $('#webapp').text(sub+firstchar);
}
