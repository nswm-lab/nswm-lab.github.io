@echo off
cd /d C:\Users\Eg4m1\Desktop\nswm-lab.github.io

REM Kill any existing Python servers on port 4000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :4000 ^| findstr LISTENING') do taskkill /F /PID %%a 2>nul

REM Clean and rebuild
rmdir /s /q _site 2>nul
bundle exec jekyll build

REM Start Python HTTP server
cd _site
start /b python -m http.server 4000
cd ..
echo Server started at http://localhost:4000
