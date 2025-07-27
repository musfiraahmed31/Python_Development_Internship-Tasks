import gradio as gr

def ReverseSentence(Sentence):
    return Sentence[::-1]

app = gr.Interface(
    fn=ReverseSentence,
    inputs=gr.Textbox(lines=2, label="Enter a Sentence"),
    outputs=gr.Textbox(label="Reversed Sentence"),
    title="🔁 Sentence Reverser",
    description="Enter a sentence and get the reversed output."
)

app.launch()
