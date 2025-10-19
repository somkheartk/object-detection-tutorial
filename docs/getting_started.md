# Getting Started with Car Object Detection
# เริ่มต้นใช้งานการตรวจจับรถยนต์

## Introduction / บทนำ

This guide will help you get started with car object detection using YOLOv8. By the end of this tutorial, you'll be able to detect cars in images and videos.

คู่มือนี้จะช่วยให้คุณเริ่มต้นใช้งานการตรวจจับรถยนต์ด้วย YOLOv8 เมื่อจบบทเรียนนี้ คุณจะสามารถตรวจจับรถยนต์ในรูปภาพและวิดีโอได้

## Prerequisites / ข้อกำหนดเบื้องต้น

Before starting, make sure you have:
ก่อนเริ่มต้น ตรวจสอบว่าคุณมี:

- Basic Python knowledge / ความรู้พื้นฐาน Python
- Python 3.8+ installed / Python 3.8 ขึ้นไปติดตั้งแล้ว
- Basic understanding of computer vision (helpful but not required) / ความเข้าใจพื้นฐานเกี่ยวกับคอมพิวเตอร์วิทัศน์ (เป็นประโยชน์แต่ไม่จำเป็น)

## Step-by-Step Installation / การติดตั้งทีละขั้นตอน

### 1. Set Up Python Environment / ตั้งค่าสภาพแวดล้อม Python

First, check your Python version:
ขั้นแรก ตรวจสอบเวอร์ชัน Python ของคุณ:

```bash
python --version
# or
python3 --version
```

You should see Python 3.8 or higher.
คุณควรเห็น Python 3.8 หรือสูงกว่า

### 2. Clone the Repository / โคลนโปรเจค

```bash
git clone https://github.com/somkheartk/object-detection-tutorial.git
cd object-detection-tutorial
```

### 3. Create Virtual Environment / สร้าง Virtual Environment

**Why use a virtual environment?** / **ทำไมต้องใช้ virtual environment?**
- Keeps project dependencies isolated / แยกการขึ้นต่อกันของโปรเจค
- Prevents conflicts with other projects / ป้องกันความขัดแย้งกับโปรเจคอื่น
- Makes it easier to manage packages / ทำให้จัดการแพ็คเกจง่ายขึ้น

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

You should see `(venv)` at the beginning of your command prompt.
คุณควรเห็น `(venv)` ที่จุดเริ่มต้นของ command prompt

### 4. Install Dependencies / ติดตั้งไลบรารี

```bash
pip install -r requirements.txt
```

This will install:
การดำเนินการนี้จะติดตั้ง:
- OpenCV for image/video processing / OpenCV สำหรับประมวลผลรูปภาพ/วิดีโอ
- PyTorch for deep learning / PyTorch สำหรับการเรียนรู้เชิงลึก
- YOLOv8 for object detection / YOLOv8 สำหรับการตรวจจับวัตถุ
- Other supporting libraries / ไลบรารีสนับสนุนอื่นๆ

**Note:** The first installation may take a few minutes, especially for PyTorch.
**หมายเหตุ:** การติดตั้งครั้งแรกอาจใช้เวลาสักครู่ โดยเฉพาะสำหรับ PyTorch

## Your First Detection / การตรวจจับครั้งแรกของคุณ

### Test 1: Run the Demo / ทดสอบที่ 1: รันตัวอย่าง

```bash
python demo.py
```

This will show you information about the available features.
การดำเนินการนี้จะแสดงข้อมูลเกี่ยวกับฟีเจอร์ที่มี

### Test 2: Detect Cars in a Sample Image / ทดสอบที่ 2: ตรวจจับรถในรูปภาพตัวอย่าง

First, you need a test image. You can:
ขั้นแรก คุณต้องมีรูปภาพทดสอบ คุณสามารถ:

1. Download a sample image from the internet / ดาวน์โหลดรูปภาพตัวอย่างจากอินเทอร์เน็ต
2. Use your own image of cars / ใช้รูปภาพรถยนต์ของคุณเอง
3. Take a photo with your phone / ถ่ายภาพด้วยมือถือของคุณ

Place your image in the `images` folder and run:
วางรูปภาพของคุณในโฟลเดอร์ `images` และรัน:

```bash
python src/car_detector.py --input images/your_image.jpg --output result.jpg
```

**What happens?** / **เกิดอะไรขึ้น?**
1. The script loads the YOLOv8 model (first time will download ~6MB)
2. Processes your image
3. Detects vehicles
4. Draws bounding boxes
5. Saves the result as `result.jpg`
6. Shows the result in a window

1. สคริปต์โหลดโมเดล YOLOv8 (ครั้งแรกจะดาวน์โหลดประมาณ 6MB)
2. ประมวลผลรูปภาพของคุณ
3. ตรวจจับยานพาหนะ
4. วาดกรอบล้อม
5. บันทึกผลลัพธ์เป็น `result.jpg`
6. แสดงผลลัพธ์ในหน้าต่าง

## Understanding the Code / ทำความเข้าใจโค้ด

Let's break down the main components:
มาแยกวิเคราะห์ส่วนประกอบหลัก:

### 1. Importing the Detector / นำเข้าตัวตรวจจับ

```python
from src.car_detector import CarDetector
```

This imports the `CarDetector` class that handles all detection logic.
การดำเนินการนี้นำเข้าคลาส `CarDetector` ที่จัดการตรรกะการตรวจจับทั้งหมด

### 2. Creating a Detector Instance / สร้างอินสแตนซ์ของตัวตรวจจับ

```python
detector = CarDetector(model_name='yolov8n.pt', conf_threshold=0.5)
```

**Parameters explained:** / **อธิบายพารามิเตอร์:**
- `model_name`: Which YOLOv8 model to use / โมเดล YOLOv8 ที่จะใช้
  - `yolov8n.pt` = Nano (fastest) / นาโน (เร็วที่สุด)
  - `yolov8s.pt` = Small / เล็ก
  - `yolov8m.pt` = Medium / กลาง
  - `yolov8l.pt` = Large / ใหญ่
  - `yolov8x.pt` = XLarge (most accurate) / ใหญ่พิเศษ (แม่นยำที่สุด)

- `conf_threshold`: Minimum confidence (0.0-1.0) / ความมั่นใจขั้นต่ำ (0.0-1.0)
  - 0.5 = 50% confident / มั่นใจ 50%
  - Higher = fewer but more accurate detections / สูงขึ้น = ตรวจจับน้อยลงแต่แม่นยำกว่า
  - Lower = more detections but less accurate / ต่ำลง = ตรวจจับมากขึ้นแต่แม่นยำน้อยลง

### 3. Detecting Cars / ตรวจจับรถยนต์

```python
image, detections = detector.detect_cars_in_image(
    'images/test.jpg',
    output_path='output.jpg'
)
```

**Returns:** / **ส่งคืน:**
- `image`: The annotated image with bounding boxes / รูปภาพที่มีกรอบล้อม
- `detections`: List of detected vehicles with details / รายการยานพาหนะที่ตรวจพบพร้อมรายละเอียด

### 4. Processing Results / ประมวลผลผลลัพธ์

```python
print(f"Found {len(detections)} vehicles")
for det in detections:
    print(f"  - {det['class_name']}: {det['confidence']:.2f}")
```

Each detection contains:
แต่ละการตรวจจับประกอบด้วย:
- `class_name`: Type of vehicle (car, bus, truck, motorcycle) / ประเภทของยานพาหนะ
- `confidence`: How confident the model is (0.0-1.0) / ความมั่นใจของโมเดล (0.0-1.0)
- `bbox`: Bounding box coordinates [x1, y1, x2, y2] / พิกัดกรอบล้อม

## Next Steps / ขั้นตอนต่อไป

Now that you've completed the basic setup:
ตอนนี้คุณได้ทำการตั้งค่าพื้นฐานเสร็จแล้ว:

1. **Try different images** / **ลองใช้รูปภาพต่างๆ**
   - Test with different lighting conditions / ทดสอบกับสภาพแสงต่างๆ
   - Try crowded scenes / ลองฉากที่แออัด
   - Test with different vehicle types / ทดสอบกับยานพาหนะประเภทต่างๆ

2. **Experiment with parameters** / **ทดลองกับพารามิเตอร์**
   - Try different models / ลองโมเดลต่างๆ
   - Adjust confidence threshold / ปรับค่าความมั่นใจ
   - Compare results / เปรียบเทียบผลลัพธ์

3. **Try video detection** / **ลองตรวจจับวิดีโอ**
   ```bash
   python src/car_detector.py --input video.mp4 --output output.mp4 --video
   ```

4. **Use webcam** / **ใช้เว็บแคม**
   ```bash
   python src/car_detector.py --input 0 --video
   ```

5. **Read the API documentation** / **อ่านเอกสาร API**
   - Check `docs/api_reference.md` for detailed API information
   - ดู `docs/api_reference.md` สำหรับข้อมูล API โดยละเอียด

## Common Questions / คำถามที่พบบ่อย

### Q: Why is the first run slow? / Q: ทำไมการรันครั้งแรกจึงช้า?
A: The first run downloads the YOLOv8 model (~6MB for nano model). Subsequent runs will be much faster.
A: การรันครั้งแรกดาวน์โหลดโมเดล YOLOv8 (ประมาณ 6MB สำหรับโมเดล nano) การรันครั้งถัดไปจะเร็วกว่ามาก

### Q: Can I use my own trained model? / Q: ฉันสามารถใช้โมเดลที่ฉันฝึกเองได้หรือไม่?
A: Yes! Just specify the path to your model file in the `model_name` parameter.
A: ได้! เพียงระบุพาธไปยังไฟล์โมเดลของคุณในพารามิเตอร์ `model_name`

### Q: What video formats are supported? / Q: รองรับรูปแบบวิดีโอใดบ้าง?
A: Most common formats: MP4, AVI, MOV, MKV. Depends on your OpenCV installation.
A: รูปแบบทั่วไปส่วนใหญ่: MP4, AVI, MOV, MKV ขึ้นอยู่กับการติดตั้ง OpenCV ของคุณ

### Q: Can I detect other objects? / Q: ฉันสามารถตรวจจับวัตถุอื่นได้หรือไม่?
A: Yes! YOLOv8 can detect 80 different object classes. Modify the `vehicle_classes` in the code.
A: ได้! YOLOv8 สามารถตรวจจับวัตถุ 80 คลาสที่แตกต่างกัน แก้ไข `vehicle_classes` ในโค้ด

## Troubleshooting / การแก้ไขปัญหา

If you encounter issues:
หากคุณพบปัญหา:

1. Make sure virtual environment is activated / ตรวจสอบว่าเปิดใช้งาน virtual environment แล้ว
2. Verify all dependencies are installed / ตรวจสอบว่าติดตั้งการขึ้นต่อกันทั้งหมดแล้ว
3. Check Python version (3.8+) / ตรวจสอบเวอร์ชัน Python (3.8+)
4. Ensure input files exist / ตรวจสอบว่าไฟล์อินพุตมีอยู่จริง
5. Check the main README for more troubleshooting tips / ดู README หลักสำหรับเคล็ดลับการแก้ไขปัญหาเพิ่มเติม

## Next Tutorial / บทเรียนต่อไป

Ready for more? Check out:
พร้อมสำหรับเนื้อหาเพิ่มเติมหรือไม่? ดู:

- `docs/advanced_usage.md` - Advanced features and customization
- `docs/api_reference.md` - Complete API documentation
- `docs/performance_tuning.md` - Optimization tips

Happy learning! / ขอให้เรียนรู้อย่างมีความสุข! 🎓
