# Hand-in 3 solution 

```python
import numpy as np
import matplotlib.pyplot as plt

def bhaskara(x):
    """
    returns the Bhaskara approximation for sin(x)
    """
    try:
        return (16*x*(np.pi-x))/(5*np.pi**2-4*x*(np.pi-x))
    except TypeError:
        print("Input should be numeric")


# Use the function 
x = np.linspace(-2*np.pi,3*np.pi,100)
y = np.sin(x)
y2 = bhaskara(x)

# Make a plot
plt.plot(x,y,x,y2)
plt.xlabel('x')
plt.legend(['sin(x)','Bhaskara approximation'])
plt.title('The Bhaskara approximation to sin(x)')
```