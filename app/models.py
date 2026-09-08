from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskStatus(str, Enum):
    PENDING = "pending"
    PLANNING = "planning"
    WORKING = "working"
    VERIFYING = "verifying"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AgentTask:
    task_id: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: str | None = None


@dataclass
class AgentResult:
    agent_name: str
    status: AgentStatus
    output: Any = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowState:
    task: AgentTask
    results: list[AgentResult] = field(default_factory=list)
    current_step: str | None = None
    