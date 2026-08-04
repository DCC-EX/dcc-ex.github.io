// This shows divs appropriate to the current operating system
document.addEventListener('DOMContentLoaded', function () {
    var userAgent = navigator.userAgent;

   if (userAgent.indexOf('WOW64') !== -1 || userAgent.indexOf('Win64') !== -1) {
            document.querySelectorAll('.win64-installer').forEach(div => div.hidden = false);
    } else if (userAgent.match(/Macintosh|Mac OS X/)) {
        document.querySelectorAll('.mac-installer').forEach(div => div.hidden = false);
    } else if (userAgent.match(/Linux/)) {
        document.querySelectorAll('.linux-installer').forEach(div => div.hidden = false);
    } else {
        document.querySelectorAll('.unsupported-installer').forEach(div => div.hidden = false);
    }
}
);
