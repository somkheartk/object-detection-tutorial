#!/bin/bash

# Quick Start Script for Car Object Detection Tutorial
# สคริปต์เริ่มต้นด่วนสำหรับบทเรียนการตรวจจับรถยนต์

echo "=================================="
echo "Car Object Detection Tutorial"
echo "บทเรียนการตรวจจับรถยนต์"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
echo "ตรวจสอบเวอร์ชัน Python..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed"
    echo "ข้อผิดพลาด: Python 3 ยังไม่ได้ติดตั้ง"
    exit 1
fi

echo ""
echo "Step 1: Creating virtual environment..."
echo "ขั้นตอนที่ 1: สร้าง virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    echo "ข้อผิดพลาด: ไม่สามารถสร้าง virtual environment ได้"
    exit 1
fi

echo ""
echo "Step 2: Activating virtual environment..."
echo "ขั้นตอนที่ 2: เปิดใช้งาน virtual environment..."

# Detect OS and activate accordingly
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo ""
echo "Step 3: Installing dependencies..."
echo "ขั้นตอนที่ 3: ติดตั้งไลบรารี..."
echo "This may take a few minutes..."
echo "อาจใช้เวลาสักครู่..."

pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    echo "ข้อผิดพลาด: ไม่สามารถติดตั้งไลบรารีได้"
    exit 1
fi

echo ""
echo "=================================="
echo "✓ Setup completed successfully!"
echo "✓ ติดตั้งเสร็จสมบูรณ์!"
echo "=================================="
echo ""
echo "You can now:"
echo "คุณสามารถ:"
echo ""
echo "1. Run the demo:"
echo "   python demo.py"
echo ""
echo "2. Detect cars in an image:"
echo "   python src/car_detector.py --input path/to/image.jpg --output result.jpg"
echo ""
echo "3. Detect cars in a video:"
echo "   python src/car_detector.py --input path/to/video.mp4 --output result.mp4 --video"
echo ""
echo "4. Use webcam:"
echo "   python src/car_detector.py --input 0 --video"
echo ""
echo "For more information, see README.md"
echo "สำหรับข้อมูลเพิ่มเติม โปรดดู README.md"
echo ""
