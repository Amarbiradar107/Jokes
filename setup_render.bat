@echo off
REM Render Deployment Helper Script for Windows
REM This script sets up your project for Render deployment

echo.
echo ========================================
echo   Render Deployment Helper
echo ========================================
echo.

REM Check if venv exists
if not exist "venv\" (
    echo [1/5] Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo [1/5] Virtual environment already exists
)

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
pip install -r requirements.txt > nul 2>&1
pip install python-decouple gunicorn > nul 2>&1
echo ✓ Dependencies installed

echo.
echo [4/5] Running migrations...
python JokesProject\manage.py migrate > nul 2>&1
echo ✓ Migrations complete

echo.
echo [5/5] Collecting static files...
python JokesProject\manage.py collectstatic --noinput > nul 2>&1
echo ✓ Static files collected

echo.
echo ========================================
echo   ✓ Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create .env file (copy from .env.example)
echo 2. Generate a new SECRET_KEY
echo 3. Push to GitHub
echo 4. Deploy to Render
echo.
echo To generate SECRET_KEY, run:
echo   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
echo.
echo To test locally, run:
echo   python JokesProject\manage.py runserver
echo.
pause

