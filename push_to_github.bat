@echo off
git init
git add .
git commit -m "Initial commit: Patient Monitoring Platform"
git branch -M main
git remote add origin https://github.com/anusiyamct2025/patient-monitoring-platform
git push -u origin main
echo Done.
