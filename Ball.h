#ifndef BALL_H_
#define BALL_H_

#include "Vector.h"
using namespace mathtool;
#include <iostream>
using namespace std;

class Ball {
  public:
    Ball();
    
    void SetValues(double _radius, Vector3d _center, Vector3d _vel, Vector3d _accel, double* _bbx); 
    void SetRandomColor();
    bool IsMoving();

    void Update(double dt);
    void ResolveCollision();
    Vector3d GetCenter() { return center; }
    void Draw();
  private:
    Vector3d center;
    Vector3d velocity;
    Vector3d oldVelocity;
    Vector3d accel;

    Vector3d color;

    double radius;

    //double yPlane;
    double* bbx;
};


struct Node {
  Ball ball;
  Node* next;
};


#endif //BALL_H_
