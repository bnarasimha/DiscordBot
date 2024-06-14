import gradio as gr
#import rag
import rag_working

def getAnswer(query):
    return rag_working.getResponse(query)

demo = gr.Interface(
    fn=getAnswer,
    inputs=["text"],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch()
