@echo off
REM Quick Start Script for Car Object Detection Tutorial (Windows)
REM สคริปต์เริ่มต้นด่วนสำหรับบทเรียนการตรวจจับรถยนต์ (Windows)

echo ==================================
echo Car Object Detection Tutorial
echo บทเรียนการตรวจจับรถยนต์
echo ==================================
echo.

echo Checking Python version...
echo ตรวจสอบเวอร์ชัน Python...
python --version
if errorlevel 1 (
    echo Error: Python is not installed
    echo ข้อผิดพลาด: Python ยังไม่ได้ติดตั้ง
    pause
    exit /b 1
)

echo.
echo Step 1: Creating virtual environment...
echo ขั้นตอนที่ 1: สร้าง virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    echo ข้อผิดพลาด: ไม่สามารถสร้าง virtual environment ได้
    pause
    exit /b 1
)

echo.
echo Step 2: Activating virtual environment...
echo ขั้นตอนที่ 2: เปิดใช้งาน virtual environment...
call venv\Scripts\activate.bat

echo.
echo Step 3: Installing dependencies...
echo ขั้นตอนที่ 3: ติดตั้งไลบรารี...
echo This may take a few minutes...
echo อาจใช้เวลาสักครู่...

python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    echo ข้อผิดพลาด: ไม่สามารถติดตั้งไลบรารีได้
    pause
    exit /b 1
)

echo.
echo ==================================
echo ✓ Setup completed successfully!
echo ✓ ติดตั้งเสร็จสมบูรณ์!
echo ==================================
echo.
echo You can now:
echo คุณสามารถ:
echo.
echo 1. Run the demo:
echo    python demo.py
echo.
echo 2. Detect cars in an image:
echo    python src\car_detector.py --input path\to\image.jpg --output result.jpg
echo.
echo 3. Detect cars in a video:
echo    python src\car_detector.py --input path\to\video.mp4 --output result.mp4 --video
echo.
echo 4. Use webcam:
echo    python src\car_detector.py --input 0 --video
echo.
echo For more information, see README.md
echo สำหรับข้อมูลเพิ่มเติม โปรดดู README.md
echo.
pause
