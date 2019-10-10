#include "Target.h"

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

Target::Target() {
  center.SetAll(0,10,-80);
  color.SetAll(0.8,0.7,0.8);
  innerRadius = 0.5;
  outerRadius = 4;
  isMoving = false;
  deltaX = 0.02;
}

void Target::SetBBX(double* _bbx) {
  bbx = _bbx;
}

void Target::Update(Node* ballList) {
  if( isMoving ) {
    center.SetX( center.GetX() + deltaX );
    if( center.GetX() < bbx[0] ) {
      center.SetX( bbx[0] );
      deltaX *= -1;
    }
    if( center.GetX() > bbx[1] ) {
      center.SetX( bbx[1] );
      deltaX *= -1;
    }
  }

  bool hit = false;
  bool isLast = false;
  Node* curBall = ballList;
  while(curBall != NULL) {
    Ball& b = curBall->ball;
    Vector3d ballCenter = b.GetCenter();
    if( (ballCenter-center).norm() < outerRadius) {
      if( fabs(ballCenter.GetZ()-center.GetZ()) < 1.0 ) {
	hit = true;
	break;
      }
    }

    curBall = curBall->next;
  }

  if( hit ) {
    //start isMoving
    isMoving = true;
    //change color
    color.SetX( drand48() );
    color.SetY( drand48() );
    color.SetZ( drand48() );
    deltaX *= 1.05;
  }
  
}

void Target::Draw() {

  //void glutSolidTorus(GLdouble innerRadius,
  //                  GLdouble outerRadius,
  //                  GLint nsides, GLint rings);

  glColor3f(color.GetX(),color.GetY(),color.GetZ());
  glPushMatrix();
  glTranslated(center[0],center[1],center[2]);
  glutSolidTorus(innerRadius,outerRadius,20,20);
  glPopMatrix();
}
