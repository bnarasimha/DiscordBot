import gradio as gr
import rag as rag

def getAnswer(query):
    if query:
        return rag.getResponse(query)

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Ask anything about GPU Droplets
    """)
    with gr.Row():
        with gr.Column(scale=1):
            inp = gr.Textbox(label="Question", placeholder="What are GPU Droplets?")
            submit_btn = gr.Button(value="Submit")
        with gr.Column(scale=2):
            out = gr.Textbox(label="Answer")
            inp.submit(getAnswer, inp, out)
            
    submit_btn.click(getAnswer, inputs=[inp], outputs=[out], api_name=False)
    
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
