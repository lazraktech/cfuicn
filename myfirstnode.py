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
        """
        Generate text using the Ollama API.
        """
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
            
            # Ollama streams responses, so we need to accumulate the full response
            full_response = ""
            for line in response.iter_lines():
                if line:
                    data = response.json()
                    full_response += data.get("response", "")
                    
                    # Break if we're done
                    if data.get("done", False):
                        break
                        
            return (full_response,)
            
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {str(e)}")
            return ("Error: Failed to communicate with Ollama server. Is it running?",)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "My First Node": MyNode,
    "Ollama Node": OllamaNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FirstNode": "My First Node",
    "Ollama Node": "Ollama Node"
}
