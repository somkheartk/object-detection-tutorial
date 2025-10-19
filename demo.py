"""
Demo script for car detection
สคริปต์ตัวอย่างสำหรับการตรวจจับรถยนต์

This script demonstrates basic usage of the car detector.
สคริปต์นี้แสดงการใช้งานพื้นฐานของตัวตรวจจับรถยนต์
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from car_detector import CarDetector


def demo_image_detection():
    """Demo: Detect cars in an image"""
    print("=" * 60)
    print("Demo 1: Image Detection / การตรวจจับในรูปภาพ")
    print("=" * 60)
    
    # Initialize detector / สร้างตัวตรวจจับ
    detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.5)
    
    # Example: Detect cars in an image
    # ตัวอย่าง: ตรวจจับรถยนต์ในรูปภาพ
    print("\nNote: Place your test image in the 'images' folder")
    print("หมายเหตุ: วางรูปภาพทดสอบของคุณในโฟลเดอร์ 'images'")
    print("\nExample usage:")
    print("  python demo.py --image path/to/your/image.jpg")
    print("\nOr use our car_detector.py directly:")
    print("  python src/car_detector.py --input images/test.jpg --output output.jpg")


def demo_video_detection():
    """Demo: Detect cars in a video"""
    print("\n" + "=" * 60)
    print("Demo 2: Video Detection / การตรวจจับในวิดีโอ")
    print("=" * 60)
    
    print("\nTo process a video file:")
    print("  python src/car_detector.py --input video.mp4 --output output.mp4 --video")
    
    print("\nTo use webcam (camera 0):")
    print("  python src/car_detector.py --input 0 --video")


def demo_with_custom_image():
    """Demo with user-provided image"""
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='Path to test image')
    parser.add_argument('--video', type=str, help='Path to test video')
    args, _ = parser.parse_known_args()
    
    if args.image:
        print(f"\nDetecting cars in: {args.image}")
        detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.5)
        detector.detect_cars_in_image(args.image, output_path='output.jpg')
    elif args.video:
        print(f"\nDetecting cars in video: {args.video}")
        detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.5)
        detector.detect_cars_in_video(args.video, output_path='output.mp4', show=True)
    else:
        demo_image_detection()
        demo_video_detection()
        
        print("\n" + "=" * 60)
        print("Additional Information / ข้อมูลเพิ่มเติม")
        print("=" * 60)
        print("\nAvailable YOLOv8 models (from fastest to most accurate):")
        print("โมเดล YOLOv8 ที่มี (จากเร็วที่สุดถึงแม่นยำที่สุด):")
        print("  - yolov8n.pt (nano)   - Fastest, good for real-time")
        print("  - yolov8s.pt (small)")
        print("  - yolov8m.pt (medium)")
        print("  - yolov8l.pt (large)")
        print("  - yolov8x.pt (xlarge) - Most accurate, slowest")
        
        print("\nFor more examples, check the documentation in the 'docs' folder")
        print("สำหรับตัวอย่างเพิ่มเติม โปรดดูเอกสารในโฟลเดอร์ 'docs'")


if __name__ == '__main__':
    demo_with_custom_image()
