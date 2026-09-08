import os

os.environ["GEMINI_API_KEY"] = "test-key"

from unittest.mock import MagicMock, patch

from app.models import AgentTask, AgentResult, AgentStatus, TaskStatus
from app.agents.planner import PlannerAgent
from app.agents.worker import WorkerAgent
from app.agents.verifier import VerifierAgent
from app.orchestrator import AgentOrchestrator


def test_planner_creates_plan():
    task = AgentTask(
        task_id="test-001",
        description="Test a simple task",
    )

    fake_response = MagicMock()
    fake_response.text = """Understand the task
Break the task into actionable steps
Execute the required work
Verify the result"""

    with patch("app.agents.planner.genai.Client") as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.models.generate_content.return_value = fake_response

        planner = PlannerAgent()
        result = planner.run(task)

    assert result.status == AgentStatus.COMPLETED
    assert result.output["task_id"] == "test-001"
    assert len(result.output["plan"]) == 4


def test_planner_rejects_empty_task():
    task = AgentTask(
        task_id="test-002",
        description="",
    )

    planner = PlannerAgent()
    result = planner.run(task)

    assert result.status == AgentStatus.FAILED
    assert result.error == "Task description cannot be empty."


def test_worker_requires_plan():
    task = AgentTask(
        task_id="test-003",
        description="Test worker",
    )

    worker = WorkerAgent()
    result = worker.run(task, [])

    assert result.status == AgentStatus.FAILED
    assert result.error == "No plan was provided."


def test_worker_uses_gemini():
    task = AgentTask(
        task_id="test-004",
        description="Test Gemini worker",
    )

    fake_response = MagicMock()
    fake_response.text = "Task completed successfully."

    with patch("app.agents.worker.genai.Client") as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.models.generate_content.return_value = fake_response

        worker = WorkerAgent()

        result = worker.run(
            task,
            [
                "Understand the task",
                "Execute the task",
            ],
        )

    assert result.status == AgentStatus.COMPLETED
    assert result.output["result"] == "Task completed successfully."

    mock_client.models.generate_content.assert_called_once()


def test_verifier_accepts_valid_result():
    worker_result = AgentResult(
        agent_name="worker",
        status=AgentStatus.COMPLETED,
        output={
            "result": "Task completed",
        },
    )

    result = VerifierAgent().run(worker_result)

    assert result.status == AgentStatus.COMPLETED
    assert result.output["verified"] is True
    assert result.output["original_agent"] == "worker"


def test_verifier_rejects_missing_output():
    result = AgentResult(
        agent_name="worker",
        status=AgentStatus.COMPLETED,
        output=None,
    )

    verification = VerifierAgent().run(result)

    assert verification.status == AgentStatus.FAILED
    assert verification.error == "Worker returned no output."


def test_orchestrator_completes_workflow():
    task = AgentTask(
        task_id="test-orchestrator",
        description="Test the complete agent workflow",
    )

    fake_planner_response = MagicMock()
    fake_planner_response.text = """Understand the task
Break the task into steps
Execute the task
Verify the result"""

    fake_worker_response = MagicMock()
    fake_worker_response.text = "Workflow task completed."

    with patch("app.agents.planner.genai.Client") as mock_planner_client_class:
        with patch("app.agents.worker.genai.Client") as mock_worker_client_class:

            mock_planner_client = mock_planner_client_class.return_value
            mock_planner_client.models.generate_content.return_value = (
                fake_planner_response
            )

            mock_worker_client = mock_worker_client_class.return_value
            mock_worker_client.models.generate_content.return_value = (
                fake_worker_response
            )

            orchestrator = AgentOrchestrator()
            state = orchestrator.run(task)

    assert state.task.status == TaskStatus.COMPLETED
    assert state.current_step == "completed"
    assert len(state.results) == 3

    assert state.results[0].agent_name == "planner"
    assert state.results[0].status == AgentStatus.COMPLETED

    assert state.results[1].agent_name == "worker"
    assert state.results[1].status == AgentStatus.COMPLETED

    assert state.results[2].agent_name == "verifier"
    assert state.results[2].status == AgentStatus.COMPLETED
    