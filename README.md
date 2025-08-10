# 📊 AI PPTX Generator

An AI-powered PowerPoint presentation generator built with **Streamlit**, **Groq API**, **Pexels API**, and **python-pptx**.  
This tool creates a well-structured PPT with:
- **Intro slide** (title & intro text)
- **Content slides** (heading + 4 bullet points + image on the right)
- **Conclusion slide** (final summary or thank-you note)

---

## 🚀 Features
- 🧠 **Groq LLM** for fast & free text generation (LLaMA 3, Mixtral models)
- 🖼 **Pexels API** for high-quality images
- 📑 **Perfect slide alignment** — no overlapping text & images
- 🎨 **ChatGPT-style Streamlit interface**
- 📥 Download-ready `.pptx` file

---

## 📂 Project Structure
    pptx_generator/
    │── app.py # Streamlit app entry point
    │── ppt_creator.py # PPT creation & formatting functions
    │── pexels_api.py # Fetch images from Pexels
    │── llm_content.py # Groq API for content generation
    │── requirements.txt # Project dependencies
    │── .env # API keys


---

## 🔑 Requirements
- Python 3.8+
- Groq API key (https://console.groq.com/)
- Pexels API key (https://www.pexels.com/api/)

---

## 📦 Installation
1. **Clone the repository**
     ```bash
    git clone https://github.com/yourusername/ai-pptx-generator.git
    cd ai-pptx-generator
2. **Create and activate a virtual environment**
      ```bash
      python -m venv .venv
      source .venv/bin/activate   # Linux/Mac
      .venv\Scripts\activate      # Windows
3. **Install dependencies**
     ```bash
     pip install -r requirements.txt
4. **Set up environment variables in .env**
    ```bash
    GROQ_API_KEY=your_groq_api_key
    PEXELS_API_KEY=your_pexels_api_key
