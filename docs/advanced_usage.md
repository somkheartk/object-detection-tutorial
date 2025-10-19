# Advanced Usage Guide
# คู่มือการใช้งานขั้นสูง

## Custom Detection Settings / การตั้งค่าการตรวจจับแบบกำหนดเอง

### Filtering by Vehicle Type / กรองตามประเภทยานพาหนะ

You can modify the code to detect only specific vehicle types:
คุณสามารถแก้ไขโค้ดเพื่อตรวจจับเฉพาะประเภทยานพาหนะที่ต้องการ:

```python
from src.car_detector import CarDetector

# Create a custom detector for only cars (no motorcycles, buses, trucks)
detector = CarDetector()

# Modify the vehicle classes to only include cars
detector.vehicle_classes = {2: 'car'}  # Only cars

# Now detect
image, detections = detector.detect_cars_in_image('test.jpg')
```

### Custom Confidence Per Class / ความมั่นใจแบบกำหนดเองต่อคลาส

```python
def filter_detections_by_class(detections, min_conf_by_class):
    """
    Filter detections with different confidence thresholds per class.
    กรองการตรวจจับด้วยเกณฑ์ความมั่นใจที่แตกต่างกันสำหรับแต่ละคลาส
    
    Args:
        detections: List of detections
        min_conf_by_class: Dict mapping class_name to minimum confidence
    """
    filtered = []
    for det in detections:
        class_name = det['class_name']
        min_conf = min_conf_by_class.get(class_name, 0.5)
        if det['confidence'] >= min_conf:
            filtered.append(det)
    return filtered

# Example usage
image, detections = detector.detect_cars_in_image('test.jpg')

# Different thresholds for different vehicle types
filtered = filter_detections_by_class(detections, {
    'car': 0.6,        # Higher confidence for cars
    'motorcycle': 0.4, # Lower for motorcycles (harder to detect)
    'bus': 0.7,
    'truck': 0.7
})
```

## Working with Video Streams / การทำงานกับสตรีมวิดีโอ

### Processing Multiple Videos in Batch / ประมวลผลวิดีโอหลายไฟล์แบบแบตช์

```python
from pathlib import Path
from src.car_detector import CarDetector

def batch_process_videos(video_folder, output_folder):
    """
    Process all videos in a folder.
    ประมวลผลวิดีโอทั้งหมดในโฟลเดอร์
    """
    detector = CarDetector(model_name='yolov8s.pt', conf_threshold=0.6)
    
    video_folder = Path(video_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True)
    
    # Supported video formats
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    
    for video_path in video_folder.iterdir():
        if video_path.suffix.lower() in video_extensions:
            print(f"\nProcessing: {video_path.name}")
            output_path = output_folder / f"detected_{video_path.name}"
            
            try:
                detector.detect_cars_in_video(
                    str(video_path),
                    output_path=str(output_path),
                    show=False
                )
                print(f"Saved to: {output_path}")
            except Exception as e:
                print(f"Error processing {video_path.name}: {e}")

# Usage
batch_process_videos('input_videos/', 'output_videos/')
```

### Real-time Stream Analysis / การวิเคราะห์สตรีมแบบเรียลไทม์

```python
import cv2
from src.car_detector import CarDetector
from collections import deque
import time

class StreamAnalyzer:
    """
    Analyze vehicle traffic in real-time.
    วิเคราะห์การจราจรของยานพาหนะแบบเรียลไทม์
    """
    
    def __init__(self, detector):
        self.detector = detector
        self.vehicle_counts = deque(maxlen=30)  # Last 30 frames
        self.fps_history = deque(maxlen=30)
    
    def analyze_stream(self, video_source=0):
        """Analyze video stream with statistics."""
        cap = cv2.VideoCapture(video_source)
        
        while True:
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect vehicles
            results = self.detector.model(frame, verbose=False)
            
            # Count vehicles
            vehicle_count = 0
            for result in results:
                for box in result.boxes:
                    if int(box.cls[0]) in self.detector.vehicle_classes:
                        vehicle_count += 1
            
            # Calculate statistics
            self.vehicle_counts.append(vehicle_count)
            avg_vehicles = sum(self.vehicle_counts) / len(self.vehicle_counts)
            
            # Calculate FPS
            fps = 1 / (time.time() - start_time)
            self.fps_history.append(fps)
            avg_fps = sum(self.fps_history) / len(self.fps_history)
            
            # Display statistics
            cv2.putText(frame, f"Vehicles: {vehicle_count}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Avg: {avg_vehicles:.1f}", (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"FPS: {avg_fps:.1f}", (10, 110),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Stream Analysis', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

# Usage
detector = CarDetector(model_name='yolov8n.pt')
analyzer = StreamAnalyzer(detector)
analyzer.analyze_stream(0)  # 0 for webcam
```

## Advanced Model Configuration / การตั้งค่าโมเดลขั้นสูง

### Using Custom Trained Models / การใช้โมเดลที่ฝึกเอง

```python
from src.car_detector import CarDetector

# Use your custom trained model
detector = CarDetector(
    model_name='path/to/your/custom_model.pt',
    conf_threshold=0.6
)

# You may need to update the vehicle_classes dictionary
# คุณอาจต้องอัปเดตพจนานุกรม vehicle_classes
detector.vehicle_classes = {
    0: 'car',
    1: 'truck',
    2: 'bus',
    # Add your custom classes here
}
```

### Model Ensemble / การรวมโมเดล

```python
class EnsembleDetector:
    """
    Use multiple models for better accuracy.
    ใช้หลายโมเดลเพื่อความแม่นยำที่ดีขึ้น
    """
    
    def __init__(self, model_names, conf_threshold=0.5):
        self.detectors = [
            CarDetector(model_name=name, conf_threshold=conf_threshold)
            for name in model_names
        ]
    
    def detect_with_voting(self, image_path, vote_threshold=2):
        """
        Detect using multiple models and vote on results.
        ตรวจจับโดยใช้หลายโมเดลและลงคะแนนผลลัพธ์
        """
        all_detections = []
        
        for detector in self.detectors:
            _, detections = detector.detect_cars_in_image(
                image_path, show=False
            )
            all_detections.append(detections)
        
        # Merge detections with voting logic
        # (Implementation depends on your requirements)
        # รวมการตรวจจับด้วยตรรกะการลงคะแนน
        # (การนำไปใช้ขึ้นอยู่กับความต้องการของคุณ)
        
        return merged_detections

# Usage
ensemble = EnsembleDetector([
    'yolov8n.pt',
    'yolov8s.pt',
    'yolov8m.pt'
])
results = ensemble.detect_with_voting('test.jpg')
```

## Performance Optimization / การเพิ่มประสิทธิภาพ

### Using GPU Acceleration / การใช้ GPU Acceleration

```python
import torch

# Check if GPU is available
if torch.cuda.is_available():
    print(f"GPU available: {torch.cuda.get_device_name(0)}")
    device = 'cuda'
else:
    print("GPU not available, using CPU")
    device = 'cpu'

# The model will automatically use GPU if available
detector = CarDetector(model_name='yolov8n.pt')
```

### Batch Processing for Images / การประมวลผลแบบแบตช์สำหรับรูปภาพ

```python
from pathlib import Path
import cv2
from src.car_detector import CarDetector

def batch_detect_images(image_folder, output_folder, batch_size=4):
    """
    Process multiple images efficiently.
    ประมวลผลรูปภาพหลายไฟล์อย่างมีประสิทธิภาพ
    """
    detector = CarDetector(model_name='yolov8n.pt')
    
    image_folder = Path(image_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True)
    
    image_paths = list(image_folder.glob('*.jpg')) + list(image_folder.glob('*.png'))
    
    # Process in batches
    for i in range(0, len(image_paths), batch_size):
        batch = image_paths[i:i+batch_size]
        
        for img_path in batch:
            output_path = output_folder / f"detected_{img_path.name}"
            detector.detect_cars_in_image(
                str(img_path),
                output_path=str(output_path),
                show=False
            )
            print(f"Processed: {img_path.name}")

# Usage
batch_detect_images('input_images/', 'output_images/', batch_size=8)
```

### Frame Skipping for Faster Video Processing / การข้ามเฟรมเพื่อประมวลผลวิดีโอเร็วขึ้น

```python
import cv2
from src.car_detector import CarDetector

def process_video_with_frame_skip(video_path, output_path, skip_frames=2):
    """
    Process every Nth frame for faster processing.
    ประมวลผลทุกเฟรมที่ N เพื่อประมวลผลเร็วขึ้น
    
    Args:
        skip_frames: Process every (skip_frames + 1)th frame
    """
    detector = CarDetector(model_name='yolov8n.pt')
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frame_count = 0
    last_detections = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Only process every Nth frame
        if frame_count % (skip_frames + 1) == 0:
            results = detector.model(frame, verbose=False)
            # Store detections for reuse
            last_detections = results
        else:
            # Reuse last detections
            results = last_detections
        
        # Draw detections (you'd need to implement this)
        # วาดการตรวจจับ (คุณจะต้องนำสิ่งนี้ไปใช้)
        
        writer.write(frame)
        frame_count += 1
    
    cap.release()
    writer.release()

# Usage - Process every 3rd frame
process_video_with_frame_skip('input.mp4', 'output.mp4', skip_frames=2)
```

## Integration Examples / ตัวอย่างการรวมระบบ

### REST API Server / เซิร์ฟเวอร์ REST API

```python
from flask import Flask, request, jsonify
from src.car_detector import CarDetector
import base64
import cv2
import numpy as np

app = Flask(__name__)
detector = CarDetector(model_name='yolov8n.pt')

@app.route('/detect', methods=['POST'])
def detect():
    """
    API endpoint for car detection.
    จุดสิ้นสุด API สำหรับการตรวจจับรถยนต์
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    # Read image
    file = request.files['image']
    image = cv2.imdecode(
        np.frombuffer(file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )
    
    # Detect
    _, detections = detector.detect_cars_in_image(
        image,  # Can also accept numpy array
        show=False
    )
    
    # Format response
    response = {
        'vehicle_count': len(detections),
        'detections': detections
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Command-line Interface with Rich Output / อินเทอร์เฟซบรรทัดคำสั่งพร้อมเอาต์พุตที่สมบูรณ์

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track
from src.car_detector import CarDetector

console = Console()

def detect_with_rich_output(image_path):
    """Display detection results with rich formatting."""
    
    console.print("[bold green]Starting car detection...[/bold green]")
    
    detector = CarDetector(model_name='yolov8n.pt')
    image, detections = detector.detect_cars_in_image(
        image_path,
        show=False
    )
    
    # Create results table
    table = Table(title="Detection Results")
    table.add_column("ID", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Confidence", style="green")
    table.add_column("Position", style="blue")
    
    for i, det in enumerate(detections, 1):
        x1, y1, x2, y2 = det['bbox']
        table.add_row(
            str(i),
            det['class_name'],
            f"{det['confidence']:.2%}",
            f"({x1}, {y1}) -> ({x2}, {y2})"
        )
    
    console.print(table)
    console.print(f"\n[bold]Total vehicles detected: {len(detections)}[/bold]")

# Usage
detect_with_rich_output('test.jpg')
```

## Tips and Best Practices / เคล็ดลับและแนวทางปฏิบัติที่ดีที่สุด

1. **Choose the Right Model Size** / **เลือกขนาดโมเดลที่เหมาะสม**
   - For real-time: yolov8n.pt or yolov8s.pt
   - For accuracy: yolov8l.pt or yolov8x.pt
   - สำหรับเรียลไทม์: yolov8n.pt หรือ yolov8s.pt
   - สำหรับความแม่นยำ: yolov8l.pt หรือ yolov8x.pt

2. **Optimize Input Resolution** / **เพิ่มประสิทธิภาพความละเอียดอินพุต**
   - Resize large images before processing / ปรับขนาดรูปภาพขนาดใหญ่ก่อนประมวลผล
   - Balance between speed and accuracy / สมดุลระหว่างความเร็วและความแม่นยำ

3. **Use Appropriate Confidence Thresholds** / **ใช้เกณฑ์ความมั่นใจที่เหมาะสม**
   - Too low: Many false positives / ต่ำเกินไป: ผลบวกลวงมาก
   - Too high: Miss some detections / สูงเกินไป: พลาดการตรวจจับบางอย่าง

4. **Monitor Performance** / **ติดตามประสิทธิภาพ**
   - Track FPS and latency / ติดตาม FPS และความหน่วง
   - Profile your code / วิเคราะห์โค้ดของคุณ
   - Optimize bottlenecks / เพิ่มประสิทธิภาพจุดคอขวด

For more information, check the main README and other documentation files.
สำหรับข้อมูลเพิ่มเติม โปรดดู README หลักและไฟล์เอกสารอื่นๆ
