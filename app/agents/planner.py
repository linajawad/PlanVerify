from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.models import AgentTask, AgentResult, AgentStatus


class PlannerAgent:
    name = "planner"

    def __init__(self):
        self.model = GEMINI_MODEL
        self.client = None

    def _get_client(self):
        if self.client is None:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

        return self.client

    def run(self, task: AgentTask) -> AgentResult:
        if not task.description.strip():
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error="Task description cannot be empty.",
            )

        prompt = f"""
You are the planning agent in a multi-agent system.

Your job is to create a clear execution plan for the following task:

Task:
{task.description}

Create 3 to 6 practical steps that another AI worker can execute.

Return ONLY the steps, one step per line.
Do not number them.
Do not add explanations.
"""

        try:
            client = self._get_client()

            response = client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            plan_text = response.text.strip()

            plan = [
                line.strip()
                for line in plan_text.splitlines()
                if line.strip()
            ]

            if not plan:
                return AgentResult(
                    agent_name=self.name,
                    status=AgentStatus.FAILED,
                    error="Planner returned an empty plan.",
                )

            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.COMPLETED,
                output={
                    "task_id": task.task_id,
                    "plan": plan,
                },
            )

        except Exception as exc:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error=str(exc),
            )
        