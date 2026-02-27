class Scene:
    def __init__(self):
        self.objects = []
        self.cameras = []

    def add(self, obj):
        self.objects.append(obj)

    def add_camera(self, camera):
        self.cameras.append(camera)

    def render(self):
        print("Rendering scene with objects:", [o.name for o in self.objects])
