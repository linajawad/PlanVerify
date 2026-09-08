 AgentOps

A lightweight multi-agent workflow built with Python and Google Gemini.

AgentOps demonstrates how multiple AI agents can work together through a structured workflow:

Planner → Worker → Verifier

The project is designed to demonstrate agent orchestration, task planning, execution, verification, testing, and Gemini API integration.

  Features

* **Planner Agent** — Breaks a task into practical execution steps.
* **Worker Agent** — Executes the task using the generated plan.
* **Verifier Agent** — Validates the worker's result.
* **Orchestrator** — Coordinates the complete agent workflow.
* **Gemini Integration** — Uses Google's Gemini API for AI-powered planning and execution.
* **Automated Tests** — Includes unit tests for individual agents and the complete workflow.
* **Environment Configuration** — Uses environment variables for API configuration.

 Architecture


                    User Task
                       │
                       ▼
               ┌───────────────┐
               │    Planner    │
               │   Agent       │
               └───────┬───────┘
                       │
                  Execution Plan
                       │
                       ▼
               ┌───────────────┐
               │    Worker     │
               │    Agent      │
               └───────┬───────┘
                       │
                  Task Result
                       │
                       ▼
               ┌───────────────┐
               │   Verifier    │
               │    Agent      │
               └───────┬───────┘
                       │
                       ▼
                Verified Result


 Project Structure


AgentOps/
│
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── planner.py
│   │   ├── verifier.py
│   │   └── worker.py
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── orchestrator.py
│
├── dashboard/
├── data/
│
├── tests/
│   ├── __init__.py
│   └── test_agents.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

 How It Works

 1. Planner

The Planner receives the user's task and uses Gemini to generate a practical execution plan.

 2. Worker

The Worker receives the original task and the generated plan, then uses Gemini to produce the task result.

 3. Verifier

The Verifier checks that the Worker completed successfully and returned a valid result.

 4. Orchestrator

The Orchestrator manages the complete workflow and tracks the task state:


PENDING
   ↓
PLANNING
   ↓
WORKING
   ↓
VERIFYING
   ↓
COMPLETED


If an agent fails, the workflow moves to FAILED.

 Requirements

* Python 3.14+
* Google Gemini API key
* Python virtual environment

  Setup

Clone the repository and enter the project directory:


git clone https://github.com/linajawad/AgentOps.git
cd AgentOps


Create and activate a virtual environment:

 Windows PowerShell


python -m venv venv
.\venv\Scripts\Activate.ps1


Install dependencies:


pip install -r requirements.txt


 Environment Variables

Create a .env file in the project root:


GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.6-flash


Never commit your real API key to GitHub.

The project includes `.env.example` as a safe configuration template.

 Run the Application

With the virtual environment activated:


python -m app.main


The application runs the complete:


Planner → Worker → Verifier


workflow and prints the results to the terminal.

Run Tests

Run the automated test suite with:

pytest


Current test result:


7 passed


The tests cover:

* Planner task generation
* Empty task validation
* Worker plan validation
* Gemini worker execution
* Verifier validation
* Verifier error handling
* End-to-end orchestration

  Technology Stack

* Python
* Google Gemini API
* `google-genai
* pytest
* python-dotenv
* Dataclasses
* REST/API-based AI integration

  Project Status

The core multi-agent workflow is implemented and tested.

Current workflow:

Planner → Worker → Verifier → Completed

The project is intended as a foundation for future improvements such as persistent task history, richer verification logic, observability, dashboards, and additional specialized agents.

 Author

Lina Jawad

Built as a practical AI automation and agent-orchestration project.
