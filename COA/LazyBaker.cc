// ******************** Lazy Baker Program by ********************
// ********************   David P. Feldman    ********************
// ********************   15 February 1998    ******************** 
// ********************   dpf@santafe.edu     ********************

// ********* To learn more about the lazy Baker map, see *********
// *********   A. Lakshminarayan and N. L. Balazs, "The  ********* 
// *********    Classical and Quantum Mechanics of Lazy  *********
// *********   Baker Maps," Annals of Physics 226 (1993) *********
// *********                  350-373                    *********

#include <iostream.h>
#include <fstream.h>
#include <stdio.h>
#include <math.h>

int main()
{
  char *file_ptr = "output_temp"; // name of file data is sent to
  // you'll need to use a plotting program to visualize the
  // output.  i used gnuplot.
  ofstream tfile(file_ptr);
  int N = 7000; // number of iterations
  double x = 0.2; // initial x position
  double y = 0.3; // initial y position
  double x_temp, y_temp; // holds x,y as map is being iterated
  double A = 0.3; // map parameters
  double B = 0.5; // map parameters

  // A = 0.35, B = 0.64 will produce a funky pattern
  // A = 0.30, B = 0.5 will produce a "mostly random" pattern


  for( int i=0; i<N; i++){
    if( x<=A){
      x_temp = x/A;
      y_temp = A*y;}
    if( x>A && x<=B){
      x_temp = 1-y;
      y_temp = x;}
    if(x>B){
      x_temp = (x-B)/(1-B);
      y_temp = y*(1-B) + B;}
    x=x_temp;
    y=y_temp;
    
    tfile << x << "  " << y << "  "<< endl;
  }
  
}

