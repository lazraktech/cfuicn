from .ollama_text_gen import OllamaNode
NODE_CLASS_MAPPINGS = {"OllamaNode": OllamaNode}
NODE_DISPLAY_NAME_MAPPINGS = {"OllamaNode": "Ollama Text Generation"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']