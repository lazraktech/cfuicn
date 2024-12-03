import requests
from typing import Dict, Any

class OllamaNode:
    """
    A ComfyUI node that interfaces with a local Ollama server for text generation.
    """
    
    def __init__(self):
        self.api_base = "http://localhost:11434/api"
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "model": ("STRING", {"default": "llama2"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.0, "step": 0.1}),
            },
            "optional": {
                "system_prompt": ("STRING", {"multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "AI/LLM"
    
    def generate(self, prompt: str, model: str, temperature: float, system_prompt: str = "") -> tuple[str]:
        """Generate text using the Ollama API."""
        url = f"{self.api_base}/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
        }
        
        if system_prompt:
            payload["system"] = system_prompt
            
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    data = response.json()
                    full_response += data.get("response", "")
                    if data.get("done", False):
                        break
                        
            return (full_response,)
            
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {str(e)}")
            return ("Error: Failed to communicate with Ollama server. Is it running?",)

def create_expansion_prompt(tags: str) -> str:
    """
    Create a prompt for the Ollama llava-llama3 model to expand upon a list of tags.
    
    Args:
        tags (str): A string of tags separated by commas.
        
    Returns:
        str: A formatted prompt for the model.
    """
    prompt = (
        "Expand upon the following list of tags by providing similar and related words or concepts. "
        "Tags: {tags}. "
        "For each tag, suggest additional words or concepts that are related or similar."
    ).format(tags=tags)
    
    return prompt

NODE_CLASS_MAPPINGS = {
    "Ollama Text Generation": OllamaNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ollama Text Generation": "Ollama Text Generation"
} 