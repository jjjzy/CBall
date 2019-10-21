from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import Vector
import Ball
import Target

bbx = [-20,20,-4,20,-100,100]
yPlane = -4
curRadius = 0.6
minRadius = 0.2
maxRadius = 1.4

maxAccel = 850

cannonL = 0.5
maxCannonL = 1.5
minCannonL = 0.25

dt = 0.02

angle1 = 45.0
angle2 = 165.0

cannon = Vector.Vector3D(0, 0, 0)
target = Target.Target()

head = Ball.node()
ballList = []


def init():
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

def drawBBX():
	glShadeModel (GL_SMOOTH);
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

def processNormalKeys(bkey, x, y):
	global cannonL
	global curRadius
	key = bkey.decode("utf-8")
	if key == chr(27) or key == 'q':
		sys.exit()
	elif key == 's':
		a = getCannonEndPts3D(angle1,angle2)
		accel = maxAccel * (cannonL/maxCannonL)
		stPt = Vector.Vector3D(a.GetX(), a.GetY()+curRadius, a.GetZ())
		vel = Vector.Vector3D(0, 0, 0)
		accelVec = Vector.Vector3D(a.GetX()-cannon.GetX(),a.GetY()-cannon.GetY(),a.GetZ()-cannon.GetZ())

		accelVec.selfNormalize()
		accelVec.self_scale(accel)
		AddBall(curRadius, stPt, vel, accelVec)
	elif key == '1':
		# print(cannonL)
		cannonL -= 0.02
		if cannonL < minCannonL: 
			cannonL = minCannonL
	elif key == '2':
		# print(cannonL)
		cannonL += 0.02
		if cannonL > maxCannonL:
			cannonL = maxCannonL
	elif key == '9':
		curRadius -= 0.2
		if curRadius < maxRadius:
			curRadius = minRadius
	elif key == '0':
		curRadius += 0.2
		if curRadius > maxRadius:
			curRadius = maxRadius

def processSpecialKeys(key, x, y):
	global angle1
	global angle2
	if key == GLUT_KEY_UP:
		angle1 += 1
		if angle1 >= 100:
			angle1 = 100
	elif key == GLUT_KEY_DOWN:
		angle1 -= 1
		if angle1 <= 0:
			angle1 = 0
	elif key == GLUT_KEY_LEFT:
		angle2 += 7
		if angle2 >= 270:
			angle2 = 270
	elif key == GLUT_KEY_RIGHT:
		angle2 -= 7
		if angle2 <= 90:
			angle2 = 90


def getCannonEndPts3D(ang1, ang2):
	cY = cannon.GetY()+ (cannonL * Vector.sind(ang1))
	l2 = cannonL * Vector.cosd(ang1)
	cX = cannon.GetX()+ (cannonL * Vector.sind(ang2))
	cZ = cannon.GetZ()+ (cannonL * Vector.cosd(ang2))
	a = Vector.Vector3D(cX, cY, cZ)
	return a

def changeSize(w, h):
	if h == 0:
		h = 1
	ratio = w * 1.0 / h

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glViewport(0, 0, w, h);
	gluPerspective(45.0, ratio, 0.1, 1000.0);
	glMatrixMode(GL_MODELVIEW);

def renderScene():
	global target
	glEnable(GL_DEPTH_TEST)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glClearColor(0.5, 0.5, 0.5, 1.0)

	glLoadIdentity()

	gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)

	drawBBX()

	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex3f(-4.0,yPlane, 0.0)
	glVertex3f(4.0,yPlane, 0.0)
	glEnd()

	DrawAllBalls()
	target.Draw()

	cX = float()
	cY = float()
	cZ = float()

	a = getCannonEndPts3D(angle1, angle2)

	glColor3f(0, 0, 1)
	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex3f(cannon.GetX(), cannon.GetY(), cannon.GetZ())
	glVertex3f(a.GetX(), a.GetY(), a.GetZ())
	glEnd()

	UpdateAllBalls()
	target.Update(ballList)

	# for i in range(len(ballList)):
	# 	print("ball ", i + 1, "'s velocity: ")
	# 	ballList[i].velocity.print_vec()

	glutSwapBuffers()

def DrawAllBalls():
	size = len(ballList)
	for i in range(len(ballList)):
		ballList[i].Draw()


def UpdateAllBalls():
    global ballList
    for i in range(len(ballList)):
        ballList[i].Update(dt, ballList)
        # print(my_t[0])
        # print(my_t[1])
        # ballList[0].velocity.assign_vec(Vector.Vector3D(5, 5, 5))
        # ballList[my_t[2]].velocity.assign_vec(my_t[3])
        print("ball ", i + 1, "'s velocity: ")
        ballList[i].velocity.print_vec()
        print(ballList[i].IsMoving())
        # print(rt_val[1])
        # rt_val[0].print_vec()
        # ballList[rt_val[3]].velocity.assign_val(rt_val[0], rt_val[1], rt_val[2])
        # ballList[0].velocity.assign_val(15, 15, 15)

def AddBall(_r, stPt, vel, accelVec):
	global ballList
	newBall = Ball.Ball()
	newBall.SetValues(curRadius, stPt, vel, accelVec, bbx)
	newBall.SetRandomColor()
	collision_stat = False
	for i in range(len(ballList)):
		if newBall.detect_collision(ballList[i]) == True and len(ballList) != 0:
			collision_stat = True
	
	if collision_stat == False:
		ballList.append(newBall)
	else:
		print("CANT SHOOT!!!!")
		return
	# ballList.append(newBall)

cannon.Set_All(0, yPlane, 0)
target.SetBBX(bbx)

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(100,100)
glutInitWindowSize(600,600)
glutCreateWindow("ShootPts")

init()

glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize)
glutIdleFunc(renderScene)

glutKeyboardFunc(processNormalKeys)
glutSpecialFunc(processSpecialKeys)
glutMainLoop()