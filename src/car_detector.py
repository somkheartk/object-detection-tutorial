"""
Car Object Detection using YOLOv8
==================================
This script demonstrates how to detect cars in images and videos using YOLOv8.
สคริปต์นี้แสดงวิธีการตรวจจับรถยนต์ในรูปภาพและวิดีโอโดยใช้ YOLOv8

Author: Object Detection Tutorial
License: MIT
"""

import cv2
import argparse
from pathlib import Path
from ultralytics import YOLO
import numpy as np


class CarDetector:
    """
    A class for detecting cars in images and videos using YOLOv8.
    คลาสสำหรับการตรวจจับรถยนต์ในรูปภาพและวิดีโอโดยใช้ YOLOv8
    """
    
    def __init__(self, model_name='yolov8n.pt', conf_threshold=0.5):
        """
        Initialize the car detector.
        
        Args:
            model_name (str): YOLOv8 model name (yolov8n.pt, yolov8s.pt, etc.)
            conf_threshold (float): Confidence threshold for detections
        """
        print(f"Loading model: {model_name}")
        self.model = YOLO(model_name)
        self.conf_threshold = conf_threshold
        
        # COCO dataset class IDs for vehicles
        # รหัสคลาสสำหรับยานพาหนะใน COCO dataset
        self.vehicle_classes = {
            2: 'car',           # รถยนต์
            3: 'motorcycle',    # รถจักรยานยนต์
            5: 'bus',          # รถบัส
            7: 'truck'         # รถบรรทุก
        }
    
    def detect_cars_in_image(self, image_path, output_path=None, show=True):
        """
        Detect cars in an image.
        ตรวจจับรถยนต์ในรูปภาพ
        
        Args:
            image_path (str): Path to input image
            output_path (str): Path to save output image (optional)
            show (bool): Whether to display the result
        
        Returns:
            tuple: (annotated_image, detections)
        """
        # Read image / อ่านรูปภาพ
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Cannot read image from {image_path}")
        
        # Run inference / ทำการตรวจจับ
        results = self.model(image, conf=self.conf_threshold)
        
        # Filter only vehicle detections / กรองเฉพาะการตรวจจับยานพาหนะ
        detections = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                if class_id in self.vehicle_classes:
                    conf = float(box.conf[0])
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    detections.append({
                        'class_id': class_id,
                        'class_name': self.vehicle_classes[class_id],
                        'confidence': conf,
                        'bbox': [int(x1), int(y1), int(x2), int(y2)]
                    })
        
        # Draw detections / วาดกรอบการตรวจจับ
        annotated_image = image.copy()
        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            label = f"{det['class_name']}: {det['confidence']:.2f}"
            
            # Draw rectangle / วาดกรอบสี่เหลี่ยม
            cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw label / วาดป้ายข้อความ
            (label_width, label_height), _ = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2
            )
            cv2.rectangle(
                annotated_image, 
                (x1, y1 - label_height - 10), 
                (x1 + label_width, y1), 
                (0, 255, 0), 
                -1
            )
            cv2.putText(
                annotated_image, 
                label, 
                (x1, y1 - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.6, 
                (0, 0, 0), 
                2
            )
        
        # Save output / บันทึกผลลัพธ์
        if output_path:
            cv2.imwrite(str(output_path), annotated_image)
            print(f"Saved output to: {output_path}")
        
        # Display result / แสดงผลลัพธ์
        if show:
            cv2.imshow('Car Detection', annotated_image)
            print("Press any key to close the window...")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        print(f"Detected {len(detections)} vehicle(s)")
        for i, det in enumerate(detections, 1):
            print(f"  {i}. {det['class_name']} (confidence: {det['confidence']:.2f})")
        
        return annotated_image, detections
    
    def detect_cars_in_video(self, video_path, output_path=None, show=True):
        """
        Detect cars in a video.
        ตรวจจับรถยนต์ในวิดีโอ
        
        Args:
            video_path (str): Path to input video or camera index (0 for webcam)
            output_path (str): Path to save output video (optional)
            show (bool): Whether to display the result
        """
        # Open video / เปิดวิดีโอ
        if isinstance(video_path, int) or video_path.isdigit():
            cap = cv2.VideoCapture(int(video_path))
        else:
            cap = cv2.VideoCapture(str(video_path))
        
        if not cap.isOpened():
            raise ValueError(f"Cannot open video from {video_path}")
        
        # Get video properties / รับข้อมูลวิดีโอ
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Setup video writer / ตั้งค่าตัวเขียนวิดีโอ
        writer = None
        if output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
        
        frame_count = 0
        print("Processing video... Press 'q' to quit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            
            # Run inference / ทำการตรวจจับ
            results = self.model(frame, conf=self.conf_threshold, verbose=False)
            
            # Filter and draw vehicles / กรองและวาดยานพาหนะ
            vehicle_count = 0
            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    if class_id in self.vehicle_classes:
                        vehicle_count += 1
                        conf = float(box.conf[0])
                        x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
                        label = f"{self.vehicle_classes[class_id]}: {conf:.2f}"
                        
                        # Draw detection / วาดการตรวจจับ
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(
                            frame, label, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
                        )
            
            # Add frame info / เพิ่มข้อมูลเฟรม
            info_text = f"Frame: {frame_count} | Vehicles: {vehicle_count}"
            cv2.putText(
                frame, info_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )
            
            # Save frame / บันทึกเฟรม
            if writer:
                writer.write(frame)
            
            # Display frame / แสดงเฟรม
            if show:
                cv2.imshow('Car Detection', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        # Cleanup / ทำความสะอาด
        cap.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()
        
        print(f"Processed {frame_count} frames")
        if output_path:
            print(f"Saved output to: {output_path}")


def main():
    """Main function to run the car detector from command line."""
    parser = argparse.ArgumentParser(
        description='Car Object Detection using YOLOv8 / ตรวจจับรถยนต์ด้วย YOLOv8'
    )
    parser.add_argument(
        '--input', '-i', type=str, required=True,
        help='Path to input image/video or camera index (0 for webcam)'
    )
    parser.add_argument(
        '--output', '-o', type=str, default=None,
        help='Path to save output image/video'
    )
    parser.add_argument(
        '--model', '-m', type=str, default='yolov8n.pt',
        choices=['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'],
        help='YOLOv8 model size (n=nano, s=small, m=medium, l=large, x=xlarge)'
    )
    parser.add_argument(
        '--conf', '-c', type=float, default=0.5,
        help='Confidence threshold (0.0-1.0)'
    )
    parser.add_argument(
        '--no-show', action='store_true',
        help='Do not display the output'
    )
    parser.add_argument(
        '--video', '-v', action='store_true',
        help='Process as video instead of image'
    )
    
    args = parser.parse_args()
    
    # Create detector / สร้างตัวตรวจจับ
    detector = CarDetector(model_name=args.model, conf_threshold=args.conf)
    
    # Process input / ประมวลผลอินพุต
    try:
        if args.video:
            detector.detect_cars_in_video(
                args.input, 
                output_path=args.output, 
                show=not args.no_show
            )
        else:
            detector.detect_cars_in_image(
                args.input, 
                output_path=args.output, 
                show=not args.no_show
            )
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
