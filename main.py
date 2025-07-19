"""
Backend module: defines FastAPI endpoints for handling client GET and POST requests for Conversational AI agent
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime
import groq_client
import uuid

# Storage for messages(to remember conversation history)
chat_history: Dict[str, List[Dict[str, str]]] = {}

MAX_CONVERSATION_LENGTH = 15 # Maximum number of messages to store in chat history
MAX_CONVERSATION_HISTORY = 10 # Maximum number of conversations to store in chat history

# App initalization
app = FastAPI()

# Request and Response Models
class UserMessage(BaseModel):
    session_id: Optional[str] = None
    message: str
    timestamp: datetime

class BotResponse(BaseModel):
    session_id: str
    response: str
    timestamp: str

class NewChatRequest(BaseModel):
    initial_message: str

class NewChatResponse(BaseModel):
    session_id: str
    response: str
    timestamp: str

class ChatHistoryResponse(BaseModel):
    sessions: Dict[str, List[Dict[str, Any]]]
    
# Generate a unique session ID for each conversation
def generate_session_id() -> str:
    """
    Returns:
        str: A unique session ID.
    """
    return str(uuid.uuid4())

# Method to retrive chat history for a session
def get_chat_history(session_id: str) -> List[Dict[str, str]]:
    """
    Retrieve chat history for a given session ID.
    
    Args:
        session_id (str): The unique session ID.
    
    Returns:
        List[Dict[str, str]]: A list of messages in the chat history.
    """
    return chat_history.get(session_id, [])

# Method to add a message to the chat history
def add_message_to_history(session_id: str, message: Dict[str, str]) -> None:
    """
    Add a message to the chat history for a given session ID.
    """
    if session_id not in chat_history:
        chat_history[session_id] = []
    
    # Add new message to the history
    chat_history[session_id].append(message)
    
    # Ensure we do not exceed the maximum conversation length
    if len(chat_history[session_id]) > MAX_CONVERSATION_LENGTH:
        chat_history[session_id] = chat_history[session_id][-MAX_CONVERSATION_LENGTH:]
    
    # Ensure we do not exceed the maximum number of conversations
    if len(chat_history) > MAX_CONVERSATION_HISTORY:
        oldest_session = min(chat_history.keys(), key=lambda k: chat_history[k][0]['timestamp'])
        del chat_history[oldest_session]

#  Method to check if session exists
def session_exists(session_id: str) -> bool:
    """
    Check if a session ID exists in chat history.
    """
    return session_id in chat_history

# Health check endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Endpoint to start a new chat session
@app.post("/new_chat", response_model=NewChatResponse)
async def new_chat(request: NewChatRequest):
    """
    Start a new chat session with an initial message.
    """
    try:
        # Generate new session ID
        session_id = generate_session_id()
        
        # Add user's initial message to history
        user_message = {
            "role": "user",
            "content": request.initial_message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        add_message_to_history(session_id, user_message)
        
        # Get AI response using context (even though it's first message)
        history = get_chat_history(session_id)
        ai_response = groq_client.generate_response_with_context(history)
        
        # Add AI response to history
        bot_message = {
            "role": "assistant",
            "content": ai_response['response'],
            "timestamp": ai_response['timestamp']
        }
        add_message_to_history(session_id, bot_message)
        
        return NewChatResponse(
            session_id=session_id,
            response=ai_response['response'],
            timestamp=ai_response['timestamp']
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create new chat: {str(e)}")

# Endpoint to send a message to the AI agent
@app.post("/send_message", response_model=BotResponse)
async def send_message(user_message: UserMessage):
    """
    Endpoint to send a message to the AI agent and receive a response.
    """
    try: 
        session_id = user_message.session_id
        if not session_id or not session_exists(session_id):
            session_id = generate_session_id()
    
        # Add user message to chat history
        add_message_to_history(session_id, {
            "role": "user",
            "content": user_message.message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
    
        # Generate response using Groq client
        history = get_chat_history(session_id)
        response = groq_client.generate_response_with_context(history)
        
        # Add bot response to chat history
        add_message_to_history(session_id, {
            "role": "assistant",
            "content": response['response'],
            "timestamp": response['timestamp']
        })
        
        return BotResponse(
            session_id=session_id,
            response=response['response'],
            timestamp=response['timestamp']
        )
    
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Endpoint to get chat history for all sessions
@app.get("/chat_history", response_model=ChatHistoryResponse)
async def get_all_chat_history():
    """
    Retrieve chat history for all sessions.
    """
    try:
        return ChatHistoryResponse(
            sessions=chat_history,
            total_sessions=len(chat_history)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve chat history: {str(e)}")

# Endpoint to get chat history for a specific session
@app.get("/chat_history/{session_id}")
async def get_session_history(session_id: str):
    """
    Retrieve chat history for a specific session.
    """
    try:
        if not session_exists(session_id):
            raise HTTPException(status_code=404, detail="Session not found")
        
        return {
            "session_id": session_id,
            "messages": get_chat_history(session_id),
            "message_count": len(get_chat_history(session_id))
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve session history: {str(e)}")
