/*
  This script is tied to the command station download page and automatically modifies the download
  link in order to supply the user with the correct download of the new installer for their Operating System and append the apprppriate text to the end of this URL.
  
   https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-

*/
function getNewLink() {
	needed = "not supported";
	switch (platform.os.family) {
		case "Windows":
			if (platform.os.architecture == 32) {
				needed = "Win32.exe";
			} else if (platform.os.architecture == 64) {
				needed = "Win64.exe";
			}
			break;
		case "Red Hat":
		case "CentOS":
		case "Ubuntu":
		case "Debian":
		case "Fedora":
		case "Linux":
			if (platform.os.architecture == 64) {
				needed = "Linux64";
			}
			break;
		case "OS X":
			if (platform.os.architecture == 64) {
				needed = "macOS";
			}
	}
	if (needed === "not supported") {
		alert("OS Version not supported at this time");
		return;
	} else {
		window.open("https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-"+needed, "_blank");
	}
}


/*
  This script is tied to the command station download page and automatically modifies the download
  link in order to supply the user with the correct download of the original installer for their Operating System. To do this,
  it goes to the JSON version of the GitHub API here: 
  
   https://api.github.com/repos/DCC-EX/exInstaller/releases

   It then finds the OS of the machine running the users browser and searches for that string (ex: win-x64) in
   the "name" field of the first "Assets" section (parsed[0].assets), which is the latest release. It then
   initiates a download to the link in that "name" field.
*/
function getLink(needed = "nope") {
    httpGetAsync("https://api.github.com/repos/DCC-EX/exInstaller/releases", (data) => {
        let parsed = JSON.parse(data);
        if (needed == "nope") {
            needed = "not supported";
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
