class WorkFlowRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, workflow_name, workflow_object):
        if workflow_name in self._registry:
            raise ValueError(f"Workflow '{workflow_name}' is already registered.")
        self._registry[workflow_name] = workflow_object

    def get_workflow(self, workflow_name):
        return self._registry.get(workflow_name)

    def list_workflows(self):
        return list(self._registry.keys())

workflow_registry = WorkFlowRegistry()