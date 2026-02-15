from flask import Flask, render_template, request, jsonify
from pathlib import Path
import json

app = Flask(__name__)

# Directory to store student reports
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

# ---------------------------
# Student Database (from your code)
# ---------------------------
STUDENT_DATA = {
    "F.Y.B.Sc": [
        {"roll": "101", "name": "Anil Bharat Chaudhari"},
        {"roll": "102", "name": "Bhavana Suresh Jadhav"},
        {"roll": "103", "name": "Chetan Vijay More"},
        {"roll": "104", "name": "Dipti Prakash Solanki"},
        {"roll": "105", "name": "Eknath Ravi Deshmukh"}
    ],
    "S.Y.B.Sc": [
        {"roll": "201", "name": "Rohit Shrikant Agrawal"},
        {"roll": "202", "name": "Priya Anand Sali"}
    ],
    "T.Y.B.Sc": [
        {"roll": "361", "name": "Priyanka Jagdish Patil"},
        {"roll": "443", "name": "Kothari Kriya Hemendra"},
        {"roll": "449", "name": "Sumit Vinod Bhalerao"}
    ]
}

# ---------------------------
# Routes
# ---------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/student/<roll>')
def get_student(roll):
    # Find the student by roll number
    for cls, students in STUDENT_DATA.items():
        for student in students:
            if student["roll"] == roll:
                return jsonify({"class": cls, "name": student["name"], "roll": roll})
    return jsonify({"error": "Student not found"}), 404

@app.route('/api/report', methods=['POST'])
def save_report():
    data = request.get_json()
    if not data or 'roll' not in data:
        return jsonify({"error": "Invalid data"}), 400

    fpath = REPORTS_DIR / f"report_{data['roll']}.json"
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok", "message": f"Report saved for {data['roll']}"})


if __name__ == '__main__':
    app.run(debug=True)
