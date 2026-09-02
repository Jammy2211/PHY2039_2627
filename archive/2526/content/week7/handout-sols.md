**Solutions**

```python
import numpy as np

def midpoint(f,a,b,n):
    """
    Integral of f(x) using n points (n-1 rectangles) in the range [a,b]
    """
    I = 0
    x = np.linspace(a,b,n)
    for j in range(n-1):
        I += (x[j+1]-x[j])*f((x[j+1]+x[j])/2)
    return I

I = midpoint(lambda x: x**2,0,5,10)
print(I)

def trapezoid(f,a,b,n):
    """
    Integral of f(x) using n points (n-1 trapezoids) in the range [a,b]
    """
    I = 0
    x = np.linspace(a,b,n)
    for j in range(n-1):
        I += (x[j+1]-x[j])*(f(x[j+1])+f(x[j]))/2
    return I

I = trapezoid(lambda x: x**2,0,5,10)
print(I)

def simpsons(f,a,b,n):
    """
    Integral of f(x) using simpsons rule
    """
    x = np.linspace(a,b,n+1)
    I = f(x[0])+f(x[n])
    for j in range(1,n):
        if j % 2 == 0:
            I += 2*f(x[j])
        else:
            I += 4*f(x[j])
        
    return I*(x[1]-x[0])/3

I = simpsons(lambda x: x**2,0,5,1000)
print(I)
```