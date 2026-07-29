@echo off
setlocal

set "SCRIPT=%~dp0tools\Initialize-N-Human-AI-Mathematics.ps1"

if not exist "%SCRIPT%" (
    echo.
    echo ERROR: Bootstrap script not found:
    echo   %SCRIPT%
    echo.
    echo Check out the private research source bootstrap branch before running this launcher.
    echo.
    pause
    exit /b 1
)

where powershell.exe >nul 2>nul
if errorlevel 1 (
    echo.
    echo ERROR: powershell.exe was not found.
    echo.
    pause
    exit /b 1
)

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" %*
set "RC=%ERRORLEVEL%"

echo.
if "%RC%"=="0" (
    echo Bootstrap command completed successfully.
) else (
    echo Bootstrap command failed with exit code %RC%.
)
echo.
pause
exit /b %RC%
