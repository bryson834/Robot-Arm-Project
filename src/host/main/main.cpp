//
// begin license header
//
// This file is part of Pixy CMUcam5 or "Pixy" for short
//
// All Pixy source code is provided under the terms of the
// GNU General Public License v2 (http://www.gnu.org/licenses/gpl-2.0.html).
// Those wishing to use Pixy source code, software and/or
// technologies under different licensing terms should contact us at
// cmucam@cs.cmu.edu. Such licensing terms are available for
// all portions of the Pixy codebase presented here.
//
// end license header
//

#include <signal.h>
#include "libpixyusb2.h"
#include <math.h>

Pixy2        pixy;
static bool  run_flag = true;

void  get_blocks()
{
  	int  Block_Index;
    double objectAngle, moveAngle, dx, dy;
    double initialAngle = 90;
    const char *objectArray[3];
    objectArray[0] = "Red Cup";
    objectArray[1] = "Yellow Peg";
    objectArray[2] = "Green Cylinder";
    objectArray[3] = "Blue Die";

    pixy.ccc.getBlocks();

    for(Block_Index = 0; Block_Index < pixy.ccc.numBlocks; Block_Index++)
    { 
      int x = pixy.ccc.blocks[Block_Index].m_x;
      int y = pixy.ccc.blocks[Block_Index].m_y;
     
      printf("----------------------------------------------------------------------\n");
      printf("%s\n", objectArray[Block_Index]);
      printf("All Data: ");
      pixy.ccc.blocks[Block_Index].print();

      //center of arm is (103,206)
      	if (x < 157.5)  //left side of arm
      	{
         	   dx = (157.5 - x);
         	   dy = (207 - y);
         	   objectAngle = atan2(dy, dx);
         	   moveAngle = objectAngle - initialAngle;
      	}
      	else if (x > 157.5) //right side of arm
      	{
         	   dx = (x - 157.5);
         	   dy = (207 - y);
         	   objectAngle = (180 - atan2(dy, dx));
         	   moveAngle = objectAngle - initialAngle;
      	}
      	else  //down the center
      	{
         	   objectAngle = 90;
         	   moveAngle = 0;
      	}

        printf("\nX: %i\n", x);
        printf("Y: %i\n\n", y);
      	printf("%s Angle = %f\n", objectArray[Block_Index], objectAngle);
      	printf("Move Angle = %f\n", moveAngle);
    }
}

int main()
{
  int  Result;

  printf ("=============================================================\n");
  printf ("= Robot Arm Location Code                                     =\n");
  printf ("=============================================================\n");

  printf ("Connecting to Pixy2 Camera...");

  // Initialize Pixy2 Connection //
  {
    Result = pixy.init();

    if (Result < 0)
    {
      printf ("Error\n");
      printf ("pixy.init() returned %d\n", Result);
      return Result;
    }

    printf ("Success\n");
  }

  // Set Pixy2 to color connected components program //
  pixy.changeProg("color_connected_components");
 
  int a = 1;
  while(a)
  {
    get_blocks();
    a = 0;
  }
}
