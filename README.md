 AgentOps — Multi-Agent AI Workflow

A lightweight multi-agent AI workflow built with Python and Google Gemini.

AgentOps demonstrates how multiple specialized AI agents can work together through a structured workflow:

Planner → Worker → Verifier

The project focuses on AI agent orchestration, task planning, execution, verification, error handling, and automated testing.



 ✨ Features

* 🧠 Planner Agent — Breaks a user task into practical execution steps.
* ⚙️ Worker Agent — Executes the task using the generated plan.
* 🔍 Verifier Agent — Validates the worker's result.
* 🎯 Orchestrator— Coordinates the complete multi-agent workflow.
* 🤖 Gemini Integration — Uses Google's Gemini API for AI-powered planning and execution.
* 🧪 Automated Testing — Tests individual agents and the complete workflow.
* 🔐 Environment Configuration — Keeps API credentials outside the source code.
* 📊 Task State Tracking — Tracks workflow progress from planning through verification.



 🏗️ Architecture


                         User Task
                             │
                             ▼
                  ┌────────────────────┐
                  │   Planner Agent    │
                  │                    │
                  │ Creates a plan     │
                  └─────────┬──────────┘
                            │
                     Execution Plan
                            │
                            ▼
                  ┌────────────────────┐
                  │    Worker Agent    │
                  │                    │
                  │ Executes the task  │
                  └─────────┬──────────┘
                            │
                       Task Result
                            │
                            ▼
                  ┌────────────────────┐
                  │   Verifier Agent   │
                  │                    │
                  │ Validates result   │
                  └─────────┬──────────┘
                            │
                            ▼
                     Verified Result


 Workflow States


PENDING
   │
   ▼
PLANNING
   │
   ▼
WORKING
   │
   ▼
VERIFYING
   │
   ▼
COMPLETED


If an agent or workflow step fails, the system transitions to:


FAILED




 🔄 How It Works

 1. Planner

The Planner receives the user's task and uses Gemini to generate a structured execution plan.

 2. Worker

The Worker receives the original task and generated plan, then uses Gemini to produce the requested result.

 3. Verifier

The Verifier checks whether the Worker produced a valid result and whether the workflow completed successfully.

 4. Orchestrator

The Orchestrator manages the complete workflow, coordinates the agents, and tracks the task state.


User Task
    ↓
Planner
    ↓
Execution Plan
    ↓
Worker
    ↓
Task Result
    ↓
Verifier
    ↓
Verified Result




 📁 Project Structure


AgentOps/
│
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner.py
│   │   ├── worker.py
│   │   └── verifier.py
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── orchestrator.py
│
├── tests/
│   ├── __init__.py
│   └── test_agents.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt




🛠️ Technology Stack

| Technology          | Purpose                         |
| --------------------| ------------------------------- |
| Python 3.14+        | Application and agent logic     |
| Google Gemini API   | AI planning and task execution  |
| google-genai        | Gemini API integration          |
| pytest              | Automated testing               |
| python-dotenv       | Environment variable management |
| Dataclasses         | Structured application models   |
| REST/API Integratio | Communication with the AI model |



🚀 Getting Started

 Requirements

Before running the project, make sure you have:

* Python 3.14+
* A Google Gemini API key
* Python virtual environment
* Git

1. Clone the Repository


git clone https://github.com/linajawad/AgentOps.git
cd AgentOps


 2. Create a Virtual Environment

On Windows PowerShell:


python -m venv venv
.\venv\Scripts\Activate.ps1


 3. Install Dependencies


pip install -r requirements.txt


4. Configure Environment Variables

Create a .env file in the project root:


GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.6-flash


Never commit your real API key to GitHub.

A .env.example file is included as a safe configuration template.


▶️ Run the Application

With the virtual environment activated:


python -m app.main


The application runs the complete:


Planner → Worker → Verifier


workflow and displays the result in the terminal.



 🧪 Testing

Run the automated test suite:


pytest


 Current Test Result

7 tests passed**

The test suite covers:

* Planner task generation
* Empty task validation
* Worker plan validation
* Gemini worker execution
* Verifier validation
* Verifier error handling
* End-to-end orchestration


7 passed


The tests help verify both individual agent behavior and the complete multi-agent workflow.



🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Multi-agent AI architecture
* Agent orchestration
* Prompt-based task planning
* AI task execution
* Result verification
* Workflow state management
* API integration
* Environment-based configuration
* Automated testing
* Error handling
* Python application structure

Rather than relying on a single AI call, the system separates responsibilities across specialized agents.

This makes the workflow easier to test, verify, debug, and extend.



📌 Project Status

 Current

The core multi-agent workflow is implemented and tested:


Planner
   ↓
Worker
   ↓
Verifier
   ↓
Completed


Future Improvements

Potential future enhancements include:

* Persistent task history
* More advanced verification logic
* Additional specialized agents
* Agent observability
* Workflow dashboards
* Structured execution logs
* Retry and recovery mechanisms
* More extensive integration testing
* Automated evaluation metrics



 👩‍💻 Author

Lina Jawad

AI Automation & Agent-Orchestration Project

Built as a practical project demonstrating how multiple AI agents can collaborate through a controlled, testable workflow.
