from app.models import AgentTask
from app.orchestrator import AgentOrchestrator


def main():
    task = AgentTask(
        task_id="task-001",
        description="Test the AgentOps workflow",
    )

    orchestrator = AgentOrchestrator()
    state = orchestrator.run(task)

    print("\n=== AgentOps Test ===")
    print(f"Task ID: {state.task.task_id}")
    print(f"Task Status: {state.task.status.value}")
    print(f"Current Step: {state.current_step}")

    print("\n=== Agent Results ===")

    for result in state.results:
        print(f"\nAgent: {result.agent_name}")
        print(f"Status: {result.status.value}")
        print(f"Output: {result.output}")
        if result.error:
            print(f"Error: {result.error}")


if __name__ == "__main__":
    main()
    