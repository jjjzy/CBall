from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import Vector
import Ball

bbx = [-20,20,-4,20,-100,100]
yPlane = -4
curRadius = 0.6
minRadius = 0.2
maxRadius = 1.4

maxAccel = 850

cannonL = 0.5
maxCannonL = 1.5
minCannonL = 0.25

angle1 = 45.0
angle2 = 165.0

def init():
	# GLfloat mat_specular = { 1.0, 1.0, 1.0, 0.0 }
	# GLfloat mat_shininess = { 10.0 }
	# GLfloat light_position = { 1.0, 1.0, 1.0, 0.0 }
	# GLfloat light_ambient = { 0.8, 0.8, 0.8, 1.0 }
	# GLfloat light_diffuse = { 1.0, 1.0, 1.0, 1.0 }
	# GLfloat light_specular = { 0.8, 0.8, 0.8, 1.0 }
	print("init begin")

	# glClearColor(0.5, 0.5, 0.5, 1.0)

	mat_specular = [1.0, 1.0, 1.0, 0.0 ]
	mat_shininess = [10.0]
	light_position = [1.0, 1.0, 1.0, 0.0]
	light_ambient = [0.8, 0.8, 0.8, 1.0]
	light_diffuse = [1.0, 1.0, 1.0, 1.0]
	light_specular = [0.8, 0.8, 0.8, 1.0]

	glClearColor(0.0, 0.0, 0.0, 0.0)
	glShadeModel(GL_SMOOTH)
	
	glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	print("init end")




def drawBBX():
	print("called draw bbx")
	glShadeModel(GL_SMOOTH)
	glNormal3d(1,0,0)
	glColor3f(1,0,0)
	glBegin(GL_QUADS)
	glVertex3d(bbx[0],bbx[2],bbx[4])
	glVertex3d(bbx[0],bbx[3],bbx[4])
	glVertex3d(bbx[0],bbx[3],bbx[5])
	glVertex3d(bbx[0],bbx[2],bbx[5])
	glEnd()
	
	glNormal3d(-1,0,0)
	glColor3f(0,0,1)
	glBegin(GL_QUADS)
	glVertex3d(bbx[1],bbx[2],bbx[4])
	glVertex3d(bbx[1],bbx[3],bbx[4])
	glVertex3d(bbx[1],bbx[3],bbx[5])
	glVertex3d(bbx[1],bbx[2],bbx[5])
	glEnd()
	
	glNormal3d(0,1,0)
	glColor3f(0.8,0.8,0.8)
	glBegin(GL_QUADS)
	glVertex3d(bbx[0],bbx[2],bbx[4])
	glVertex3d(bbx[0],bbx[2],bbx[5])
	glVertex3d(bbx[1],bbx[2],bbx[5])
	glVertex3d(bbx[1],bbx[2],bbx[4])
	glEnd()
	
	glNormal3d(0,-1,0)
	glColor3f(0.0,0.8,0.2)
	glBegin(GL_QUADS)
	glVertex3d(bbx[0],bbx[3],bbx[4])
	glVertex3d(bbx[0],bbx[3],bbx[5])
	glVertex3d(bbx[1],bbx[3],bbx[5])
	glVertex3d(bbx[1],bbx[3],bbx[4])
	glEnd()
	
	glNormal3d(0,0,-1)
	glColor3f(0.0,0.8,0.8)
	glBegin(GL_QUADS)
	glVertex3d(bbx[0],bbx[2],bbx[4])
	glVertex3d(bbx[0],bbx[3],bbx[4])
	glVertex3d(bbx[1],bbx[3],bbx[4])
	glVertex3d(bbx[1],bbx[2],bbx[4])
	glEnd()
	
	glNormal3d(0,0,1)
	glColor3f(0.0,0.8,0.8)
	glBegin(GL_QUADS)
	glVertex3d(bbx[0],bbx[2],bbx[5])
	glVertex3d(bbx[0],bbx[3],bbx[5])
	glVertex3d(bbx[1],bbx[3],bbx[5])
	glVertex3d(bbx[1],bbx[2],bbx[5])
	glEnd()


def renderScene():
	glEnable(GL_DEPTH_TEST)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glClearColor(0.5, 0.5, 0.5, 1.0)

	glLoadIdentity()

	gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)

	glutSwapBuffers();

def DrawAllBalls():
	a = Ball.Ball()
	a.Draw()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(100,100)
glutInitWindowSize(320,320)
glutCreateWindow("ShootPts")

init()

glutDisplayFunc(renderScene);
#glutReshapeFunc(changeSize);
#glutIdleFunc(renderScene);

#glutKeyboardFunc(processNormalKeys);
#glutSpecialFunc(processSpecialKeys);
glutMainLoop()