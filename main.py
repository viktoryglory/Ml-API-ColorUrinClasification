from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
import uuid
import os
import uvicorn

IMAGEDIR = "images/"

model = tf.keras.models.load_model('model/model.h5')

class_labels = [
    'Biru', 
    'Coklat', 
    'Hijau', 
    'Hitam', 
    'Jingga', 
    'Kuning', 
    'Merah', 
    'Putih'
]

app = FastAPI()

# Variable global untuk menyimpan hasil prediksi dari model
prediction_result = None

@app.get('/')
def main():
    return {'message': 'Welcome to Capstone CH2-PS036'}

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    global prediction_result

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    # Save file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    # Lakukan prediksi
    img = image.load_img(f"{IMAGEDIR}{file.filename}", target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    pred = model.predict(img_array)
    class_index = np.argmax(pred)
    class_prediction = class_labels[class_index]
    confidence_score = pred[0][class_index] * 100

    # Simpan hasil prediksi untuk digunakan pada rute /predict
    prediction_result = {
        "model-prediction": class_prediction,
        "model-prediction-confidence-score": confidence_score,
        "filename": f"{IMAGEDIR}{file.filename}"
    }

    # Tambahkan respon sesuai dengan model-prediction
    response_message = get_response_message(class_prediction)

    return {"filename": file.filename, "prediction": prediction_result, "response_message": response_message}

def get_response_message(prediction):
    if prediction == 'Biru':
        return "Warna biru pada urine tidak umum dan mungkin merupakan hasil dari konsumsi pewarna makanan tertentu. Namun, jika warna biru terus menerus muncul, itu bisa menunjukkan masalah dengan ginjal atau saluran kemih. Disarankan untuk berkonsultasi dengan profesional kesehatan."
    elif prediction == 'Coklat':
        return "Warna coklat pada urine bisa disebabkan oleh dehidrasi, konsumsi makanan tertentu, atau masalah dengan hati. Tetapi, coklat juga dapat menjadi tanda adanya darah dalam urine, yang memerlukan perhatian medis segera."
    elif prediction == 'Hijau':
        return "Warna hijau pada urine biasanya disebabkan oleh konsumsi makanan atau suplemen tertentu. Namun, jika hijau terus muncul dan tidak dapat dijelaskan oleh faktor diet, itu bisa mengindikasikan masalah kesehatan seperti infeksi atau penyakit hati. Konsultasikan dengan dokter untuk evaluasi lebih lanjut."
    elif prediction == 'Hitam':
        return "Urine hitam dapat menjadi tanda adanya darah teroksidasi atau masalah hati. Beberapa jenis makanan dan obat-obatan juga dapat menyebabkan urine hitam. Jika urine hitam terus muncul, segera hubungi profesional kesehatan."
    elif prediction == 'Jingga':
        return "Warna jingga pada urine mungkin disebabkan oleh dehidrasi atau konsumsi vitamin B kompleks. Namun, jika jingga terus muncul tanpa alasan yang jelas, itu bisa menunjukkan masalah dengan hati atau saluran empedu. Periksakan ke dokter untuk evaluasi lebih lanjut."
    elif prediction == 'Kuning':
        return "Warna kuning pada urine biasanya normal dan disebabkan oleh pigmen urine yang disebut urobilin. Namun, warna kuning yang sangat gelap atau kuning kecoklatan bisa menunjukkan dehidrasi. Pastikan untuk cukup minum air."
    elif prediction == 'Merah':
        return "Urine merah dapat disebabkan oleh keberadaan darah. Ini bisa disebabkan oleh infeksi saluran kemih, batu ginjal, atau masalah lain pada ginjal atau kandung kemih. Segera cari bantuan medis jika urine berwarna merah."
    elif prediction == 'Putih':
        return "Urine yang putih atau bening (transparan) umumnya dianggap normal dan sehat. Ini menunjukkan bahwa Anda mungkin sedang minum cukup air, dan ginjal Anda berfungsi dengan baik untuk menyaring kelebihan air dalam tubuh. Peningkatan konsumsi air dapat menghasilkan urine yang lebih transparan."
    else:
        return "Warna urine tidak dikenali."

@app.get('/predict')
def prediction():
    global prediction_result

    # Cek apakah sudah ada hasil prediksi
    if prediction_result is None:
        return {"error": "No prediction result available. Please use the /upload endpoint first."}

    # Hapus file gambar setelah digunakan pada prediksi
    if os.path.isfile(prediction_result["filename"]):
        os.remove(prediction_result["filename"])

    return prediction_result

if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='localhost')
