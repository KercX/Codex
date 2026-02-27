class ParticleSystem:
    def __init__(self, count=100):
        self.count = count

    def emit(self):
        print(f"Emitting {self.count} particles")
