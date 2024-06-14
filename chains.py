from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

from retreiver import retriever, format_docs

llm = "mistral"
model = Ollama(model=llm)

paperspace_category_prompt = PromptTemplate.from_template(
        """
        You are a question answer service bot. Your task is to assess user intent and categorize inquiry after <<<>>> into one of the following predefined categories:
        Paperspace
        Generic-AI/ML
        Other

        <<<
        {question}
        >>>

        If the text doesn't fit into any of the above categories, classify it as:
        Other

        You will only respond with the category. Do not include the word "Category". Do not provide explanations or notes."""
)
paperspace_category_chain = (
    paperspace_category_prompt | model | StrOutputParser()
)

def getRagChain():
    paperspace_rag_prompt = PromptTemplate.from_template(
        """ Answer the following question based only on the provided context:
            <context>
            {context}
            </context>

            Question: {question}"""
    )

    paperspace_rag_chain = (
        {
            "context": retriever | format_docs, 
            "question": RunnablePassthrough()
        }
        | paperspace_rag_prompt
        | model
        | StrOutputParser()
    )
    return paperspace_rag_chain

def getGenericChain():
    paperspace_generic_prompt = PromptTemplate.from_template(
        """ You are an expert in Artificial Intelligence and Machine learning. \
            Respond to the following question:

            Question: {question}
            Answer:"""
    )

    paperspace_generic_chain = (
        paperspace_generic_prompt | model | StrOutputParser()
    )
    return paperspace_generic_chain

def getOthersChain():
    paperspace_others_prompt = PromptTemplate.from_template(
        """ Respond to the following question:
        
            Question: {question}
            Answer:"""
    )

    paperspace_others_chain = (
        paperspace_others_prompt | model | StrOutputParser()
    )
    return paperspace_others_chain

def route(info):
    if "paperspace" in info["topic"].lower():
        print('Inside Paperspace chain')
        return getRagChain()
    elif "generic-ai/ml" in info["topic"].lower():
        print('Inside Generic chain')
        return getGenericChain()
    else:
        print('Inside others chain')
        return getOthersChain()
    