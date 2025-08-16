@echo off
setlocal
echo This script downloads and sets up SteamCMD.
set STEAMCMD_URL=https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip
set STEAMCMD_DIR=%~dp0steamcmd

echo Downloading SteamCMD...
powershell -Command "Invoke-WebRequest -Uri %STEAMCMD_URL% -OutFile steamcmd.zip" || goto :error
echo Extracting...
powershell -Command "Expand-Archive -Path steamcmd.zip -DestinationPath %STEAMCMD_DIR% -Force" || goto :error
del steamcmd.zip

cd /d %STEAMCMD_DIR%
echo Running SteamCMD first-time setup...
steamcmd +quit
cd /d %~dp0
echo SteamCMD installed in %STEAMCMD_DIR%
pause
exit /b

:error
echo Failed to download or extract SteamCMD.
pause
exit /b 1
