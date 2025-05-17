@echo off

echo Verifying Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not found in PATH.
    echo Please install Python 3.9+ and add it to your PATH.
    pause
    exit /b 1
)

echo Creating virtual environment (venv)...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)

echo Activating virtual environment...
call .\venv\Scripts\activate

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo Installation complete.

echo To run the application, execute launcher.bat
pause
