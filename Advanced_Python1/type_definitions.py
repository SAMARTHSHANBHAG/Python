from typing import List, Tuple, Dict, Union
n: int = 5

name : str = "Sam"

def sum(a: int, b: int) -> int:
    return a + b

def greeting(name: str) -> str:
    return f"Hello, {name}!"

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5] 
# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30) 
# Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 
# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid 