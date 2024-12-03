# ComfyUI Custom Nodes Collection

A collection of custom nodes for ComfyUI, focusing on AI model integration and workflow enhancement. This project serves as my first major Python AI programming project, leveraging ComfyUI's existing framework.

## ✅ Completed Features

- Ollama Server Integration: Successfully implemented local Ollama server interaction

### Ollama Integration Setup & Usage

#### Prerequisites
1. Install Ollama on your system ([Ollama Installation Guide](https://github.com/ollama/ollama))
2. Start the Ollama server locally
3. Pull your desired model (e.g., `ollama pull llama2`)

#### Node Configuration
The Ollama node accepts the following inputs:
- **Prompt**: Text input for the model
- **Model Name**: Name of the Ollama model to use (default: "llama2")
- **System Prompt** (optional): Context or instructions for the model
- **Temperature**: Controls randomness (0.0 - 1.0, default: 0.7)

#### Example Usage
1. Add the Ollama node to your ComfyUI workflow
2. Connect a text input node to the "Prompt" input
3. Configure model settings
4. Execute the workflow to get AI-generated responses

#### API Reference

## 🚀 Planned Nodes

### 1. Data Preprocessing Node
- Handles data normalization
- Implements data augmentation
- Provides filtering capabilities
- Prepares data for training/inference

### 2. Model Evaluation Node
- Calculates key metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Processes model predictions against ground truth

### 3. Visualization Node
- Generates visual analytics:
  - Custom plots
  - Heatmaps
  - Confusion matrices
- Aids in model performance analysis

### 4. Hyperparameter Tuning Node
- Automates hyperparameter optimization
- Identifies optimal model configurations
- Streamlines model tuning process

### 5. Custom Loss Function Node
- Enables custom loss function implementation
- Supports specialized training tasks
- Extends beyond standard loss functions

### 6. Data Splitting Node
- Manages dataset partitioning:
  - Training set
  - Validation set
  - Test set
- Ensures reproducible splits

### 7. Batch Processing Node
- Handles large dataset processing
- Features:
  - Efficient data loading
  - Batch management
  - Data shuffling

## 🛠️ Installation

1. Make sure you have ComfyUI installed and running
2. Clone this repository into your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone [your-repo-url] comfyui-ollama
   ```
3. Install the required dependencies:
   ```bash
   pip install -r comfyui-ollama/requirements.txt
   ```
4. Restart ComfyUI

### Dependencies
- Python 3.8+
- requests>=2.31.0
- Ollama server running locally

### Troubleshooting
- Ensure Ollama server is running (`ollama serve`)
- Check if Ollama is accessible at `http://localhost:11434`
- Verify you have pulled your desired model (e.g., `ollama pull llama2`)
- Check ComfyUI console for any error messages

## 📖 Usage

### Basic Usage
1. Start ComfyUI and locate "Ollama Text Generation" in the node menu under "AI/LLM" category
2. Add the node to your workflow
3. Configure the following parameters:
   - **Prompt**: Your input text
   - **Model**: The Ollama model to use (default: llama2)
   - **Temperature**: Controls response randomness (0.0-1.0)
   - **System Prompt** (optional): Context or instructions for the model

### Example Workflow
1. Create a new workflow in ComfyUI
2. Add a "Text" node for your prompt
3. Connect it to the Ollama node's "prompt" input
4. Add an output node to display the generated text
5. Execute the workflow

### Tips
- Lower temperature (0.1-0.3) for more focused, deterministic responses
- Higher temperature (0.7-1.0) for more creative, varied outputs
- Use system prompts to set context or control response style
- Models must be pre-downloaded using Ollama CLI before use

## 🤝 Contributing

[Contribution guidelines to be added]

## 📄 License

[License information to be added] 