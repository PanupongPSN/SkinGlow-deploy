from flask import Flask, request, jsonify
from flask_cors import CORS  # สำหรับการจัดการ CORS
import tensorflow as tf
from PIL import Image, UnidentifiedImageError
import numpy as np
import io

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุกเส้นทางในแอปพลิเคชัน

# โหลดโมเดล
model_path = r'E:\Project END\skinglow\wp-content\plugins\skin_model\AcneDetection_model.h5'
model = tf.keras.models.load_model(model_path)
print("Model loaded successfully.")  # ยืนยันว่าโมเดลถูกโหลดเรียบร้อยแล้ว

def preprocess_image(uploaded_file):
    """
    ฟังก์ชันสำหรับเตรียมรูปภาพที่อัปโหลดก่อนการทำนาย
    """
    try:
        # เปิดและปรับขนาดรูปภาพ
        img = Image.open(uploaded_file)
        img = img.resize((150, 150))  # ปรับขนาดให้ตรงกับที่โมเดลต้องการ
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # ปรับขนาดพิกเซลให้อยู่ในช่วง 0-1
        return img_array
    except UnidentifiedImageError:
        return None

@app.route('/predict', methods=['POST'])
def predict():
    """
    เส้นทางสำหรับการทำนายรูปภาพที่อัปโหลด
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    processed_image = preprocess_image(file)

    if processed_image is None:
        return jsonify({'error': 'Cannot process the uploaded file as an image'}), 400

    try:
        # ทำนายผลด้วยโมเดล
        predictions = model.predict(processed_image)
        class_labels = ['Acne', 'Clear', 'Comedo', 'Wrinkles']

        predicted_class = class_labels[np.argmax(predictions)]
        confidence = np.max(predictions) * 100

        return jsonify({'prediction': predicted_class, 'confidence': confidence})
    except Exception as e:
        print(f"Prediction error: {str(e)}")  # แสดงข้อความแสดงข้อผิดพลาดใน console
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # รันเซิร์ฟเวอร์ Flask บนพอร์ต 5000
