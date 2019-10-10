#ifndef TARGET_H_
#define TARGET_H_

#include "Vector.h"
using namespace mathtool;
#include <iostream>
using namespace std;

#include "Ball.h"

class Target {
public:
  Target();

  void Update(Node* ballList);
  void Draw();
  void SetBBX(double* _bbx);
  Vector3d GetCenter() { return center; }

private:
  Vector3d center;
  Vector3d color;
  double* bbx;
  double innerRadius, outerRadius;
  bool isMoving;
  double deltaX;
};

#endif 
