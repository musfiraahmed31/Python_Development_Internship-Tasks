import gradio as gr

def evaluate_password(password):
    score = 0
    suggestions = []

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{},.<>?/\\|" for c in password)
    length_ok = len(password) >= 8

    if length_ok:
        score += 1
    else:
        suggestions.append("🔸 Use at least 8 characters.")

    if has_upper:
        score += 1
    else:
        suggestions.append("🔸 Add uppercase letters (A–Z).")

    if has_lower:
        score += 1
    else:
        suggestions.append("🔸 Add lowercase letters (a–z).")

    if has_digit:
        score += 1
    else:
        suggestions.append("🔸 Add digits (0–9).")

    if has_special:
        score += 1
    else:
        suggestions.append("🔸 Add special characters (!@# etc.).")

    percent = int((score / 5) * 100)

    if score == 5:
        verdict = "💪 Strong Password"
        color = "#28a745"
    elif score >= 3:
        verdict = "😐 Medium Password"
        color = "#ffc107"
    else:
        verdict = "⚠️ Weak Password"
        color = "#dc3545"

    result_html = f"""
    <div class='verdict-box' style='background-color:{color};'>
        {verdict}
    </div>
    """

    rules = (
        "- 1 point: Length ≥ 8\n"
        "- 1 point: Uppercase letter (A–Z)\n"
        "- 1 point: Lowercase letter (a–z)\n"
        "- 1 point: Digit (0–9)\n"
        "- 1 point: Special character (!@# etc.)"
    )

    examples = (
        "- Secur3!Login2024\n"
        "- Myp@ssword$Safe\n"
        "- Zx7!aB9@Lm#"
    )

    return percent, gr.HTML(result_html), "\n".join(suggestions), rules, examples

def clear_all():
    return "", 0, gr.HTML(""), "", "", ""

with gr.Blocks(css="""
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f4f6f8;
}
h1, h2, h3 {
    text-align: center;
    color: #2c3e50;
}
.gr-textbox textarea {
    font-size: 16px !important;
    padding: 10px !important;
}
.gr-button {
    padding: 10px 18px !important;
    font-size: 16px !important;
    border-radius: 8px !important;
    background-color: #3498db;
    color: white;
    border: none;
}
.gr-button:hover {
    background-color: #2980b9;
}
.verdict-box {
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 14px;
    text-align: center;
    border-radius: 10px;
    margin-top: 12px;
}
""") as app:

    gr.Markdown("## 🔐 Password Strength Checker")
    gr.Markdown("Enter your password below to get a full strength check, improvement tips, and example strong passwords.")

    with gr.Group():
        password_input = gr.Textbox(
            label="🔑 Enter Your Password",
            type="text",  # 👈 password is visible
            placeholder="e.g., MySecureP@ss123"
        )

        with gr.Row():
            check_btn = gr.Button("✅ Check Password")
            clear_btn = gr.Button("❌ Clear")

    strength_slider = gr.Slider(0, 100, label="Password Strength (%)", interactive=False)
    result_box = gr.HTML()
    suggestions_box = gr.Textbox(label="🔧 Suggestions to Improve", lines=4, interactive=False)
    rules_box = gr.Textbox(label="📋 Scoring Rules", lines=5, interactive=False)
    examples_box = gr.Textbox(label="💡 Example Strong Passwords", lines=3, interactive=False)

    check_btn.click(
        fn=evaluate_password,
        inputs=password_input,
        outputs=[strength_slider, result_box, suggestions_box, rules_box, examples_box]
    )

    clear_btn.click(
        fn=clear_all,
        inputs=None,
        outputs=[password_input, strength_slider, result_box, suggestions_box, rules_box, examples_box]
    )

app.launch()
