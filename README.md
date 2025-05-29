# Business Idea Generator Agent

A simple OpenAI-powered agent that generates business ideas based on your input.

## 🚀 Quick Start

1. **Set up**:
   ```bash
   git clone https://github.com/pallavi1428/Open-AI-Agents-.git
   cd Open-AI-Agents-
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```

2. **Add your API key**:
   - Edit `app/config.py` and add your OpenAI API key:
   ```python
   self.openai_api_key = "sk-your-key-here"
   ```

3. **Run it**:
   ```bash
   python -m app.main
   ```

## 📂 Project Structure
```
openai-agents-app/
├── app/               # Core application
│   ├── __init__.py
│   ├── main.py        # Entry point
│   ├── config.py      # API configuration
│   └── runner.py      # Execution handler
├── agents/
│   └── business_idea_agent.py  # Brain of the operation
└── requirements.txt   # Dependencies
```

## 💡 Example Usage
When you run the program, it will automatically generate business ideas based on a default prompt. To customize:

1. Edit `app/main.py` and change the prompt:
```python
idea = await runner.generate("your custom prompt here")
```

## ⚠️ Important Notes
- Keep your API key secret
- Requires Python 3.8+
- Internet connection required

