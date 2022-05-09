# Justin Ventura

from typing import Any, List


# This is the stack class:
class Stack:
    '''Custom Stack class'''

    def __init__(self, stack=None):
        '''
        Params:
            - stack: a previous stack as a list.
        '''
        self.stack = stack if stack else []

    # Function to push onto the stack:
    def push(self, val: Any = None) -> None:
        if val is None:
            pass

        self.stack.append(val)

    # Function to pop off the top of the stack:
    def pop(self) -> Any:
        return self.stack.pop()

    # Function to check if stack is empty:
    def is_empty(self) -> bool:
        return self.stack == []

    # Function to print stack:
    def sprint(self) -> List[Any]:
        print(self.stack)
        return self.stack
