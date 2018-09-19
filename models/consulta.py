class Consulta:
    def __init__(self, type, goal, height, weight, paciente, strategy, id=None, date=None):
        self.id = id
        self.type = type
        self.date = date
        self.goal = goal
        self.height = height
        self.weight = weight
        self.paciente = paciente
        self.strategy = strategy
