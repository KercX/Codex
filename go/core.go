package core

import "fmt"

type Object3D struct {
    Name     string
    Position [3]float64
}

type Scene struct {
    Objects []Object3D
}

func (s *Scene) Add(obj Object3D) {
    s.Objects = append(s.Objects, obj)
}

func (s *Scene) Render() {
    fmt.Println("Rendering scene with objects:")
    for _, o := range s.Objects {
        fmt.Println("-", o.Name)
    }
}

// Example usage
func Example() {
    scene := Scene{}
    cube := Object3D{Name: "Cube"}
    scene.Add(cube)
    scene.Render()
}
