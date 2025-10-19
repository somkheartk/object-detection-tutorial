#!/usr/bin/env python3
"""
Test script to validate the project structure
สคริปต์ทดสอบเพื่อตรวจสอบโครงสร้างโปรเจค
"""

import os
import sys
from pathlib import Path

def check_file_exists(path, description):
    """Check if a file exists"""
    if os.path.exists(path):
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ {description}: {path} NOT FOUND")
        return False

def check_directory_exists(path, description):
    """Check if a directory exists"""
    if os.path.isdir(path):
        print(f"✓ {description}: {path}/")
        return True
    else:
        print(f"✗ {description}: {path}/ NOT FOUND")
        return False

def main():
    print("=" * 70)
    print("Car Object Detection Tutorial - Structure Validation")
    print("บทเรียนการตรวจจับรถยนต์ - การตรวจสอบโครงสร้าง")
    print("=" * 70)
    print()
    
    all_checks_passed = True
    
    # Check main files
    print("Main Files / ไฟล์หลัก:")
    all_checks_passed &= check_file_exists("README.md", "README")
    all_checks_passed &= check_file_exists("requirements.txt", "Requirements")
    all_checks_passed &= check_file_exists("demo.py", "Demo script")
    all_checks_passed &= check_file_exists(".gitignore", "Git ignore")
    print()
    
    # Check directories
    print("Directories / โฟลเดอร์:")
    all_checks_passed &= check_directory_exists("src", "Source code")
    all_checks_passed &= check_directory_exists("images", "Images")
    all_checks_passed &= check_directory_exists("docs", "Documentation")
    all_checks_passed &= check_directory_exists("models", "Models (will be auto-created)")
    print()
    
    # Check source files
    print("Source Files / ไฟล์ซอร์สโค้ด:")
    all_checks_passed &= check_file_exists("src/car_detector.py", "Car detector")
    print()
    
    # Check documentation
    print("Documentation / เอกสาร:")
    all_checks_passed &= check_file_exists("docs/getting_started.md", "Getting started")
    all_checks_passed &= check_file_exists("docs/advanced_usage.md", "Advanced usage")
    all_checks_passed &= check_file_exists("images/README.md", "Images README")
    print()
    
    # Check Python syntax
    print("Python Syntax Check / ตรวจสอบไวยากรณ์ Python:")
    import ast
    
    py_files = ["src/car_detector.py", "demo.py"]
    for file in py_files:
        try:
            with open(file, 'r') as f:
                ast.parse(f.read())
            print(f"✓ {file} - Syntax OK")
        except SyntaxError as e:
            print(f"✗ {file} - Syntax Error: {e}")
            all_checks_passed = False
    print()
    
    # Check requirements.txt content
    print("Dependencies Check / ตรวจสอบการขึ้นต่อกัน:")
    required_packages = ['opencv-python', 'numpy', 'torch', 'ultralytics']
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    
    for package in required_packages:
        if package in requirements:
            print(f"✓ {package} is in requirements.txt")
        else:
            print(f"✗ {package} is NOT in requirements.txt")
            all_checks_passed = False
    print()
    
    # Final result
    print("=" * 70)
    if all_checks_passed:
        print("✓ All checks passed! / ผ่านการตรวจสอบทั้งหมด!")
        print()
        print("Next steps / ขั้นตอนต่อไป:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run demo: python demo.py")
        print("3. Test detection: python src/car_detector.py --input image.jpg")
    else:
        print("✗ Some checks failed / การตรวจสอบบางอย่างล้มเหลว")
        return 1
    print("=" * 70)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
