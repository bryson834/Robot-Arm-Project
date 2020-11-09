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


void handle_SIGINT(int unused)
{
  // On CTRL+C - abort! //

  run_flag = false;
}

void  get_blocks()
{
  	int  Block_Index;
    double moveAngle, dieAngle, dx, dy;
    double initialAngle = 90;
    const char *objectArray[3];
    objectArray[0] = "Red Cup";
    objectArray[1] = "Yellow Cylinder";
    objectArray[2] = "Green Cylinder";
    objectArray[3] = "Blue Die";

    pixy.ccc.getBlocks();

    double x = pixy.ccc.blocks->m_x;
    double y = pixy.ccc.blocks->m_y;

    for(Block_Index = 0; Block_Index < pixy.ccc.numBlocks; Block_Index++)
    {
      printf("\n%s\n", objectArray[Block_Index]);
      printf("All Data: ");
      pixy.ccc.blocks[Block_Index].print();
      printf("X = %d\n", x);
      printf("Y = %d\n", y);
      


      //center of arm is (103,206)
      	if (x < 157.5)  //left side of arm
      	{
         	   dx = (157.5 - x);
         	   dy = (207 - y);
         	   dieAngle = atan2(dy, dx);
         	   moveAngle = dieAngle - initialAngle;
      	}
      	else if (x > 157.5) //right side of arm
      	{
         	   dx = (x - 157.5);
         	   dy = (207 - y);
         	   dieAngle = (180 - atan2(dy, dx));
         	   moveAngle = dieAngle - initialAngle;
      	}
      	else  //down the center
      	{
         	   dieAngle = 90;
         	   moveAngle = 0;
      	}

      	printf("Die Angle = %f\n", dieAngle);
      	printf("Move Angle = %f\n", moveAngle);
    }
}

int main()
{
  int  Result;

  // Catch CTRL+C (SIGINT) signals //
  signal (SIGINT, handle_SIGINT);

  printf ("=============================================================\n");
  printf ("= PIXY2 Get Blocks Demo                                     =\n");
  printf ("=============================================================\n");

  printf ("Connecting to Pixy2...");

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

  // Get Pixy2 Version information //
  {
    Result = pixy.getVersion();

    if (Result < 0)
    {
      printf ("pixy.getVersion() returned %d\n", Result);
      return Result;
    }

    pixy.version->print();
  }

  // Set Pixy2 to color connected components program //
  pixy.changeProg("color_connected_components");

  while(1)
  {
    get_blocks();

    if (run_flag == false)
    {
      // Exit program loop //
      break;
    }
  }

  printf ("PIXY2 Get Blocks Demo Exit\n");
}
