# Object Detection Tutorial - Car Detection
# บทเรียนการตรวจจับวัตถุ - การตรวจจับรถยนต์

## 🚗 Overview / ภาพรวม

This tutorial teaches you how to develop an object detection program for detecting cars and other vehicles using YOLOv8, one of the most advanced and efficient object detection models.

บทเรียนนี้สอนวิธีการพัฒนาโปรแกรมตรวจจับวัตถุสำหรับการตรวจจับรถยนต์และยานพาหนะอื่นๆ โดยใช้ YOLOv8 ซึ่งเป็นหนึ่งในโมเดลการตรวจจับวัตถุที่ทันสมัยและมีประสิทธิภาพที่สุด

### Features / คุณสมบัติ

- ✅ Detect cars, motorcycles, buses, and trucks / ตรวจจับรถยนต์ รถจักรยานยนต์ รถบัส และรถบรรทุก
- ✅ Process images and videos / ประมวลผลรูปภาพและวิดีโอ
- ✅ Real-time detection from webcam / ตรวจจับแบบเรียลไทม์จากเว็บแคม
- ✅ Easy-to-use Python API / API ของ Python ที่ใช้งานง่าย
- ✅ Bilingual documentation (English/Thai) / เอกสารสองภาษา (อังกฤษ/ไทย)

## 📋 Requirements / ความต้องการ

### System Requirements / ความต้องการของระบบ
- Python 3.8 or higher / Python 3.8 ขึ้นไป
- Operating System: Windows, Linux, or macOS / ระบบปฏิบัติการ: Windows, Linux หรือ macOS
- (Optional) NVIDIA GPU with CUDA for faster processing / (ตัวเลือก) NVIDIA GPU พร้อม CUDA สำหรับการประมวลผลที่เร็วขึ้น

### Python Dependencies / ไลบรารีที่ต้องการ
- OpenCV (cv2)
- NumPy
- PyTorch
- Ultralytics YOLOv8
- Pillow
- Matplotlib

## 🚀 Installation / การติดตั้ง

### Step 1: Clone the Repository / ขั้นตอนที่ 1: โคลนโปรเจค

```bash
git clone https://github.com/somkheartk/object-detection-tutorial.git
cd object-detection-tutorial
```

### Step 2: Create Virtual Environment (Recommended) / ขั้นตอนที่ 2: สร้าง Virtual Environment (แนะนำ)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies / ขั้นตอนที่ 3: ติดตั้งไลบรารี

```bash
pip install -r requirements.txt
```

This will automatically download and install all required packages including YOLOv8.

การดำเนินการนี้จะดาวน์โหลดและติดตั้งแพ็คเกจที่จำเป็นทั้งหมด รวมถึง YOLOv8

## 📚 Usage / วิธีการใช้งาน

### Basic Usage / การใช้งานพื้นฐาน

#### 1. Detect Cars in an Image / ตรวจจับรถยนต์ในรูปภาพ

```bash
python src/car_detector.py --input path/to/image.jpg --output result.jpg
```

**Example / ตัวอย่าง:**
```bash
python src/car_detector.py --input images/traffic.jpg --output output/detected.jpg
```

#### 2. Detect Cars in a Video / ตรวจจับรถยนต์ในวิดีโอ

```bash
python src/car_detector.py --input path/to/video.mp4 --output result.mp4 --video
```

#### 3. Real-time Detection from Webcam / ตรวจจับแบบเรียลไทม์จากเว็บแคม

```bash
python src/car_detector.py --input 0 --video
```

### Advanced Usage / การใช้งานขั้นสูง

#### Change Model Size / เปลี่ยนขนาดโมเดล

YOLOv8 provides multiple model sizes. Larger models are more accurate but slower.
YOLOv8 มีหลายขนาดโมเดล โมเดลที่ใหญ่กว่าจะแม่นยำกว่าแต่ช้ากว่า

```bash
# Nano model (fastest) / โมเดล Nano (เร็วที่สุด)
python src/car_detector.py --input image.jpg --model yolov8n.pt

# Small model / โมเดล Small
python src/car_detector.py --input image.jpg --model yolov8s.pt

# Medium model / โมเดล Medium
python src/car_detector.py --input image.jpg --model yolov8m.pt

# Large model / โมเดล Large
python src/car_detector.py --input image.jpg --model yolov8l.pt

# XLarge model (most accurate) / โมเดล XLarge (แม่นยำที่สุด)
python src/car_detector.py --input image.jpg --model yolov8x.pt
```

#### Adjust Confidence Threshold / ปรับค่าความมั่นใจ

Control how confident the model should be before reporting a detection (0.0-1.0):
ควบคุมระดับความมั่นใจที่โมเดลควรมีก่อนรายงานการตรวจจับ (0.0-1.0):

```bash
# Higher confidence (fewer, more accurate detections)
python src/car_detector.py --input image.jpg --conf 0.7

# Lower confidence (more detections, but less accurate)
python src/car_detector.py --input image.jpg --conf 0.3
```

### Running the Demo / เรียกใช้งานตัวอย่าง

```bash
# Show demo information
python demo.py

# Test with your own image
python demo.py --image path/to/your/image.jpg

# Test with your own video
python demo.py --video path/to/your/video.mp4
```

## 🔧 Command Line Options / ตัวเลือกบรรทัดคำสั่ง

| Option | Short | Description | คำอธิบาย |
|--------|-------|-------------|----------|
| `--input` | `-i` | Input image/video path or camera index | พาธของรูปภาพ/วิดีโอหรือหมายเลขกล้อง |
| `--output` | `-o` | Output path to save result | พาธสำหรับบันทึกผลลัพธ์ |
| `--model` | `-m` | YOLOv8 model size | ขนาดของโมเดล YOLOv8 |
| `--conf` | `-c` | Confidence threshold (0.0-1.0) | ค่าความมั่นใจ (0.0-1.0) |
| `--video` | `-v` | Process as video | ประมวลผลเป็นวิดีโอ |
| `--no-show` | | Don't display output window | ไม่แสดงหน้าต่างผลลัพธ์ |

## 🎓 How It Works / วิธีการทำงาน

### YOLOv8 Architecture / สถาปัตยกรรมของ YOLOv8

YOLO (You Only Look Once) is a state-of-the-art object detection algorithm that:
YOLO (You Only Look Once) เป็นอัลกอริธึมการตรวจจับวัตถุที่ทันสมัยซึ่ง:

1. **Single Pass Detection** / **การตรวจจับครั้งเดียว**: Looks at the entire image once to make predictions
   - มองภาพทั้งหมดเพียงครั้งเดียวเพื่อทำการทำนาย

2. **Real-time Performance** / **ประสิทธิภาพแบบเรียลไทม์**: Fast enough for real-time applications
   - เร็วพอสำหรับการใช้งานแบบเรียลไทม์

3. **Bounding Box Prediction** / **การทำนายกรอบล้อม**: Predicts bounding boxes and class probabilities directly
   - ทำนายกรอบล้อมและความน่าจะเป็นของคลาสโดยตรง

### Detection Process / กระบวนการตรวจจับ

```
Input Image → YOLOv8 Model → Detection Results → Post-processing → Output
รูปภาพ → โมเดล YOLOv8 → ผลการตรวจจับ → การประมวลผลหลัง → ผลลัพธ์
```

## 📖 Code Examples / ตัวอย่างโค้ด

### Example 1: Basic Image Detection / ตัวอย่างที่ 1: การตรวจจับรูปภาพพื้นฐาน

```python
from src.car_detector import CarDetector

# Create detector
detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.5)

# Detect cars in image
image, detections = detector.detect_cars_in_image(
    'images/traffic.jpg',
    output_path='output.jpg'
)

# Print results
print(f"Found {len(detections)} vehicles")
for det in detections:
    print(f"  - {det['class_name']}: {det['confidence']:.2f}")
```

### Example 2: Video Processing / ตัวอย่างที่ 2: การประมวลผลวิดีโอ

```python
from src.car_detector import CarDetector

# Create detector
detector = CarDetector(model_name='yolov8s.pt', conf_threshold=0.6)

# Process video
detector.detect_cars_in_video(
    'traffic_video.mp4',
    output_path='detected_video.mp4',
    show=True
)
```

### Example 3: Webcam Detection / ตัวอย่างที่ 3: การตรวจจับจากเว็บแคม

```python
from src.car_detector import CarDetector

# Create detector
detector = CarDetector()

# Use webcam (camera index 0)
detector.detect_cars_in_video(0, show=True)
```

## 🎯 Vehicle Classes Detected / ประเภทยานพาหนะที่ตรวจจับได้

The model can detect the following vehicle types:
โมเดลสามารถตรวจจับยานพาหนะประเภทต่อไปนี้:

- 🚗 **Car** / **รถยนต์**: Personal vehicles, sedans, SUVs
- 🏍️ **Motorcycle** / **รถจักรยานยนต์**: Motorcycles, scooters
- 🚌 **Bus** / **รถบัส**: Public buses, coaches
- 🚚 **Truck** / **รถบรรทุก**: Delivery trucks, cargo trucks

## 📊 Performance Tips / เคล็ดลับด้านประสิทธิภาพ

### For Better Speed / เพื่อความเร็วที่ดีขึ้น:
- Use smaller models (yolov8n.pt or yolov8s.pt) / ใช้โมเดลที่เล็กกว่า
- Reduce input image resolution / ลดความละเอียดของภาพ
- Use GPU if available / ใช้ GPU ถ้ามี

### For Better Accuracy / เพื่อความแม่นยำที่ดีขึ้น:
- Use larger models (yolov8l.pt or yolov8x.pt) / ใช้โมเดลที่ใหญ่กว่า
- Increase confidence threshold / เพิ่มค่าความมั่นใจ
- Use high-quality input images / ใช้รูปภาพคุณภาพสูง

## 🐛 Troubleshooting / การแก้ไขปัญหา

### Common Issues / ปัญหาที่พบบ่อย

**1. "Cannot read image" Error**
```
Solution: Check if the image path is correct and the file exists
แก้ไข: ตรวจสอบว่าพาธของรูปภาพถูกต้องและไฟล์มีอยู่จริง
```

**2. Model Download Issues**
```
Solution: The first run will download the model. Ensure internet connection
แก้ไข: การรันครั้งแรกจะดาวน์โหลดโมเดล ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
```

**3. Slow Performance**
```
Solution: Use a smaller model (yolov8n.pt) or enable GPU
แก้ไข: ใช้โมเดลที่เล็กกว่า (yolov8n.pt) หรือเปิดใช้งาน GPU
```

**4. "No module named 'ultralytics'" Error**
```
Solution: Install requirements: pip install -r requirements.txt
แก้ไข: ติดตั้งไลบรารี: pip install -r requirements.txt
```

## 📁 Project Structure / โครงสร้างโปรเจค

```
object-detection-tutorial/
├── src/
│   └── car_detector.py      # Main detection script / สคริปต์หลัก
├── images/                   # Sample images / รูปภาพตัวอย่าง
├── models/                   # Model files (auto-downloaded) / ไฟล์โมเดล
├── docs/                     # Documentation / เอกสาร
├── demo.py                   # Demo script / สคริปต์ตัวอย่าง
├── requirements.txt          # Python dependencies / ไลบรารีที่ต้องการ
└── README.md                 # This file / ไฟล์นี้
```

## 🎓 Learning Resources / แหล่งเรียนรู้

### Tutorials / บทเรียน
- [YOLOv8 Official Documentation](https://docs.ultralytics.com/)
- [OpenCV Python Tutorial](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)

### Research Papers / บทความวิชาการ
- [YOLOv8 Paper](https://arxiv.org/abs/2305.09972)
- [YOLO: Real-Time Object Detection](https://arxiv.org/abs/1506.02640)

## 🤝 Contributing / การมีส่วนร่วม

Contributions are welcome! Feel free to:
ยินดีรับการมีส่วนร่วม! คุณสามารถ:

- Report bugs / รายงานข้อผิดพลาด
- Suggest new features / แนะนำฟีเจอร์ใหม่
- Submit pull requests / ส่ง pull requests
- Improve documentation / ปรับปรุงเอกสาร

## 📄 License / ใบอนุญาต

This project is licensed under the MIT License.
โปรเจคนี้อยู่ภายใต้ใบอนุญาต MIT

## 👨‍💻 Author / ผู้เขียน

Created for educational purposes to teach object detection.
สร้างขึ้นเพื่อวัตถุประสงค์ทางการศึกษาเพื่อสอนการตรวจจับวัตถุ

## 📞 Support / การสนับสนุน

If you have questions or need help:
หากคุณมีคำถามหรือต้องการความช่วยเหลือ:

- Open an issue on GitHub / เปิด issue บน GitHub
- Check the documentation in the `docs` folder / ดูเอกสารในโฟลเดอร์ `docs`

---

## 🚀 Quick Start Guide / คู่มือเริ่มต้นด่วน

1. **Install dependencies** / **ติดตั้งไลบรารี**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run demo** / **รันตัวอย่าง**
   ```bash
   python demo.py
   ```

3. **Detect cars in your image** / **ตรวจจับรถในรูปภาพของคุณ**
   ```bash
   python src/car_detector.py --input your_image.jpg --output result.jpg
   ```

Happy detecting! / ขอให้ตรวจจับอย่างสนุก! 🚗✨