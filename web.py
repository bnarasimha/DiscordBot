import gradio as gr
import rag
import logger

def getAnswer(query):
    if query:
        return rag.getResponse(query)

def logUserFeedback_CorrectAnswer(input, output, feedback):
    logger.logUserFeedback(input, "Correct Answer")

def logUserFeedback_NeedsImprovement(input, output, feedback):
    logger.logUserFeedback(input, "Needs Improvement")

def logUserFeedback_IncorrectAnswer(input, output, feedback):
    logger.logUserFeedback(input, "Incorrect Answer")


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
            # with gr.Row():
            #     correct_btn = gr.Button(value="Correct Answer")
            #     needs_improvement_btn = gr.Button(value="Needs Improvement")
            #     incorrect_answer_btn = gr.Button(value="Incorrect Answer")    
            
    submit_btn.click(getAnswer, inputs=[inp], outputs=[out], api_name=False)
    # correct_btn.click(logUserFeedback_CorrectAnswer, inputs=[inp], outputs=[out])
    # needs_improvement_btn.click(logUserFeedback_NeedsImprovement, inputs=[inp], outputs=[out])
    # incorrect_answer_btn.click(logUserFeedback_IncorrectAnswer, inputs=[inp], outputs=[out])
    
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
