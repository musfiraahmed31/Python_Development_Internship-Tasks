# 🔐 Password Strength Checker

An interactive web app built with **Gradio** in **Python** that evaluates the strength of user-entered passwords based on length, character diversity, and complexity. It provides real-time feedback, suggestions for improvement, and examples of strong passwords.

## 🔍 Preview

## 🔍 Preview

![App Screenshot](screenshot.png)

---

## 🚀 Live Demo

You can launch this project locally using Python, or host it for free on [Hugging Face Spaces](https://huggingface.co/spaces).

---

## 🛠️ Features

- ✔️ Evaluates password strength on 5 key criteria
- 🎨 Displays strength using color-coded feedback
- 🧠 Provides improvement suggestions
- 📊 Shows scoring rules
- 💡 Includes strong password examples
- 🌐 Web UI styled with custom CSS
- 🔁 "Clear" button to reset inputs

---

## 📷 UI Preview

```
- 1 point: Length ≥ 8  
- 1 point: Uppercase letter (A–Z)  
- 1 point: Lowercase letter (a–z)  
- 1 point: Digit (0–9)  
- 1 point: Special character (!@# etc.)  
```

---

## 🧑‍💻 Technologies Used

| Tool/Library | Purpose                |
|--------------|------------------------|
| Python       | Core logic             |
| Gradio       | Web interface & UI     |
| HTML/CSS     | Result display styling |

---

## 📦 Installation

### 🔧 Requirements
- Python 3.7+
- pip install streamlit


### ⏬ Steps
```bash
# 1. Clone the repository
git clone https://github.com/your-username/PasswordStrengthChecker.git
cd PasswordStrengthChecker

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install gradio

# 4. Run the app
python app.py
```

---

## 🧪 How It Works

The app evaluates a password using:
- Minimum length (8 characters)
- Presence of uppercase, lowercase, digits, and special characters

It then scores the password out of 5, converts it into a percentage, and classifies it as:
- 💪 Strong (Green)
- 😐 Medium (Yellow)
- ⚠️ Weak (Red)

---

## 🌍 Deployment

You can deploy it easily on:
- [Hugging Face Spaces](https://huggingface.co/spaces)
- Replit
- PythonAnywhere
- Your own server

Want help deploying? Message or raise an issue!

---

## 📸 Screenshot

## 🔍 Preview

![Password Strength Checker Screenshot](password_checker_screenshot.png)

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to suggest features or fixes, feel free to:
- Open an issue
- Fork the repo and submit a PR

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Musfira Ahmed**  
_BS Software Engineering, 4th Semester_  
📧 Reach out: ahmedmusfira3@gmail.com 
🌍 Based in Pakistan

---

## ⭐️ Show Your Support

If you find this project helpful, please ⭐️ star the repo and share it with others!
