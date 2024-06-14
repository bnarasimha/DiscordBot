from langchain_core.runnables import RunnableLambda
from chains import route, paperspace_category_chain, getRagChain

def getResponse(query):
        
    full_chain = {"topic": paperspace_category_chain, "question": lambda x: x["question"]} | RunnableLambda(
        route
    )
    result = full_chain.invoke({"question":query})
    return result


#print(getResponse("Which are the real world applications of DINO 1.5?"))

# query = "Which are the real world applications of DINO 1.5?"
# ragChain = getRagChain()
# print(ragChain.invoke({"question":query}))
