import math as m
import mymodule as mm
def q1a(y,x):
	f = y*m.log(y)/x
	return f
def q1b(y,x):
	f = 6 - 2*y/x
	return f

with open('q1a_p5.txt', "r+") as f:
	y, x = mm.euler(q1a,m.e,2,10,0.5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1a_p1.txt', "r+") as f:
	y, x = mm.euler(q1a,m.e,2,10,0.1)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1a_p05.txt', "r+") as f:
	y, x = mm.euler(q1a,m.e,2,10,0.05)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1a_p01.txt', "r+") as f:
	y, x = mm.euler(q1a,m.e,2,10,0.01)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
	
with open('q1b_p5.txt', "r+") as f:
	y, x = mm.euler(q1b,1,3,10,0.5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1b_p1.txt', "r+") as f:
	y, x = mm.euler(q1b,1,3,10,0.1)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1b_p05.txt', "r+") as f:
	y, x = mm.euler(q1b,1,3,10,0.05)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q1b_p01.txt', "r+") as f:
	y, x = mm.euler(q1b,1,3,10,0.01)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
def dvdx(y, v, x):
	f = 1-x-v
	return f

with open('q2forh=0.1.txt', "r+") as f:
	v, y, x = mm.rk4(dvdx,2,1,0,0.1,-5,5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
	
with open('q2forh=0.5.txt', "r+") as f:
	v, y, x = mm.rk4(dvdx,2,1,0,0.5,-5,5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q2forh=0.05.txt', "r+") as f:
	v, y, x = mm.rk4(dvdx,2,1,0,0.05,-5,5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()
with open('q2forh=0.01.txt', "r+") as f:
	v, y, x = mm.rk4(dvdx,2,1,0,0.01,-5,5)
	for i in range(len(x)):
		f.write(str(x[i]))
		f.write("	")
		f.write(str(y[i]))
		f.write("\n")
	f.close()

		
		
