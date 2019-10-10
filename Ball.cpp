#include "Ball.h"

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

double damping = 0.95;
//double collisionDamping = 0.3;
double collisionDamping = 0.3;

Ball::Ball() {
  center.SetAll(0,0,0);
  velocity.SetAll(0,0,0);
  accel.SetAll(0,0,0);
  color.SetAll(0.3,0.2,0.8);
}

void Ball::SetValues(double _radius, Vector3d _center, Vector3d _vel, Vector3d _accel, double* _bbx) {
  radius = _radius;
  center = _center;
  velocity = _vel;
  accel = _accel;
  bbx = _bbx;
}

void Ball::SetRandomColor() {
  color.SetX( drand48() );
  color.SetY( drand48() );
  color.SetZ( drand48() );
}

bool Ball::IsMoving() {
  if( velocity.norm() < 0.2 ) return true;
  else return false;
}

void Ball::Update(double dt) {
  //cout << "Ball update! center = " << center << " vel = " << velocity << " accel = " << accel << endl;
  center = center + velocity * dt;
  oldVelocity = velocity;
  velocity = velocity + accel * dt;
  double oldAccelY = accel.GetY();
  oldAccelY -= 9.8;
  accel.SetY(oldAccelY);
  accel *= damping; 

  ResolveCollision(); //this should fix things in the case that it goes out of bounds

  if(accel.norm() < 0.5 ) accel.SetAll(0,0,0);
  if(velocity.norm() < 0.5 ) velocity.SetAll(0,0,0);
}

//              [  0 , 1  ,  2  , 3  ,  4  , 5  ]
// bbx contains [xMin,xMax, yMin,yMax, zMin,zMax]
void Ball::ResolveCollision() {
  //resolve X component
  if( center.GetX()-radius < bbx[0] ) {
    double oldCenterX = center.GetX();
    //make sure center doesn't cross plane
    center.SetX(bbx[0]+radius);
    //reflect velocity - just change y direction
    velocity.SetX( -1*velocity.GetX() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
  if( center.GetX()+radius > bbx[1] ) {
    double oldCenterX = center.GetX();
    //make sure center doesn't cross plane
    center.SetX(bbx[1]-radius);
    //reflect velocity - just change y direction
    velocity.SetX( -1*velocity.GetX() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
  //resolve Y component
  if( center.GetY()-radius < bbx[2] ) {
    double oldCenterY = center.GetY();
    //make sure center doesn't cross plane
    center.SetY(bbx[2]+radius);
    //reflect velocity - just change y direction
    velocity.SetY( -1*velocity.GetY() );
    //accel.SetY( -1*accel.GetY() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
  if( center.GetY()+radius > bbx[3] ) {
    double oldCenterY = center.GetY();
    //make sure center doesn't cross plane
    center.SetY(bbx[3]-radius);
    //reflect velocity - just change y direction
    velocity.SetY( -1*velocity.GetY() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
  //resolve Z component
  if( center.GetZ()-radius < bbx[4] ) {
    double oldCenterZ = center.GetZ();
    //make sure center doesn't cross plane
    center.SetZ(bbx[4]+radius);
    //reflect velocity - just change y direction
    velocity.SetZ( -1*velocity.GetZ() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
  if( center.GetZ()+radius > bbx[5] ) {
    double oldCenterZ = center.GetZ();
    //make sure center doesn't cross plane
    center.SetZ(bbx[5]-radius);
    //reflect velocity - just change y direction
    velocity.SetZ( -1*velocity.GetZ() );
    velocity *= collisionDamping;
    accel *= collisionDamping;
  }
}

void Ball::Draw() {
  //cout << "Ball draw!" << endl;

  //glColor3f(0.3,0.2,0.8);
  glColor3f(color.GetX(),color.GetY(),color.GetZ());
  glPushMatrix();
  glTranslated(center[0],center[1],center[2]);
  glutSolidSphere(radius,10,10);
  glPopMatrix();

  /*
  glPointSize(3);
  glColor3f(1,0,0);
  glBegin(GL_POINTS);
  glVertex3d(center[0],center[1],center[2]);
  glEnd();
  */
}
