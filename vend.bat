@ECHO OFF

REM This batch file removes the local virtual environment that is activated with start.bat

where /q virtualenv

ECHO De-activating virtual environment...
call .\venv\Scripts\deactivate.bat^
 & rmdir /S /Q venv