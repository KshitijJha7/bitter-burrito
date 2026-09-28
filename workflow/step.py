from collections.abc import Callable
from typing import Any
from __future__ import annotations
from workflow.workflow import Workflow

class Step:
    def __init__(self, name, fn:Callable[...,Any]):
        self.name = name
        self.fn = fn

    def setParent(self, step:Step):
        self.parent = step

    def getParent(self):
        return getattr(self, 'parent', None)

    def setChildren(self, steps:list[Step]):
        self.children = steps

    def getChildren(self):
        return self.children
     
    def execute(self, *args, **kwargs):
        return self.fn(*args, **kwargs)