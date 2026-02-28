# 🌙 Codex L

Welcome to the official documentation of **Codex L**.

A modular 3D engine supporting:

- Scene System
- Animation Timeline
- Particle Effects
- Real-time Rendering

---

## 🚀 Quick Example

```python
from engine.core.scene import Scene
from engine.core.object3d import Object3D

scene = Scene()
cube = Object3D("Cube")

scene.add(cube)
scene.render()
