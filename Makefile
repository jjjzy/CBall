all: shootpts

main.o: main.cpp
	g++ -O2 -std=c++11 -DMACOS -c main.cpp -I/usr/X11/include 

Basic.o: Basic.cpp
	g++ -O2 -std=c++11 -DMACOS -c Basic.cpp -I/usr/X11/include

Ball.o: Ball.cpp
	g++ -O2 -std=c++11 -DMACOS -c Ball.cpp -I/usr/X11/include 

Target.o: Target.cpp
	g++ -O2 -std=c++11 -DMACOS -c Target.cpp -I/usr/X11/include 

shootpts: main.o Basic.o Ball.o Target.o
	g++ main.o Basic.o Ball.o Target.o -o shootpts -lglut -lGLU -lGL -lm
 
clean:
	rm *.o shootpts
