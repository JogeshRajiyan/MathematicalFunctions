def find_dy(y):
    dy_values = [];
    i = 0;
    while i < len(y) - 1:
        dy = y[i + 1] - y[i]
        dy_values.append(dy)
        i += 1
    return dy_values

dy_global = [];
def list_dy(y):
    global dy_global;
    while len(y) > 1:
        dy_global.append(find_dy(y))
        return list_dy(find_dy(y))
    return dy_global

def retrieve_dy(y):
    dy_global.insert(1,y)
    l = list(list_dy(y))
    print("Successive dy values for given y values: ",l[1:])
    return [item[-1] for item in l]

def calculate_u(u,n):
    local_var = u;
    for i in range(1,n):
        local_var = local_var*(u + i)
    return local_var

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


def backward_difference(x,y,to_find):
    print(x)
    print(y)
    dy_list = list(retrieve_dy(y))
    n = len(dy_list)
    u = (to_find - x[n - 1])/(x[1] - x[0])
    sum_dy = dy_list[0]
    for i in range(1,n):
        sum_dy = sum_dy + (calculate_u(u,i)*dy_list[i])/factorial(i)
    print("The required value for y is: ",sum_dy)
    
x = list(eval(input("Enter the values of x(comma separated): ")))
y = list(eval(input("Enter the values of y(comma separated): ")))
to_find = int(input("Enter the value of x for which value of y has to be found: "))
backward_difference(x,y,to_find)