import matplotlib.pyplot as plt
import numpy as np

def function():
    function = input("Enter a value for the function: ")
    try:
        x = np.linspace(-10, 10, 1000)  # range of values x
        y = eval(function)
        plt.figure(figsize=(8, 6))  # size
        plt.plot(x, y)  # plotting a function
        plt.title('Graph of a function: ' + function)
        plt.xlabel('x')  # axis x
        plt.ylabel('y')  # axis y
        plt.grid(True) 
        plt.show()  # displaying a graph of a function
    except Exception as e:
        print("Error:", e)
        print("Please enter a valid value.")

function()
