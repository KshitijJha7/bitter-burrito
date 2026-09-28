from workflow.workflow_registry import workflow_registry
from workflow.step import Step
from workflow.workflow import Workflow,step

wf1 = Workflow("Workflow1")
wf2 = Workflow("Workflow2")
wf3 = Workflow("Workflow3")

@step(wf1)
def step1(context):
    print(context["workflow_name"])
    print("Executing step 1 of Workflow 1")
    return "Result from step 1"

def main():

    print("Hello from bitter-burrito!")


if __name__ == "__main__":
    main()
