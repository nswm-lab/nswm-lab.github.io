@echo off
echo Killing port 4000...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :4000 ^| findstr LISTENING') do (
    echo Killing PID %%a
    taskkill /PID %%a /F 2>nul
)

echo Building site...
cmd /c "set ACC_PRODUCT_CONFIG_V3= && bundle exec jekyll build"
if %errorlevel% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)

echo Starting server at http://localhost:4000
cd _site
python -m http.server 4000
