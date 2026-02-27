#ifndef CORE_HPP
#define CORE_HPP

#include <string>
#include <vector>
#include <iostream>

class Object3D {
public:
    std::string name;
    float position[3] = {0,0,0};

    Object3D(std::string n) : name(n) {}
    void translate(float x, float y, float z) {
        position[0] += x;
        position[1] += y;
        position[2] += z;
    }
};

class Scene {
public:
    std::vector<Object3D> objects;
    void add(Object3D obj) { objects.push_back(obj); }
    void render() {
        std::cout << "Rendering scene with objects:\n";
        for(auto &o: objects) std::cout << "- " << o.name << "\n";
    }
};

#endif
