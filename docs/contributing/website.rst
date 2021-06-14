***************
Documentation
***************

Thank you for your offer to help. Here's some instructions for how to contribute. You might want to check in with an admin from the DCC++ EX team before working on documentation changes to identify current needs.

Submission Procedure
======================

We will assume that you have an appropriate text editor and Git installed on your machine. We recommend the free `Visual Studio Code IDE (VSC) <https://code.visualstudio.com/>`_ and `GitHub Desktop <https://desktop.github.com/>`_ or `Git Bash (the command line interface in Git) <https://git-scm.com/downloads>`_.

1. Clone the `dcc-ex.github.io <https://github.com/DCC-EX/dcc-ex.github.io/tree/sphinx>`_Support repository, to your local machine. Make sure you're on the sphinx branch. (`Cloning a repository in GitHub <https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository>`_)

2. Install Python 3.8 (which also installs pip) then use pip to install the required packages ```pip install sphinx sphinx_rtd_theme sphinxcontrib-spelling```

3. Using Git Bash, go to the "website" folder and make a branch using GitHub desktop or this command: ```git checkout -b your-branch-name```

4. Open VSC and edit the files in the ```dcc-ex.github.io/docs``` folder. Save, then Preview your changes by running ```make github``` from the root of the ```dcc-ex.github.io``` folder. *This must be done from cmd.exe in Windows, not PowerShell* Then go to the directory ```dcc-ex.github.io/docs/build/html``` and open ```index.html``` in Chrome or another browser. Note that since 11/23/2020, this is just a local preview - when you push your changes, GitHub will automatically rebuild your website.

5. Use ```git add``` and ```git commit -m "MY CHANGE DESCRIPTION"``` often to save changes. If you're using GitHub Desktop these are combined in the commit button.

6. Push it to GitHub: ```git push origin {your-name}-changes```

7. Go to GitHub and issue a pull request for your branch to be pulled into the sphinx branch. Once it's merged in by one of the admins, your changes will go live!

Standards
==========

* Main Headings have asterisks above and below them
* Subheadings are underlined with equals signs
* The next level is underlined with underscores
* And the next level is underlined with carets
* The last one we use is underlined with tildes

All heading underlines and overlines must be at least as long as the text of the heading

*Work in progress*