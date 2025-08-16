@echo off
setlocal enabledelayedexpansion

REM Automatically compile any flexScript* Python file into flexScripy.exe

set SCRIPT=
for %%i in (flexScript*.py) do (
    set SCRIPT=%%i
)

if not defined SCRIPT (
    echo No flexScript*.py file found.
    goto end
)

where pyinstaller >nul 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Install it with:
    echo     pip install pyinstaller
    goto end
)

pyinstaller --noconfirm --onefile --name flexScripy "!SCRIPT!"

if errorlevel 1 (
    echo.
    echo Build failed.
    goto end
)

echo.
echo Build complete. The executable can be found in the dist folder.

:end
echo.
pause
