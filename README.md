🌿 EcoWise – Sustainable Living Companion
EcoWise is a modern web application designed to help users reduce their carbon footprint and make more sustainable lifestyle choices. It combines a beautifully designed frontend with an intelligent backend assistant powered by a local AI model using CrewAI.

🌟 Features

📊 Carbon Footprint Calculator
Allows users to estimate their yearly carbon emissions based on energy use, transport, diet, and air travel.

🧠 AI Eco Assistant
Chatbot powered by Ollama's LLaMA3 model using CrewAI to offer real-time sustainability advice.

📰 Live News Panel
Auto-scrolling environmental news ticker showcasing the latest in green initiatives.

🏆 Leaderboard & History Tracking
Visual comparison with other users and personal carbon footprint history over time.

📁 Project Structure

├── index.html       # Main web page with login, calculator, and chat assistant
├── styles.css       # Modern, responsive, eco-themed styling
├── main.py          # Flask backend using CrewAI for the eco assistant
🧠 AI Assistant Setup (Backend)
Powered by CrewAI using a local LLM via Ollama.

Make sure to run Ollama locally with the specified model (e.g., llama3.2:1b) before starting the Flask server.

# In one terminal
ollama run llama3.2:1b

# In another terminal (project root)
python main.py
🛠️ How to Run Locally
Clone this repository:

git clone https://github.com/yourusername/ecowise.git
cd ecowise
Ensure you have Python and Flask installed:

pip install flask flask-cors
Start the backend server:

python main.py
Open index.html in your browser.

📸 Screenshots
Add screenshots here if you want to showcase your UI.

✨ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

AI/LLM: CrewAI + Ollama (LLaMA3.2)

Styling: Responsive layout with eco-themed color palette

