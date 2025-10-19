# Sample Images / รูปภาพตัวอย่าง

This folder is for storing test images for car detection.
โฟลเดอร์นี้สำหรับเก็บรูปภาพทดสอบสำหรับการตรวจจับรถยนต์

## How to Use / วิธีการใช้งาน

1. Place your test images in this folder
   วางรูปภาพทดสอบของคุณในโฟลเดอร์นี้

2. Supported formats: JPG, PNG, JPEG
   รูปแบบที่รองรับ: JPG, PNG, JPEG

3. Run detection:
   รันการตรวจจับ:
   ```bash
   python src/car_detector.py --input images/your_image.jpg --output result.jpg
   ```

## Where to Find Test Images / หาภาพทดสอบได้ที่ไหน

You can find free test images from:
คุณสามารถหาภาพทดสอบฟรีได้จาก:

- [Unsplash](https://unsplash.com/s/photos/cars-traffic) - Free high-quality images
- [Pexels](https://www.pexels.com/search/traffic/) - Free stock photos
- [Pixabay](https://pixabay.com/images/search/cars/) - Free images
- Your own photos! / ภาพถ่ายของคุณเอง!

## Tips / เคล็ดลับ

- Use images with good lighting / ใช้รูปภาพที่มีแสงสว่างดี
- Higher resolution = better detection / ความละเอียดสูงกว่า = การตรวจจับที่ดีขึ้น
- Try different angles and scenarios / ลองมุมและสถานการณ์ต่างๆ
