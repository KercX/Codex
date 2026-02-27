class Object3D:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)
        self.rotation = (0, 0, 0)
        self.scale = (1, 1, 1)

    def translate(self, x, y, z):
        self.position = (self.position[0]+x, self.position[1]+y, self.position[2]+z)
