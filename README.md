## 🎨 Urine Color Classification API
<div align="center">

![Flask](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![TENSORFLOW](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**AI-powered urine color analysis for health insights**

</div>

## 📋 Overview

A intelligent FastAPI application that classifies urine color from
images using deep learning. This system provides instant analysis and
health recommendations based on urine color characteristics.

## ✨ Features

-   🖼️ **Image Upload** - REST API for easy image submission\
-   🧠 **AI Classification** - Deep learning model with TensorFlow\
-   🎯 **8 Color Categories** - Comprehensive urine color analysis\
-   💡 **Health Insights** - Medical information for each color\
-   🧹 **Auto Cleanup** - Automatic file management\
-   📊 **Confidence Scoring** - Probability-based predictions

## 🎨 Supported Color Classes

  Color   Indonesian   English
  ------- ------------ ---------
  🟦      Biru         Blue
  🟫      Coklat       Brown
  🟩      Hijau        Green
  ⬛      Hitam        Black
  🟧      Jingga       Orange
  🟨      Kuning       Yellow
  🟥      Merah        Red
  ⬜      Putih        White

## 🚀 Quick Start

### Prerequisites

-   Python 3.8+
-   pip package manager

### Installation

1.  Clone the repository

``` bash
git clone <your-repository-url>
cd <project-directory>
```

2.  Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scriptsctivate    # Windows
```

3.  Install dependencies

``` bash
pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 tensorflow==2.20.0 numpy==1.26.4 pillow==10.3.0 python-multipart==0.0.9
```

4.  Download Model File 📥\
    Important: The model file is available on Google Drive:

[🔗 Download model.h5 from Google
Drive](https://drive.google.com/drive/folders/1Z9SzeX64ijgbtLytaR5hjHju3UupzI9L?usp=drive_link)

Place the downloaded `model.h5` file in the `model/` directory.

## 📂 Project Structure

``` text
├── main.py                 # Main application file
├── requirements.txt        # Dependencies list
├── model/
│   └── model.h5           # AI model (download from Google Drive)
├── images/                # Auto-created upload directory
└── README.md              # This file
```

## 🏃‍♂️ Running the Application

### Development Mode

``` bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

``` bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
```

### Direct Execution

``` bash
python main.py
```

## 📡 API Endpoints

### 🔍 Root Endpoint

``` bash
GET /
```

Returns welcome message

### 📤 Upload & Analyze Image

``` bash
POST /upload
```

-   Content-Type: `multipart/form-data`\
-   Body: Image file

### 📥 Get Results

``` bash
GET /predict
```

Retrieves latest prediction results

## 🛠️ Usage Examples

### Using cURL

``` bash
curl -X POST "http://localhost:8000/upload"   -F "file=@path/to/urine_image.jpg"
```

### Using Python

``` python
import requests

response = requests.post(
    "http://localhost:8000/upload",
    files={"file": open("urine_image.jpg", "rb")}
)
print(response.json())
```

### Using Web Interface

Access interactive documentation at:\
- Swagger UI: http://localhost:8000/docs\
- ReDoc: http://localhost:8000/redoc

## 📋 Example Response

``` json
{
  "filename": "a1b2c3d4-e5f6-7890-abcd-ef1234567890.jpg",
  "prediction": {
    "model-prediction": "Kuning",
    "model-prediction-confidence-score": 95.5,
    "filename": "images/a1b2c3d4-e5f6-7890-abcd-ef1234567890.jpg"
  },
  "response_message": "Warna kuning pada urine biasanya normal dan disebabkan oleh pigmen urine yang disebut urobilin. Namun, warna kuning yang sangat gelap atau kuning kecoklatan bisa menunjukkan dehidrasi. Pastikan untuk cukup minum air."
}
```

## 🩺 Health Insights

The application provides specific health information for each urine
color:\
- 🔵 **Blue**: Possible food dyes or kidney concerns\
- 🟤 **Brown**: Dehydration or potential liver issues\
- 🟢 **Green**: Usually dietary, possible infections\
- ⚫ **Black**: Oxidized blood or liver problems\
- 🟠 **Orange**: Dehydration or vitamin effects\
- 🟡 **Yellow**: Normal to dehydrated range\
- 🔴 **Red**: Possible blood - seek medical attention\
- ⚪ **White**: Healthy hydration levels

## ⚠️ Important Notes

1.  📦 Model Requirement: Remember to download model.h5 from Google
    Drive\
2.  🏥 Medical Disclaimer: This tool is for educational purposes only\
3.  🖼️ Image Quality: Use clear, well-lit images for best results\
4.  🔒 Privacy: Images are automatically deleted after processing

## 🐛 Troubleshooting

  Issue               Solution
  ------------------- ---------------------------------------
  Model not found     Download model.h5 from Google Drive
  Import errors       Check all dependencies are installed
  Port in use         Change port (`--port 8001`)
  Permission denied   Check write permissions for `images/`

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests or
open issues for bugs and feature requests.

## 📞 Support

For technical support or questions about this application, please
contact me.

{align="center"}
✨ Don't forget to download the model file from Google Drive before
running! ✨

[📥 Download Model
Here](https://drive.google.com/drive/folders/1Z9SzeX64ijgbtLytaR5hjHju3UupzI9L?usp=drive_link)

