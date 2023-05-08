from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_completed(self):
        return self.completion_percentage == 100

    def update_completion(self, new_completion_percentage):
        self.completion_percentage = int(new_completion_percentage)

    def update_priority(self, new_priority):
        self.priority = int(new_priority)