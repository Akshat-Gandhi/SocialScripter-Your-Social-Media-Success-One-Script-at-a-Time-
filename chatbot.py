import uuid
import cohere 
co = cohere.Client("P0FBK4kwQTVtfjDMKrRINrTofQ57QJ5oAVmvtT6f") # Your Cohere API key

def generate_response(message, preamble, conversation_id):
    if conversation_id is None:
        conversation_id = str(uuid.uuid4())  # Generate a new conversation ID if None
    
    stream = co.chat_stream(message=message,
                            model="command-r-plus",
                            preamble=preamble,
                            conversation_id=conversation_id)

    response = ""
    for event in stream:
        if event.event_type == "text-generation":
            response += event.text
        if event.event_type == "stream-end":
            chat_history = event.response.chat_history

    return response
