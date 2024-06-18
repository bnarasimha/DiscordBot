import gradio as gr
import rag

def getAnswer(query):
    return rag.getResponse(query)

demo = gr.Interface(
    fn=getAnswer,
    inputs=["text"],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
