@echo off
cd /d "%~dp0_site"
python -m http.server 4000
