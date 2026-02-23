# 🐾 AI Pet Name Generator

An interactive AI-powered web application that generates personalized pet names based on user-defined characteristics such as pet type, color, personality, and naming style.

Built using **Streamlit**, **LangChain**, and the **OpenAI API**, this project demonstrates real-time LLM integration within a user-facing application.

---

# 🚀 Features

- 🎯 Personalized name generation based on structured inputs  
- 🧠 Personality-driven naming using custom adjectives  
- 🎚 Adjustable output count (5–20 names)  
- ⚡ Real-time AI generation  
- 💾 Stateful interface that preserves results across interactions  
- 🎨 Clean, responsive Streamlit UI  

---

# 🧠 How It Works

The application follows a simple pipeline:

1. User inputs pet characteristics through the Streamlit interface  
2. Inputs are injected into a LangChain prompt template  
3. The prompt is sent to the OpenAI model (`gpt-4o-mini`)  
4. The model generates formatted name suggestions  
5. Results are displayed instantly in the UI  

---

# 🖥️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- OpenAI API  
- python-dotenv  

---

# 📂 Project Structure
