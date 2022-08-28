$(function()
{
    $("#html").val(`
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
        <style>
        </style>
    </head>
    <body>
    </body>
</html>`)
});
function run() {
    $("#preview").html($("#html").val())
}