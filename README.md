## 🎨 Urine Color Classification API

<div align="center">
https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

AI-powered urine color analysis for health insights

</div>

## 📋 Overview
A intelligent FastAPI application that classifies urine color from images using deep learning. This system provides instant analysis and health recommendations based on urine color characteristics.

## ✨ Features
# -🖼️ Image Upload - REST API for easy image submission
# -🧠 AI Classification - Deep learning model with TensorFlow
# -🎯 8 Color Categories - Comprehensive urine color analysis
# -💡 Health Insights - Medical information for each color
# -🧹 Auto Cleanup - Automatic file management
# -📊 Confidence Scoring - Probability-based predictions

## 🎨 Supported Color Classes


| Color | Indonesian | English |
|------------|---------|---------|
| 🟦 | Biru | Blue |
| 🟫 | Coklat | Brown |
| 🟩 | Hijau | Green |
| ⬛ | Hitam | Black |
| 🟧 | Jingga | Orange |
| 🟨 | Kuning | Yellow |
| 🟥 | Merah | Red |
| ⬜ | Putih | White |

## 🚀 Quick Start

**Prerequisites**
- Python 3.8+
- pip package manager

**Installation**
1. Clone the repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate    # Windows
```

3. Install dependencies
```bash
pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 tensorflow==2.20.0 numpy==1.26.4 pillow==10.3.0 python-multipart==0.0.9
```

4. Download Model File 📥
Important: The model file is available on Google Drive:

🔗 Download model.h5 from Google Drive

Place the downloaded model.h5 file in the model/ directory.