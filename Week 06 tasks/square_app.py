import gradio as gr

# Function to calculate square
def CalculateSquare(Number):
    return f"{Number}² = {Number ** 2}"

# Gradio app setup
app = gr.Interface(
    fn=CalculateSquare,
    inputs=gr.Number(label="Enter a Number"),
    outputs=gr.Textbox(label="Squared Result"),
    title="🔢 Square Numbers App",
    description="This app takes a number and returns its square using Gradio."
)

# Launch the app
app.launch()
