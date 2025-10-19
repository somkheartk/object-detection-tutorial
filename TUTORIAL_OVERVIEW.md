# Tutorial Overview / ภาพรวมบทเรียน

## What You'll Learn / สิ่งที่คุณจะเรียนรู้

This tutorial teaches you how to develop a complete car object detection system using state-of-the-art YOLOv8 technology.

บทเรียนนี้สอนวิธีการพัฒนาระบบตรวจจับรถยนต์ที่สมบูรณ์โดยใช้เทคโนโลยี YOLOv8 ที่ทันสมัย

## What's Included / สิ่งที่รวมอยู่

### 1. Complete Source Code / ซอร์สโค้ดที่สมบูรณ์
- Production-ready car detector class
- Command-line interface
- Video and image processing
- Real-time webcam detection

### 2. Bilingual Documentation / เอกสารสองภาษา
- English and Thai throughout
- Step-by-step guides
- Code examples
- Troubleshooting help

### 3. Multiple Learning Paths / เส้นทางการเรียนรู้หลายแบบ

**Beginner Path** / **เส้นทางสำหรับผู้เริ่มต้น**:
1. Read README.md for overview
2. Follow docs/getting_started.md for installation
3. Run demo.py to see examples
4. Try detecting cars in your own images

**Intermediate Path** / **เส้นทางสำหรับระดับกลาง**:
1. Study src/car_detector.py implementation
2. Read docs/advanced_usage.md
3. Modify parameters and experiment
4. Process videos and use webcam

**Advanced Path** / **เส้นทางสำหรับระดับสูง**:
1. Review examples.py for integration patterns
2. Customize the detector for your needs
3. Implement batch processing
4. Build your own applications

## Technologies Used / เทคโนโลยีที่ใช้

- **YOLOv8**: Latest version of YOLO object detection
- **OpenCV**: Image and video processing
- **PyTorch**: Deep learning framework
- **Python**: Easy-to-learn programming language

## Vehicle Detection Capabilities / ความสามารถในการตรวจจับ

The system can detect:
ระบบสามารถตรวจจับ:

- 🚗 **Cars** / **รถยนต์**: Sedans, SUVs, hatchbacks
- 🏍️ **Motorcycles** / **รถจักรยานยนต์**: All two-wheelers
- 🚌 **Buses** / **รถบัส**: Public and private buses
- 🚚 **Trucks** / **รถบรรทุก**: Delivery and cargo trucks

## Real-World Applications / การประยุกต์ใช้ในโลกจริง

Learn to build:
เรียนรู้การสร้าง:

- Traffic monitoring systems / ระบบติดตามจราจร
- Parking management / การจัดการที่จอดรถ
- Security systems / ระบบรักษาความปลอดภัย
- Vehicle counting / การนับยานพาหนะ
- Smart city applications / แอปพลิเคชันเมืองอัจฉริยะ

## Quick Start / เริ่มต้นอย่างรวดเร็ว

### For Beginners / สำหรับผู้เริ่มต้น

```bash
# 1. Run quick start script
./quick_start.sh  # Linux/macOS
# or
quick_start.bat   # Windows

# 2. Try the demo
python demo.py

# 3. Detect cars in an image
python src/car_detector.py --input your_image.jpg --output result.jpg
```

### For Python Developers / สำหรับนักพัฒนา Python

```python
from src.car_detector import CarDetector

# Create detector
detector = CarDetector()

# Detect cars
image, detections = detector.detect_cars_in_image('image.jpg')

# Print results
for det in detections:
    print(f"{det['class_name']}: {det['confidence']:.2%}")
```

## Support and Learning / การสนับสนุนและการเรียนรู้

### Documentation Files / ไฟล์เอกสาร
- `README.md` - Main documentation
- `docs/getting_started.md` - Installation and first steps
- `docs/advanced_usage.md` - Advanced features
- `examples.py` - Code examples

### Getting Help / การขอความช่วยเหลือ
- Check documentation first
- Review code examples
- Try troubleshooting section in README
- Open an issue on GitHub

## What Makes This Tutorial Special / จุดเด่นของบทเรียนนี้

1. **Bilingual** / **สองภาษา**: Full English and Thai support
2. **Complete** / **สมบูรณ์**: From installation to advanced usage
3. **Practical** / **ใช้งานได้จริง**: Real code you can use in projects
4. **Modern** / **ทันสมัย**: Uses latest YOLOv8 technology
5. **Educational** / **เน้นการศึกษา**: Designed for learning

## Next Steps / ขั้นตอนต่อไป

After completing this tutorial, you'll be able to:
หลังจากจบบทเรียนนี้ คุณจะสามารถ:

✓ Detect vehicles in images and videos
✓ Understand YOLOv8 object detection
✓ Build your own detection applications
✓ Customize and extend the system
✓ Apply computer vision to real problems

---

Ready to start? Begin with the README.md file!
พร้อมที่จะเริ่มแล้วหรือยัง? เริ่มที่ไฟล์ README.md!

Happy Learning! / ขอให้เรียนรู้อย่างสนุก! 🚀
