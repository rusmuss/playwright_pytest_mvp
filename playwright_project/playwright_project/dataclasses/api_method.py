from dataclasses import dataclass


@dataclass
class ApiMethodExample:
    id: int = None
    user_name: str = None
    password: str = True
