#include <stdlib.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include "Ball.h"
#include "Target.h"
#include "Vector.h"
using namespace mathtool;

#include <iostream>
using namespace std;

// all variables initialized to 1.0, meaning
// the triangle will initially be white
float red=1.0f, blue=1.0f, green=1.0f;

// time step
double dt = 0.02;
// yPlane
float yPlane = -4;

// create a linked-list
Node* head = NULL;

// a singular ball
Ball ball;
// a singular target
Target target;
// cannon position
Vector3d cannon;
// ball radius
double curRadius = 0.6;
double minRadius = 0.2;
double maxRadius = 1.4;
// maximum acceleration
double maxAccel = 850;
// cannon length
double cannonL = 0.5;
double maxCannonL = 1.5;
double minCannonL = 0.25;
// angle1 for rotating cannon
float angle1 = 45.0f;
float angle2 = 165.0f;

double bbx[]={-20,20,-4,20,-100,100};

void init(void) 
{


   GLfloat mat_specular[] = { 1.0, 1.0, 1.0, 0.0 };
   GLfloat mat_shininess[] = { 10.0 };
   GLfloat light_position[] = { 1.0, 1.0, 1.0, 0.0 };
   GLfloat light_ambient[] = { 0.8, 0.8, 0.8, 1.0 };
   GLfloat light_diffuse[] = { 1.0, 1.0, 1.0, 1.0 };
   GLfloat light_specular[] = { 0.8, 0.8, 0.8, 1.0 };
   glClearColor (0.0, 0.0, 0.0, 0.0);
   glShadeModel (GL_SMOOTH);

   glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular);
   glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess);


   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
   glLightfv(GL_LIGHT0, GL_POSITION, light_position);

   glEnable(GL_LIGHTING);
   glEnable(GL_LIGHT0);
   glEnable(GL_DEPTH_TEST);
}

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window of zero width).
	if (h == 0)
		h = 1;
	float ratio =  w * 1.0 / h;

        // Use the Projection Matrix
	glMatrixMode(GL_PROJECTION);

        // Reset Matrix
	glLoadIdentity();

	// Set the viewport to be the entire window
	glViewport(0, 0, w, h);

	// Set the correct perspective.
	gluPerspective(45.0f, ratio, 0.1f, 1000.0f);

	// Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW);

/*
glEnable(GL_LIGHTING);
glEnable(GL_LIGHT0);
GLfloat lightpos[] = {.5, 1., 1., 0.};
glLightfv(GL_LIGHT0, GL_POSITION, lightpos);
*/
}

void drawBBX() {
  glShadeModel (GL_SMOOTH);
  glNormal3d(1,0,0);
  glColor3f(1,0,0);
  glBegin(GL_QUADS); //left side
  glVertex3d(bbx[0],bbx[2],bbx[4]);
  glVertex3d(bbx[0],bbx[3],bbx[4]);
  glVertex3d(bbx[0],bbx[3],bbx[5]);
  glVertex3d(bbx[0],bbx[2],bbx[5]);
  glEnd();

  glNormal3d(-1,0,0);
  glColor3f(0,0,1);
  glBegin(GL_QUADS); //right side
  glVertex3d(bbx[1],bbx[2],bbx[4]);
  glVertex3d(bbx[1],bbx[3],bbx[4]);
  glVertex3d(bbx[1],bbx[3],bbx[5]);
  glVertex3d(bbx[1],bbx[2],bbx[5]);
  glEnd();

  glNormal3d(0,1,0);
  glColor3f(0.8,0.8,0.8);
  glBegin(GL_QUADS); //bottom side
  glVertex3d(bbx[0],bbx[2],bbx[4]);
  glVertex3d(bbx[0],bbx[2],bbx[5]);
  glVertex3d(bbx[1],bbx[2],bbx[5]);
  glVertex3d(bbx[1],bbx[2],bbx[4]);
  glEnd();

  glNormal3d(0,-1,0);
  glColor3f(0.0,0.8,0.2);
  glBegin(GL_QUADS); //top side
  glVertex3d(bbx[0],bbx[3],bbx[4]);
  glVertex3d(bbx[0],bbx[3],bbx[5]);
  glVertex3d(bbx[1],bbx[3],bbx[5]);
  glVertex3d(bbx[1],bbx[3],bbx[4]);
  glEnd();

  //back
  glNormal3d(0,0,-1);
  glColor3f(0.0,0.8,0.8);
  glBegin(GL_QUADS); //back side
  glVertex3d(bbx[0],bbx[2],bbx[4]);
  glVertex3d(bbx[0],bbx[3],bbx[4]);
  glVertex3d(bbx[1],bbx[3],bbx[4]);
  glVertex3d(bbx[1],bbx[2],bbx[4]);
  glEnd();
  //front
  glNormal3d(0,0,1);
  glColor3f(0.0,0.8,0.8);
  glBegin(GL_QUADS); //front side
  glVertex3d(bbx[0],bbx[2],bbx[5]);
  glVertex3d(bbx[0],bbx[3],bbx[5]);
  glVertex3d(bbx[1],bbx[3],bbx[5]);
  glVertex3d(bbx[1],bbx[2],bbx[5]);
  glEnd();
}

void getCannonEndPts(double ang1, double& cX, double& cY) {
  cX = cannon.GetX()+cannonL * cosd(ang1);
  cY = cannon.GetY()+cannonL * sind(ang1);
}
void getCannonEndPts3D(double ang1, double ang2, double& cX, double& cY, double& cZ) {
  cY = cannon.GetY()+ (cannonL * sind(ang1));
  double l2 = cannonL * cosd(ang1);
  cX = cannon.GetX()+ (cannonL * sind(ang2));
  cZ = cannon.GetZ()+ (cannonL * cosd(ang2));
}

void DrawAllBalls() {
  Node* tmp = head;
  while(tmp!=NULL) {
    tmp->ball.Draw();
    tmp = tmp->next;
  }
}
void UpdateAllBalls() {
  Node* tmp = head;
  while(tmp!=NULL) {
    tmp->ball.Update(dt);
    tmp = tmp->next;
  }
}
void AddBall(double _r, Vector3d stPt, Vector3d vel, Vector3d accelVec) {
  Node* newBall = new Node;
  newBall->ball.SetValues(curRadius,stPt,vel,accelVec,bbx);
  newBall->ball.SetRandomColor();
  newBall->next = head;
  head = newBall;
}


void RemoveAllNonMoving() {
  Node* predLoc = NULL;
  Node* location = head; 
  bool isLast = false;
  int numRemoved = 0;
  int numBallsRemaining = 0;
  int counter = 0;
  while(location != NULL) {
    if(location->next == NULL ) isLast = true;
    if(location->ball.IsMoving()) {
      //increment
      predLoc = location;
      location = location->next;
      numBallsRemaining++;
    }
    else { //not moving remove
      cout << "counter = " << counter << endl;
      numRemoved++;
      Node* tmp = location; //tmp points to what should be removed
      location = location->next; //move location over
      if( predLoc != NULL )
	predLoc->next = location;
      else
	head = location;
      delete tmp;
    }
    counter++;
  }//endwhile
  cout << "numBallsRemaining: " << numBallsRemaining << " numRemoved: " << numRemoved << endl;
}

void renderScene(void) {
glEnable(GL_DEPTH_TEST); 

	// Clear Color and Depth Buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glClearColor(0.5, 0.5, 0.5, 1.0);           // background is gray

	// Reset transformations
	glLoadIdentity();

	// Set the camera
	gluLookAt(	0.0f, 0.0f, 10.0f,
			0.0f, 0.0f,  0.0f,
			0.0f, 1.0f,  0.0f);

         // Enable lighting
        glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
        glEnable(GL_COLOR_MATERIAL);

        // draw bbx
	drawBBX();

	// draw yPlane
	glLineWidth(2);
	glBegin(GL_LINES);  //draw the yPlane
	   glVertex3f(-4.0f,yPlane, 0.0f);
	   glVertex3f(4.0f,yPlane, 0.0f);
	glEnd();

	//draw the ball(s)
	//ball.Draw();
	DrawAllBalls();
	target.Draw();

        //draw the cannon
	//double cX; //<<next 3 lines, for 2d
	//double cY;
	//getCannonEndPts(angle1,cX,cY);
	double cX;
	double cY;
	double cZ;
	getCannonEndPts3D(angle1, angle2 ,cX,cY,cZ);
	glColor3f(0,0,1);
	glLineWidth(2);
	glBegin(GL_LINES);  //draw the yPlane
	   glVertex3f(cannon.GetX(), cannon.GetY(), cannon.GetZ());
	   glVertex3f(cX, cY, cZ);
	glEnd();

	//ball.Update(dt);
	UpdateAllBalls();
        target.Update(head);	

	glutSwapBuffers();
}

void processNormalKeys(unsigned char key, int x, int y) {

	if (key == 27 || key=='q')  //quit
		exit(0);
        else if(key=='s') { //shoot
	  double cX, cY, cZ;
	  getCannonEndPts3D(angle1,angle2,cX,cY,cZ);
	  double accel = maxAccel * (cannonL/maxCannonL);
	  Vector3d stPt(cX,cY+curRadius,cZ);
	  Vector3d vel(0,0,0);
	  Vector3d accelVec(cX-cannon.GetX(),cY-cannon.GetY(),cZ-cannon.GetZ());
	  accelVec.selfNormalize();
	  accelVec.selfScale(accel);
	  //ball.SetValues(curRadius,stPt,vel,accelVec,yPlane);
	  AddBall(curRadius,stPt,vel,accelVec);
    cout << cannon.GetX() << " " << cannon.GetY() << " " << cannon.GetZ() << endl;
	}
	else if(key=='d') {
	  RemoveAllNonMoving();
	}
	else if(key=='1') {
	  cannonL -= 0.02;
	  if(cannonL<minCannonL) cannonL = minCannonL;
	}
	else if(key=='2') {
	  cannonL += 0.02;
	  if(cannonL>maxCannonL) cannonL = maxCannonL;
	}
	else if(key=='9') {
	  curRadius -= 0.2;
	  if(curRadius<minRadius) curRadius = minRadius;
	}
	else if(key=='0') {
	  curRadius += 0.2;
	  if(curRadius>maxRadius) curRadius = maxRadius;
	}
}

void processSpecialKeys(int key, int x, int y) {

  switch(key) {
      case GLUT_KEY_UP :
         angle1 += 1;
	 if(angle1>=100) angle1 = 100;
         break;
      case GLUT_KEY_DOWN :
         angle1 -= 1;
	 if(angle1<=0) angle1 = 0;
         break;
      case GLUT_KEY_LEFT :
         angle2 += 1;
	 if(angle2>=270) angle2 = 270;
         break;
      case GLUT_KEY_RIGHT :
         angle2 -= 1;
	 if(angle2<=90) angle2 = 90;
  }
}

int main(int argc, char **argv) {
        //cannon.SetAll(-4,yPlane,0);
        cannon.SetAll(0,yPlane,0);
	//set the target bbx
	target.SetBBX(bbx);

	// init GLUT and create window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(320,320);
	glutCreateWindow("ShootPts");
        
	init();
	// register callbacks
	glutDisplayFunc(renderScene);
	glutReshapeFunc(changeSize);
	glutIdleFunc(renderScene);

	// here are the new entries
	glutKeyboardFunc(processNormalKeys);
	glutSpecialFunc(processSpecialKeys);

	// enter GLUT event processing cycle
	glutMainLoop();

	return 1;
}
