from flask import Flask, request, jsonify
from crewai import Crew, Agent, Task, LLM
from flask_cors import CORS
import os
# from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# load_dotenv()

# --- Configure Ollama LLM using CrewAI's LLM class ---
ollama_llm = LLM(
    model='ollama/llama3.2:1b', # <<< Replace with your actual model name (e.g., 'ollama/llama3.2:1b')
    base_url='http://localhost:11434' # <<< Your Ollama API base URL
)
# --- End of Ollama LLM configuration ---


# --- Configure Agent to use the Ollama LLM ---
agent = Agent(
    role="Eco Assistant",
    goal="Provide sustainable advice and green solutions",
    backstory="An AI agent that helps people live greener lives.",
    llm=ollama_llm # <<< Pass the configured LLM object here
)
# --- End of Agent configuration ---


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"answer": "Please provide a question."}), 400

    try:
        task = Task(
            description=question,
            expected_output="Give a brief, clear answer.",
            agent=agent # <<< ADD THIS LINE BACK: Explicitly assign the agent to the task
        )

        # Define the crew with the agent and task
        # Ensure the agent and task are in the respective lists
        crew = Crew(
            agents=[agent], # Ensure the agent is in the agents list
            tasks=[task],   # Ensure the task is in the tasks list
            process="sequential" # Explicitly set process to sequential
        )

        result = crew.kickoff() # Correct method to start the crew

        # Convert the CrewOutput object to a string before sending as JSON
        return jsonify({"answer": str(result)}) # Convert the result to a string

    except Exception as e:
        print(f"Error running CrewAI task: {e}")
        error_message = str(e)

        if "api key" in error_message.lower() or "authentication" in error_message.lower() or "permission" in error_message.lower():
             return jsonify({"answer": f"Authentication/Permission Error: Check your API key or access permissions. Details: {e}"}), 500
        elif "model" in error_message.lower() or "ollama" in error_message.lower() or "connection refused" in error_message.lower() or "provider not provided" in error_message.lower():
             return jsonify({"answer": f"Model/Connection Error: Ensure Ollama is running, the model is available, and the URL/configuration is correct. Details: {e}"}), 500
        else:
             return jsonify({"answer": f"An internal error occurred while processing your request. Details: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)