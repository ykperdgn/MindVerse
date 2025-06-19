@echo off
echo =========================================
echo   MindVerse Daily Automation Started
echo =========================================
echo Time: %date% %time%
echo.

cd /d "C:\Users\Jacob\MindVerse\mindverse_blog"

echo Running daily automation...
python advanced_daily_automation.py run-daily

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Daily automation completed successfully!
    echo Time: %date% %time% >> automation.log
    echo ✅ Daily automation completed successfully! >> automation.log
    echo. >> automation.log
) else (
    echo.
    echo ❌ Daily automation failed with error: %ERRORLEVEL%
    echo Time: %date% %time% >> automation.log
    echo ❌ Daily automation failed with error: %ERRORLEVEL% >> automation.log
    echo. >> automation.log
)

echo =========================================
echo   MindVerse Daily Automation Finished
echo =========================================
