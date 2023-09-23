from dataclasses import dataclass


@dataclass
class TaskDto:

    id: int
    message: str

    def __str__(self):
        return f"id -> {self.id} message -> {self.message}\n"

    def __repr__(self):
        return f"id -> {self.id} message -> {self.message}\n"
