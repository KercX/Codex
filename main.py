from engine.core.scene import Scene
from engine.core.object3d import Object3D
from engine.core.camera import Camera

scene = Scene()
camera = Camera()
cube = Object3D("Cube")

scene.add(cube)
scene.add_camera(camera)

scene.render()
