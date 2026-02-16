# 📄 Report Card Generating System

A simple and user-friendly **Report Card Generating System** built using **Python Flask**, HTML, CSS, and JavaScript.  
This project helps generate student report cards by entering marks and student details, and then saving the report data in JSON format.

---

## 🚀 Features

- ✅ Fetch student details using **Roll Number**
- ✅ Supports classes:
  - F.Y.B.Sc
  - S.Y.B.Sc
  - T.Y.B.Sc
- ✅ Generates report card quickly
- ✅ Saves generated report cards in **JSON format**
- ✅ Simple and clean UI
- ✅ Flask API based backend

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-Cors**
- **HTML**
- **CSS**
- **JavaScript**
- **JSON** (for storing report card data)

---

## 📂 Project Structure

Report_Card_Generation_Sys/
│── app.py
│── requirements.txt
│── templates/
│ └── index.html
│── static/
│ ├── style.css
│ └── script.js
│── data/
│ └── students.json
│── reports/
│ └── report_<roll>.json

- `app.py` → Main backend Flask file  
- `templates/` → HTML files  
- `static/` → CSS and JavaScript files  
- `data/` → Student details JSON file  
- `reports/` → Generated report card files

- ## ⚙️ Installation & Run

### 1️⃣ Clone the Repository
bash
git clone <your-repository-link>
cd Report_Card_Generation_Sys

2️⃣ Install Requirements :--
pip install -r requirements.txt

3️⃣ Run the Flask App :--
python app.py

4️⃣ Open in Browser :--
http://127.0.0.1:5000/
  
