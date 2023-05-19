class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        return '\n'.join(musician.play() for musician in self.musicians)
