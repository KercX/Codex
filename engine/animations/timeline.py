class Timeline:
    def __init__(self):
        self.keyframes = []

    def add_keyframe(self, keyframe):
        self.keyframes.append(keyframe)

    def play(self):
        print("Playing animation with", len(self.keyframes), "keyframes")
