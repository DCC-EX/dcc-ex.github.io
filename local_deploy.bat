@ECHO OFF

REM This batch file will create a local virtual environment and activate it.
REM The versions in python_packages.bat must be kept the same as the GitHub workflow.
REM It is recommended to destroy the virtual env once testing is complete, and start fresh each time.

where /q virtualenv

IF ERRORLEVEL 1 (
  ECHO Python virtualenv command missing or not in path
  EXIT /B
)

virtualenv venv

ECHO Activating virtual environment...
call .\venv\Scripts\activate.bat^
 & python_packages.bat^
 & make clean^
 & make github^
 & pip3 list^
 & .\venv\Scripts\deactivate.bat^
 & rmdir /S /Q venv