import math as m
import mymodule as mm


#Q1----by using Euler's method
#Q1(b)----dy/dx=ylny/x
def q1a(y,x):
	f = y*m.log(y)/x
	return f

def printing(x,y):#for printing the matrix in .txt file
        for i in range(len(x)):
                f.write(str(x[i]))
                f.write("	")
                f.write(str(y[i]))
                f.write("\n")
        f.close()
       
with open('q1a_p5.txt', "r+") as f:#for dx=0.5
        y, x = mm.euler(q1a,m.e,2,10,0.5)#taking parameter(dy/dx,y(x_0),x_0,x_max,dx)
        printing(x,y)
	
with open('q1a_p1.txt', "r+") as f:#for dx=0.1
        y, x = mm.euler(q1a,m.e,2,10,0.1)
        printing(x,y)
	
with open('q1a_p05.txt', "r+") as f:#for dx=0.05
	y, x = mm.euler(q1a,m.e,2,10,0.05)
	printing(x,y)

with open('q1a_p01.txt', "r+") as f:#for dx=0.01
	y, x = mm.euler(q1a,m.e,2,10,0.01)
	printing(x,y)
	
#Q1(b)----dy/dx=6-2*y/x	
def q1b(y,x):
	f = 6 - 2*y/x
	return f	
with open('q1b_p5.txt', "r+") as f:#for dx=0.5
	y, x = mm.euler(q1b,1,3,10,0.5)
	printing(x,y)

with open('q1b_p1.txt', "r+") as f:#for dx=0.1
	y, x = mm.euler(q1b,1,3,10,0.1)
	printing(x,y)

with open('q1b_p05.txt', "r+") as f:#for dx=0.05
	y, x = mm.euler(q1b,1,3,10,0.05)
	printing(x,y)

with open('q1b_p01.txt', "r+") as f:#for dx=0.01
	y, x = mm.euler(q1b,1,3,10,0.01)
	printing(x,y)

#Q2----by using rk4(2nd order ODE)
def dvdx(y, v, x):#y''+ y'=1-x and taking dy/dx=v
	f = 1-x-v#y''=1-x-v
	return f

with open('q2forh=0.1.txt', "r+") as f:#for dx=0.1
	v, y, x = mm.rk4(dvdx,2,1,0,0.1,-5,5)
	printing(x,y)
	
with open('q2forh=0.5.txt', "r+") as f:#for dx=0.5
	v, y, x = mm.rk4(dvdx,2,1,0,0.5,-5,5)
	printing(x,y)
with open('q2forh=0.05.txt', "r+") as f:#for dx=0.05
	v, y, x = mm.rk4(dvdx,2,1,0,0.05,-5,5)
	printing(x,y)
with open('q2forh=0.01.txt', "r+") as f:#for dx=0.01
	v, y, x = mm.rk4(dvdx,2,1,0,0.01,-5,5)
	printing(x,y)

#Q3---by using boundary value problem	
def dvdx3(y,v,x):#y''=y'+1 and taking dy/dx=v
	f = 1+y
	return f
	
y=input("Give a guess of dy/dx at lower boundary: ")
try:
	z=float(y)
	#given y(0)=1, y(1)=2(e-1)
	#returns x = list consisting all the x between the 2 boundaries, v is the list consisting dy/dx correspondinig to the x list and similiarly list y consisting the y values.
	with open('q3.txt', "r+") as f:#for dx=0.02
		v, y, x=mm.shooting(dvdx3, 0, 1, 1, 2*(m.e-1), z, 0.02 )
		printing(x,y)
	print("Resulting y(b) =",y[-1])

except ValueError:
	print('The input value is not a real number')
	
'''
Output1-----
Give a guess of dy/dx at lower boundary: 10
Resulting y(b) = 3.4365636569180897

Output2-----
Give a guess of dy/dx at lower boundary: z
The input value is not a real number
'''

