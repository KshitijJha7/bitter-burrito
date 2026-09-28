from collections.abc import Callable
from typing import Any
from __future__ import annotations
from workflow.workflow import Workflow

class Step:
    def __init__(self, name, fn:Callable[...,Any],parents:list[str]=[],children:list[str]=[]):
        self.name = name
        self.fn = fn
        self.parents = parents
        self.children = children

    def getParents(self)->list[str]:
        return self.parents

    def getChildren(self)->list[str]:
        return self.children
     
    def execute(self):
        return self.fn()