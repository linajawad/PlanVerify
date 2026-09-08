from app.agents.planner import PlannerAgent
from app.agents.worker import WorkerAgent
from app.agents.verifier import VerifierAgent
from app.models import AgentTask, WorkflowState, TaskStatus


class AgentOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.worker = WorkerAgent()
        self.verifier = VerifierAgent()

    def run(self, task: AgentTask) -> WorkflowState:
        state = WorkflowState(task=task)

        # Step 1: Planning
        task.status = TaskStatus.PLANNING
        state.current_step = "planning"

        plan_result = self.planner.run(task)
        state.results.append(plan_result)

        if plan_result.error:
            task.status = TaskStatus.FAILED
            state.current_step = "failed"
            return state

        # Step 2: Execution
        task.status = TaskStatus.WORKING
        state.current_step = "working"

        plan = plan_result.output["plan"]
        worker_result = self.worker.run(task, plan)
        state.results.append(worker_result)

        if worker_result.error:
            task.status = TaskStatus.FAILED
            state.current_step = "failed"
            return state

        # Step 3: Verification
        task.status = TaskStatus.VERIFYING
        state.current_step = "verifying"

        verification_result = self.verifier.run(worker_result)
        state.results.append(verification_result)

        if verification_result.error:
            task.status = TaskStatus.FAILED
            state.current_step = "failed"
            return state

        # Workflow completed
        task.status = TaskStatus.COMPLETED
        state.current_step = "completed"

        return state
    