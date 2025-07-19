"""
AI Integration Module: Handles AI response generation using the Groq API.
"""
from datetime import datetime
from groq import Groq
from typing import Dict, List, Any
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not found.")

# Initialize AI agent 
agent = Groq(api_key=api_key)  

def generate_response(prompt: str) -> Dict[str, Any]:
    """
    Generate a response from the AI agent based on a single prompt.
    
    Args:
        prompt (str): The input prompt for the AI agent.
    
    Returns:
        Dict[str, Any]: A dictionary containing the response text and timestamp.
    """
    try:
        # Generate response using Groq API
        response = agent.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        )
        
        # Extract response text
        response_text = response.choices[0].message.content
        
        return {
            "response": response_text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    
    except Exception as e:
        raise RuntimeError(f"Failed to generate response: {str(e)}")

def generate_response_with_context(messages: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generate a response from the AI agent using conversation context.
    
    Args:
        messages (List[Dict[str, str]]): List of conversation messages in format:
            [{"role": "user/assistant", "content": "message content"}]
    
    Returns:
        Dict[str, Any]: A dictionary containing the response text and timestamp.
    """
    
    # Convert our message format to Groq API format
    groq_messages = []
    for msg in messages:
        groq_messages.append({
            "role": msg["role"], 
            "content": msg["content"]
        })
        
    # Generate response using Groq API with full context
    response = agent.chat.completions.create(
        messages=groq_messages,
        model="llama3-8b-8192"
    )
        
    # Extract response text
    response_text = response.choices[0].message.content.replace('\\n', '\n')    
        
    return {
        "response": response_text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
   
