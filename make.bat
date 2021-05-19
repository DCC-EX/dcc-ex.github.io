@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=docs\.
set BUILDDIR=docs\_build
REM set SPHINXOPTS=

if "%1" == "" goto help

if "%1" == "github" (
    %SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
	echo "dcc-ex.com" /y > docs\_build\html\CNAME
	echo "" /y > docs\_build\html\.nojekyll
    goto end
)

if "%1" == "clean" (
    echo.CLEAN BUILD with -E -a
REM    %SPHINXOPTS% = "-E -a"
    %SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% -E -a
	echo "dcc-ex.com" /y > docs\_build\html\CNAME
	echo "" /y > docs\_build\html\.nojekyll
    goto end
)

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
