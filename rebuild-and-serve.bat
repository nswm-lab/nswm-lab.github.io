@echo off
chcp 65001 >nul
echo [1/3] Stopping any running servers...
taskkill /F /IM python.exe >nul 2>&1
echo [2/3] Rebuilding Jekyll site...
cd /d "C:\Users\Eg4m1\Desktop\nswm-lab.github.io"
bundle exec jekyll build
echo [3/3] Starting server for _site directory on port 4000...
cd /d "C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_site"
start /B python -m http.server 4000
echo Done! Visit http://localhost:4000
pause
