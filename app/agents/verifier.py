from app.models import AgentResult, AgentStatus


class VerifierAgent:
    name = "verifier"

    def run(self, result: AgentResult) -> AgentResult:
        if result.status != AgentStatus.COMPLETED:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error="Cannot verify an incomplete result.",
            )

        if result.output is None:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.FAILED,
                error="Worker returned no output.",
            )

        return AgentResult(
            agent_name=self.name,
            status=AgentStatus.COMPLETED,
            output={
                "verified": True,
                "original_agent": result.agent_name,
                "result": result.output,
            },
        )
    