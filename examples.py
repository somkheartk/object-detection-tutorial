#!/usr/bin/env python3
"""
Complete Examples for Car Object Detection
ตัวอย่างที่สมบูรณ์สำหรับการตรวจจับรถยนต์

This file contains various examples demonstrating different use cases.
ไฟล์นี้มีตัวอย่างต่างๆ ที่แสดงกรณีการใช้งานที่แตกต่างกัน
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))


def example_1_basic_image_detection():
    """
    Example 1: Basic image detection
    ตัวอย่างที่ 1: การตรวจจับรูปภาพพื้นฐาน
    """
    print("\n" + "="*70)
    print("Example 1: Basic Image Detection")
    print("ตัวอย่างที่ 1: การตรวจจับรูปภาพพื้นฐาน")
    print("="*70 + "\n")
    
    try:
        from car_detector import CarDetector
        
        # Create detector with default settings
        detector = CarDetector()
        
        # Note: Replace 'test.jpg' with your actual image path
        # หมายเหตุ: แทนที่ 'test.jpg' ด้วยพาธรูปภาพจริงของคุณ
        print("To run this example, use:")
        print("  detector.detect_cars_in_image('images/your_image.jpg', output_path='output.jpg')")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please install dependencies first: pip install -r requirements.txt")


def example_2_custom_confidence():
    """
    Example 2: Detection with custom confidence threshold
    ตัวอย่างที่ 2: การตรวจจับด้วยเกณฑ์ความมั่นใจแบบกำหนดเอง
    """
    print("\n" + "="*70)
    print("Example 2: Custom Confidence Threshold")
    print("ตัวอย่างที่ 2: เกณฑ์ความมั่นใจแบบกำหนดเอง")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector

# High confidence (fewer but more accurate detections)
# ความมั่นใจสูง (ตรวจจับน้อยลงแต่แม่นยำกว่า)
detector_high = CarDetector(conf_threshold=0.7)

# Low confidence (more detections but less accurate)
# ความมั่นใจต่ำ (ตรวจจับมากขึ้นแต่แม่นยำน้อยลง)
detector_low = CarDetector(conf_threshold=0.3)

# Detect with high confidence
image, detections = detector_high.detect_cars_in_image('image.jpg')
print(f"High confidence: {len(detections)} vehicles detected")

# Detect with low confidence
image, detections = detector_low.detect_cars_in_image('image.jpg')
print(f"Low confidence: {len(detections)} vehicles detected")
"""
    print(code)


def example_3_different_models():
    """
    Example 3: Using different model sizes
    ตัวอย่างที่ 3: การใช้โมเดลขนาดต่างๆ
    """
    print("\n" + "="*70)
    print("Example 3: Different Model Sizes")
    print("ตัวอย่างที่ 3: โมเดลขนาดต่างๆ")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector
import time

# Nano model - Fastest / โมเดล Nano - เร็วที่สุด
detector_nano = CarDetector(model_name='yolov8n.pt')

# Large model - Most accurate / โมเดล Large - แม่นยำที่สุด
detector_large = CarDetector(model_name='yolov8l.pt')

# Compare performance
start = time.time()
_, detections_nano = detector_nano.detect_cars_in_image('image.jpg', show=False)
time_nano = time.time() - start

start = time.time()
_, detections_large = detector_large.detect_cars_in_image('image.jpg', show=False)
time_large = time.time() - start

print(f"Nano model: {len(detections_nano)} detections in {time_nano:.2f}s")
print(f"Large model: {len(detections_large)} detections in {time_large:.2f}s")
"""
    print(code)


def example_4_video_processing():
    """
    Example 4: Process a video file
    ตัวอย่างที่ 4: ประมวลผลไฟล์วิดีโอ
    """
    print("\n" + "="*70)
    print("Example 4: Video Processing")
    print("ตัวอย่างที่ 4: การประมวลผลวิดีโอ")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector

# Create detector
detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.6)

# Process video
detector.detect_cars_in_video(
    'traffic.mp4',           # Input video / วิดีโออินพุต
    output_path='output.mp4', # Output video / วิดีโอเอาต์พุต
    show=True                # Display while processing / แสดงขณะประมวลผล
)
"""
    print(code)


def example_5_webcam_detection():
    """
    Example 5: Real-time webcam detection
    ตัวอย่างที่ 5: การตรวจจับแบบเรียลไทม์จากเว็บแคม
    """
    print("\n" + "="*70)
    print("Example 5: Webcam Detection")
    print("ตัวอย่างที่ 5: การตรวจจับจากเว็บแคม")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector

# Create detector with fast model for real-time
# สร้างตัวตรวจจับด้วยโมเดลเร็วสำหรับเรียลไทม์
detector = CarDetector(model_name='yolov8n.pt')

# Use webcam (camera 0)
# ใช้เว็บแคม (กล้อง 0)
detector.detect_cars_in_video(0, show=True)

# Press 'q' to quit / กด 'q' เพื่อออก
"""
    print(code)


def example_6_filter_by_vehicle_type():
    """
    Example 6: Filter detections by vehicle type
    ตัวอย่างที่ 6: กรองการตรวจจับตามประเภทยานพาหนะ
    """
    print("\n" + "="*70)
    print("Example 6: Filter by Vehicle Type")
    print("ตัวอย่างที่ 6: กรองตามประเภทยานพาหนะ")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector

detector = CarDetector()
image, detections = detector.detect_cars_in_image('image.jpg', show=False)

# Filter only cars / กรองเฉพาะรถยนต์
cars = [d for d in detections if d['class_name'] == 'car']
print(f"Found {len(cars)} cars")

# Filter only trucks / กรองเฉพาะรถบรรทุก
trucks = [d for d in detections if d['class_name'] == 'truck']
print(f"Found {len(trucks)} trucks")

# Filter by confidence / กรองด้วยความมั่นใจ
high_conf = [d for d in detections if d['confidence'] > 0.8]
print(f"Found {len(high_conf)} high-confidence detections")
"""
    print(code)


def example_7_batch_processing():
    """
    Example 7: Process multiple images
    ตัวอย่างที่ 7: ประมวลผลรูปภาพหลายไฟล์
    """
    print("\n" + "="*70)
    print("Example 7: Batch Processing")
    print("ตัวอย่างที่ 7: การประมวลผลแบบแบตช์")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector
from pathlib import Path

# Create detector once
detector = CarDetector(model_name='yolov8n.pt')

# Get all images in folder / รับรูปภาพทั้งหมดในโฟลเดอร์
image_folder = Path('images')
output_folder = Path('output')
output_folder.mkdir(exist_ok=True)

# Process each image / ประมวลผลแต่ละรูปภาพ
for img_path in image_folder.glob('*.jpg'):
    print(f"Processing {img_path.name}...")
    
    output_path = output_folder / f"detected_{img_path.name}"
    detector.detect_cars_in_image(
        str(img_path),
        output_path=str(output_path),
        show=False
    )

print("Batch processing completed!")
"""
    print(code)


def example_8_save_detection_data():
    """
    Example 8: Save detection results to JSON
    ตัวอย่างที่ 8: บันทึกผลการตรวจจับเป็น JSON
    """
    print("\n" + "="*70)
    print("Example 8: Save Detection Data")
    print("ตัวอย่างที่ 8: บันทึกข้อมูลการตรวจจับ")
    print("="*70 + "\n")
    
    code = """
from car_detector import CarDetector
import json

detector = CarDetector()
image, detections = detector.detect_cars_in_image('image.jpg', show=False)

# Save detections to JSON / บันทึกการตรวจจับเป็น JSON
with open('detections.json', 'w') as f:
    json.dump(detections, f, indent=2)

# Load detections from JSON / โหลดการตรวจจับจาก JSON
with open('detections.json', 'r') as f:
    loaded_detections = json.load(f)

print(f"Saved and loaded {len(loaded_detections)} detections")
"""
    print(code)


def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("Car Object Detection - Complete Examples")
    print("การตรวจจับรถยนต์ - ตัวอย่างที่สมบูรณ์")
    print("="*70)
    
    # Show all examples
    example_1_basic_image_detection()
    example_2_custom_confidence()
    example_3_different_models()
    example_4_video_processing()
    example_5_webcam_detection()
    example_6_filter_by_vehicle_type()
    example_7_batch_processing()
    example_8_save_detection_data()
    
    print("\n" + "="*70)
    print("To run any example, copy the code and:")
    print("เพื่อรันตัวอย่างใดๆ คัดลอกโค้ดและ:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Replace paths with your actual files")
    print("3. Run the code!")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()
