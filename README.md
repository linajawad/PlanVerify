# PlanVerify — Multi-Agent AI Workflow

A lightweight multi-agent AI workflow built with **Python** and **Google Gemini**.

PlanVerify demonstrates how multiple AI agents can work together to plan, execute, and verify a task through a structured workflow.

## 🚀 What It Does

PlanVerify takes a user task and processes it through three specialized AI agents:

**Planner → Worker → Verifier**

* **Planner Agent** — breaks a task into practical execution steps.
* **Worker Agent** — executes the generated plan.
* **Verifier Agent** — evaluates the result and determines whether it is valid.
* **Orchestrator** — coordinates the complete workflow and manages task state.

This design creates a simple foundation for building reliable, testable AI agent workflows.

---

## 🧠 Architecture

```text
User Task
    ↓
Planner Agent
    ↓
Execution Plan
    ↓
Worker Agent
    ↓
Task Result
    ↓
Verifier Agent
    ↓
Verified Result
```

### Workflow States

```text
PENDING
   ↓
PLANNING
   ↓
WORKING
   ↓
VERIFYING
   ↓
COMPLETED
```

If an error occurs during execution or verification:

```text
        ↓
      FAILED
```

---

## ✨ Features

* 🤖 Multi-agent AI architecture
* 🧩 Task planning and decomposition
* ⚙️ AI-powered task execution
* 🔍 Automated result verification
* 🎯 Centralized workflow orchestration
* 📊 Task state tracking
* 🔌 Google Gemini API integration
* 🧪 Automated testing with pytest
* 🔐 Environment-based API configuration
* ⚠️ Error handling and validation
* 🐍 Modular Python project structure

---

## 🔄 How It Works

### 1. Planner Agent

The Planner receives the user's task and converts it into a structured execution plan.

```text
User Task
   ↓
Planner
   ↓
Execution Steps
```

The goal is to transform a high-level request into actionable steps.

### 2. Worker Agent

The Worker receives the generated plan and executes it using the configured Gemini model.

```text
Execution Plan
   ↓
Worker
   ↓
Task Result
```

### 3. Verifier Agent

The Verifier evaluates the Worker result and determines whether it satisfies the expected requirements.

```text
Task Result
   ↓
Verifier
   ↓
Verified Result
```

### 4. Orchestrator

The Orchestrator coordinates the agents and controls the overall workflow:

```text
Planner
   ↓
Worker
   ↓
Verifier
```

It also manages workflow states and handles failures.

---

## 📁 Project Structure

```text
PlanVerify/
│
├── app/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── worker.py
│   │   └── verifier.py
│   │
│   └── main.py
│
├── tests/
│   └── test_agents.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠️ Technology Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python 3.14+      | Application development            |
| Google Gemini API | AI agent reasoning and execution   |
| `google-genai`    | Gemini API integration             |
| `pytest`          | Automated testing                  |
| `python-dotenv`   | Environment variable management    |
| Dataclasses       | Structured task and workflow state |
| REST API          | API-based AI integration           |

---

## ⚙️ Getting Started

### Prerequisites

You will need:

* Python 3.14+
* Google Gemini API key
* Git
* A virtual environment

### 1. Clone the Repository

```bash
git clone https://github.com/linajawad/PlanVerify.git
cd PlanVerify
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.6-flash
```

> Keep your `.env` file private. Do not commit API keys to GitHub.

### 5. Run the Application

```bash
python -m app.main
```

---

## 🧪 Testing

The project includes automated tests using `pytest`.

Run:

```bash
pytest
```

Current test suite:

**7 tests passed**

The tests cover:

* Planner task generation
* Empty task validation
* Worker plan validation
* Gemini worker execution
* Verifier validation
* Verifier error handling
* End-to-end workflow orchestration

---

## 🎯 What This Project Demonstrates

PlanVerify demonstrates practical experience with:

* Multi-agent AI system design
* Agent orchestration
* Prompt-based task planning
* AI task execution
* Automated result verification
* Workflow state management
* Google Gemini API integration
* REST API integration
* Python application structure
* Automated testing
* Input validation
* Error handling
* Environment configuration

---

## 📌 Project Status

**Current status: Core workflow implemented and tested.**

The Planner, Worker, Verifier, and Orchestrator workflow is implemented with automated test coverage.

### Future Improvements

Potential future enhancements include:

* Persistent task history
* Advanced verification strategies
* Additional specialized agents
* Retry and recovery mechanisms
* Structured logging
* Observability
* Evaluation metrics
* Integration testing
* Monitoring dashboard

---

## 👩‍💻 Author

**Lina Jawad**

AI Automation • AI Agent Testing • QA Automation • Python • API Integration • Cybersecurity

GitHub: [@linajawad](https://github.com/linajawad)
