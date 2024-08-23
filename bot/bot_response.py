import webapp.rag as rag

def handle_response(message) -> str:
    query = message.lower()
    if(query.strip() == ""):
        return ""
    else:
        return rag.getResponse(query)