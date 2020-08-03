function getLink() {
    httpGetAsync("https://api.github.com/repos/DCC-EX/BaseStation-Installer/releases", (data) => {
        let parsed = JSON.parse(data);
        let needed = "not supported";
        switch (platform.os.family) {
            case "Windows":
                if (platform.os.architecture == 32) {
                    needed = "win-x86";
                } else if (platform.os.architecture == 64) {
                    needed = "win-x64";
                }
                break;
            case "Red Hat":
            case "CentOS":
            case "Ubuntu":
            case "Debian":
            case "Fedora":
            case "Linux":
                if (platform.os.architecture == 64) {
                    needed = "linux-x64";
                } else if (platform.os.architecture == `arm64`) {
                    needed = "linux-arm64";
                } else if (platform.os.architecture == `arm`) {
                    needed = "linux-arm";
                }
                break;
            case "OS X":
                if (platform.os.architecture == 64) {
                    needed = "osx-x64";
                }
        }
        if (needed === "not supported") {
            alert("OS Version not supported at this time");
            return;
        }
        for (let k in parsed[0].assets) {
            if (parsed[0].assets[k].name.includes(needed)) {
                window.open(parsed[0].assets[k].browser_download_url, "_blank");
            }
        }
    });
}

function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) callback(xmlHttp.responseText);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}
