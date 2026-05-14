@echo off
echo =======================================================
echo         MINECRAFT SUBFOLDER BACKGROUND INITIALIZATION  
echo =======================================================

if "%MC_USERNAME%"=="" set MC_USERNAME=StudentPlayer
if "%MC_VERSION%"=="" set MC_VERSION=1.20.1

where java >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Java was NOT found. Installing Microsoft OpenJDK 17...
    winget install --id Microsoft.OpenJDK.17 --silent --accept-source-agreements --accept-package-agreements
)

echo [SUCCESS] Handing execution to Python game loop...
python game_runner.py "%MC_USERNAME%" "%MC_VERSION%"
if %errorlevel% neq 0 pause