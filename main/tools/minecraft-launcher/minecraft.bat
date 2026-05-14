@echo off
setlocal enabledelayedexpansion

echo =======================================================
echo         MINECRAFT BACKGROUND INITIALIZATION            
echo =======================================================

if "%MC_USERNAME%"=="" set MC_USERNAME=StudentPlayer
if "%MC_VERSION%"=="" set MC_VERSION=1.20.1

echo [INFO] Selected Username: %MC_USERNAME%
echo [INFO] Selected Version:  %MC_VERSION%
echo -------------------------------------------------------

echo Checking system environments for Java...
where java >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Java was NOT found on this system.
    echo Preparing automatic background installation via WinGet...
    goto INSTALL_JAVA
) else (
    echo [SUCCESS] Java environment found! Proceeding to launch...
    goto START_LAUNCHER
)

:INSTALL_JAVA
echo.
echo =======================================================
echo Installing Microsoft OpenJDK 17 silently...
echo Please click "Yes" if a Windows admin prompt appears.
echo =======================================================
echo.

winget install --id Microsoft.OpenJDK.17 --silent --accept-source-agreements --accept-package-agreements

where java >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Silent installation failed or requires a system reboot.
    echo Please install Java 17 manually or restart your computer.
    pause
    exit /b
)
echo [SUCCESS] Java installed successfully!
echo.

:START_LAUNCHER
echo -------------------------------------------------------
echo Handing controls over to the core Python game engine...
echo -------------------------------------------------------
python launcher.py "%MC_USERNAME%" "%MC_VERSION%"

if %errorlevel% neq 0 (
    echo [LAUNCH ERROR] The game runner crashed or failed.
    pause
)