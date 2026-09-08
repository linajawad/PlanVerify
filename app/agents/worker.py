from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.models import AgentTask, AgentResult, AgentStatus


class WorkerAgent:
    name = "worker"

    def __init__(self):
        self.model = GEMINI_MODEL
        self.client = None

    def _get_client(self):
        if self.client is None:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

        return self.client

    def run(self, task: AgentTask, plan: list[str]) -> AgentResult:
        if not plan:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error="No plan was provided.",
            )

        prompt = f"""
You are the worker agent in a multi-agent system.

Task:
{task.description}

Plan:
{chr(10).join(f"- {step}" for step in plan)}

Execute the task according to the plan.

Return a clear and concise result.
"""

        try:
            client = self._get_client()

            response = client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.COMPLETED,
                output={
                    "task_id": task.task_id,
                    "result": response.text.strip(),
                    "steps_executed": plan,
                },
            )

        except Exception as exc:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error=str(exc),
            )
        