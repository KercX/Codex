# 🌙 Codex 

Codex is a modular 3D engine for scenes, animation and effects.

---

## Features

- Scene system
- Animation timeline
- Particle effects
- Real-time rendering

---

## Quick Example

```python
from engine.core.scene import Scene
from engine.core.object3d import Object3D

scene = Scene()
cube = Object3D("Cube")

scene.add(cube)
scene.render()
