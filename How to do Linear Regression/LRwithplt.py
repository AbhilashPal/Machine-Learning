from numpy import *
import matplotlib.pyplot as plt
import time

def compute_error_for_given_points(b,m,points):
    totalError = 0
    for i in range(len(points)):
            x = points[i,0]
            y = points[i,1]
            totalError+= (y - (m*x+b))**2
    totalError/=float(len(points))
    return totalError

def step_gradient(b_current,m_current,points, learning_rate):
    #gradient descent
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
            x = points[i,0]
            y = points[i,1]
            b_gradient += -(2/N)*(y - ((m_current*x)+b_current))
            m_gradient += -(2/N)*x*(y - ((m_current*x)+b_current))
    new_b = b_current - (learning_rate)*b_gradient
    new_m = m_current - (learning_rate)*m_gradient
    return [new_b,new_m]


def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
            [b, m] = step_gradient(b,m,array(points),learning_rate)
    return [b,m]

def predict(x_values,b,m):
    y_values = []
    for i in x_values:
        y_values.append(m*i+b)
    return y_values
def dot():
    print ".",
    time.sleep(1)
    print ".",
    time.sleep(1)
    print ".",
    time.sleep(1)
def run():
    points = genfromtxt('data.csv',delimiter=',')
    x_values = points[0:,0]
    y_values = points[0:,1]
    plt.rcParams["figure.figsize"] = (50,20)
    fig, ax = plt.subplots()
    plt.scatter(x_values, y_values)
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.xlabel("------X values----->")
    plt.ylabel("------Y values----->")

    

    #hyperparameters
    learning_rate = 0.0001
    # slope formula : y = mx+b
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b,m] = gradient_descent_runner(points, initial_b, initial_m,learning_rate,num_iterations)
    print "Gradient Descent fitting Best Fit Solution",
    dot()
    print "\n----------------------- y = mx + b ---------------------------- "
    print "b Value : ",b
    print "m Value : ",m
    predictedy = predict(x_values,b,m)
    plt.plot(x_values,predictedy,label = "Line of Best Fit")
    plt.legend()
    print "Plotting Graph for given Linear Dataset.",
    dot()
    plt.show()

if __name__ == '__main__':
    run()
