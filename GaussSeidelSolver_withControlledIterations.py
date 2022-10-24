x_values = [];
y_values = [];
z_values = [];
iterations = [];
def gauss_seidel_solver(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3,e,n):
    x1 = 0;
    y1 = 0;
    z1 = 0;
    x = 0;
    y = 0;
    z = 0;
    global x_values;
    global y_values;
    global z_values;
    global iterations;
    if (a1 > b1 + c1 and b2 > a2 + c2 and c3 > a3 + b3):
        for i in range(1,n + 1):
            print("---------------------------Iteration No. ",i," ----------------------------")
            x1 = (1/a1)*(d1 - b1*y1 - c1*z1)
            y1 = (1/b2)*(d2 - a2*x1 - c2*z1)
            z1 = (1/c3)*(d3 - a3*x1 - b3*y1)
            if abs(x - x1) < e and abs(y - y1) < e and abs(z - z1) < e:
                print("Solution has converged!")
                break
            else:
                print("The value for x1 is: ",x1)
                print("The value for y1 is: ",y1)
                print("The value for z1 is: ",z1)
            x = x1
            y = y1
            z = z1
            x_values.append(x1)
            y_values.append(y1)
            z_values.append(z1)
            iterations.append(i)
        print("The System of equations has been solved!\n")
        print("The value for x is: ", round(x1,2))
        print("The value for y is: ", round(y1,2))
        print("The value for z is: ", round(z1,2),"\n\n"
        )   
    else:
        print("The given system of equations are not strongly diagonally dominant, which ensures the divergence of approximations.")

a1 = float(input("Enter the value of a1: "))
b1 = float(input("Enter the value of b1: "))
c1 = float(input("Enter the value of c1: "))
d1 = float(input("Enter the value of d1: "))
a2 = float(input("Enter the value of a2: "))
b2 = float(input("Enter the value of b2: "))
c2 = float(input("Enter the value of c2: "))
d2 = float(input("Enter the value of d2: "))
a3 = float(input("Enter the value of a3: "))
b3 = float(input("Enter the value of b3: "))
c3 = float(input("Enter the value of c3: "))
d3 = float(input("Enter the value of d3: "))
e = float(input("Enter the value of tolerable error(e): "))
n = int(input("Enter the value of n iterations: "))
gauss_seidel_solver(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3,e,n)