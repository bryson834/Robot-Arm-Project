/*

*/
//#include <SPI.h>
#include <Pixy2.h>
#include <math.h>

Pixy2 pixy;

double initialAngle = 90;
int i = 1;
int x = pixy.ccc.blocks[i].m_x;
int y = pixy.ccc.blocks[i].m_y;
double moveAngle;
double dieAngle;
double dx;
double dy;

void setup() {
    serial.begin(9600);
    serial.print("starting");

}

void loop() {

    serial.print("X = ");
    serial.println(x);
    serial.print("Y = ");
    serial.println(y);

    //center of arm is (103,206)

    if(x < 103) // left side of arm
      {
        dx = (103 - x);
        dy = (206 - y);
        dieAngle = atan(dy,dx);
        moveAngle = dieAngle - initialAngle;
      }
    else if (x > 103) // right side of arm
      {
        dx = (x - 103);
        dy = (206 - y);
        dieAngle = (180 - atan(dy,dx));
        moveAngle = dieAngle - initialAngle;
      }
    else // down the center
      {
        dieAngle = 90;
        moveAngle = 0;
      }

    serial.print("dieAngle = ");
    serial.println(dieAngle);
    serial.print("moveAngle = ");
    serial.println(moveAngle);



    delay(200);


}
