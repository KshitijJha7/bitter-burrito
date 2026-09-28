from functools import wraps
from workflow.workflow_registry import workflow_registry
from workflow.step import Step

class Workflow:
    def __init__(self, name):
        self.name = name
        workflow_registry.register(self.name,self)
        self.steps = {}
        self.run_context = {}

    def add_step(self, step:Step):
        self.steps[step.name] = step

    def set_root_step(self, step_name):
        if step_name not in self.steps:
            raise ValueError(f"Step '{step_name}' is not defined in the workflow.")
        self.root_step = self.steps[step_name]


def step(workflow):
    def decorator(fn):

        @wraps(fn)
        def wrapper():
            return fn(workflow.context)

        workflow.add_step(
            Step(fn.__name__, wrapper)
        )

        return wrapper

    return decorator