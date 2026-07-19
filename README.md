# 🤖 AI Code Review Assistant

AI Code Review Assistant is a Flask-based web application that uses the **Groq API** and **Llama 3.3 70B Versatile** model to analyze Python source code. It provides intelligent code reviews by identifying bugs, security vulnerabilities, performance improvements, and coding best practices through a simple and user-friendly interface.

---

## 🚀 Features

- 🤖 AI-Powered Code Review
- 📂 Upload Python (.py) Files
- 🐞 Detect Bugs & Logical Errors
- 🔒 Security Analysis
- ⚡ Performance Improvement Suggestions
- ✅ Best Coding Practices
- 📋 Copy Review to Clipboard
- 📄 Download / Print Review Report
- 🌐 Responsive Web Interface
- ☁️ Deployed on PythonAnywhere

---

## 🏗️ Project Structure

```
AI-Code-Review-Assistant/
│── app.py                 # Main Flask application
│── review.py              # AI review logic using Groq API
│── requirements.txt       # Project dependencies
│── .env                   # Environment variables (API Key)
│── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── uploads/               # Uploaded Python files
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anksindagi19-collab/AI-Code-Review-Assistant.git
cd AI-Code-Review-Assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a file named **.env** in the project directory.

```env
GROQ_API_KEY=your_groq_api_key
```

### 5️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. Upload a Python (.py) source code file.
2. The application reads the uploaded code.
3. The code is sent to the Groq API.
4. The Llama 3.3 70B Versatile model analyzes the code.
5. The AI generates a detailed review including:
   - Bugs & Logical Errors
   - Security Issues
   - Performance Improvements
   - Coding Best Practices
6. The review is displayed on the results page.
7. Users can copy or print the generated review.

---

## 📊 AI Review Includes

The application automatically analyzes:

- ✅ Bugs & Logical Errors
- ✅ Security Vulnerabilities
- ✅ Performance Optimization Suggestions
- ✅ Best Coding Practices

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Groq API
- Llama 3.3 70B Versatile
- Git
- GitHub
- PythonAnywhere

---

## 🌐 Live Demo

**Live Website**

👉 https://ankitasindagi.pythonanywhere.com

---

## 💻 GitHub Repository

👉 https://github.com/anksindagi19-collab/AI-Code-Review-Assistant

---

## 🔮 Future Improvements

- 🌍 Support Multiple Programming Languages (C, C++, Java, JavaScript)
- 📊 AI Code Quality Score
- 🎨 Syntax Highlighting
- 📄 Download Review as PDF
- 🔐 User Authentication
- 📂 Review History
- 🌙 Dark / Light Mode
- 📦 ZIP Project Upload
- 🔗 GitHub Repository Code Review


## 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Developed By

**Ankita Sindagi**

Electronics & Communication Engineering (ECE)

**GitHub:** https://github.com/anksindagi19-collab

