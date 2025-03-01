# 🍽️ Restaurant Name & Menu Generator

🚀 **A Streamlit-powered app that uses Hugging Face models via LangChain to generate restaurant names and menu items based on a selected cuisine.**  

🔗 **Live Demo (Optional)**: _[Add Streamlit link if deployed]_

---

## ✨ **Features**
✅ **AI-Powered Suggestions** – Generates fancy restaurant names and menu items using Hugging Face LLMs  
✅ **Streamlit UI** – Interactive web interface for selecting cuisines and viewing results  
✅ **LangChain Integration** – Uses `LLMChain` for structured LLM interactions  
✅ **Secure API Handling** – API keys are stored in a `.env` file (not exposed in GitHub)  

---

## 🛠️ **Tech Stack**
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [LangChain](https://python.langchain.com/) + [Hugging Face Hub](https://huggingface.co/)
- **Models Used**: `tiiuae/falcon-7b-instruct` (or `mistralai/Mistral-7B-Instruct-v0.1`)
- **Deployment**: [Streamlit Cloud](https://share.streamlit.io/) (optional)

---

## ⚙️ **Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/manavisharma14/restaurant-name-generator.git
cd restaurant-name-generator
