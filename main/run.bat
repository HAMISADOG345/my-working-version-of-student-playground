@echo off
cd /d "%~dp0"
echo ======================================================
echo   STARTING PLAYGROUND WEB SERVER ENVIRONMENT         
echo ======================================================
start "" "http://localhost:8000/student-playground.html"
python server_backend.py
pause