from functools import wraps
from workflow.workflow_registry import workflow_registry
from workflow.step import Step
from collections import deque

class Workflow:
    def __init__(self, name:str,concurrency:int=1):
        self.name = name
        workflow_registry.register(self.name,self)
        self.steps = {}
        self.concurrency = concurrency

    def add_step(self, step:Step):
        self.steps[step.name] = step

    def set_root_step(self, step_name):
        if step_name not in self.steps:
            raise ValueError(f"Step '{step_name}' is not defined in the workflow.")
        self.root_step = self.steps[step_name]

    def save(self):
        pass

    def run(self,context:dict|None = None):
        if not hasattr(self, 'root_step'):
            raise ValueError("Root step is not defined for the workflow.")
        q = deque([self.root_step])
        # pop concurrency number of steps from the queue and execute them
        while q:
            batch = []
            while len(q) > 0 and len(batch) < self.concurrency:
                batch.append(q.popleft())
                

def step(workflow: Workflow,parents: list[str] | None = None,children: list[str] | None = None,):
    def decorator(fn):
        step = Step(
            name=fn.__name__,
            fn=fn,
            parents=parents or [],
            children=children or [],
        )
        workflow.add_step(step)
        return fn

    return decorator