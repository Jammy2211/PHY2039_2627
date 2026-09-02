[Click here to open this handout in a new browser tab](#){target="_blank"}

### Example: Tyne Bridge

Polynomials are used out there in the big wide world for all sorts of things, including designing things like churches, bridges and rollercoasters. 

The Tyne Bridge is an example of a parabolic bridge. Without going to some significant effort I can obtain only three data points to map out its shape. From Wikipedia, I see that its arch span is 162m and its maximum height 55m. I therefore propose the below 3 data points, letting $x$ be the horizontal position, $y$ the height of the arch and defining the base of the bridge on one side to be at $(0,0)$. Then,

x    |  y  
-----|-----  
0    |  0   
81   |  55
162  |  0


We don't actually need a computer for this one; you can calculate the equation for the height of the arch on pen and paper from the standard form of a parabola (which I've done for you), to find that the "Tyne Bridge Equation" (in the coordinate system that we have defined) is 

$$y = -\frac{55}{81^2}\left(x-81\right)^2+55 \quad\text{(*)}$$

Since we know that it is parabolic, i.e. its shape is based on a quadratic equation $ax^2+bx+c$, the fact that we can fit the three data points precisely will not be surprising in this case. And it won't give us any information that we didn't already know. However it does give us some nice practice in using `polyfit` and `polyval`

So let's use polyfit again:

```python

import numpy as np
# data points
x = [0,81,162];
y = [0,55,0];

# Fit using polyfit and polyval
p = np.polyfit(x,y,2)

print(p)
```
 which gives the output

 ```output
[-8.38286847e-03  1.35802469e+00 -9.32374915e-15]
 ```

In other words, polyfit suggests that the equation of the Tyne Bridge is $y \approx -0.0084x^2+1.358x$. I note that equation (*) above expands to 

$$ y = -\frac{55}{81^2}x^2+\frac{110}{81}x$$

which is consistent with the floating point numbers returned by `polyfit`. 

For a final check, I'm going to do some trickery to make sure that the axis grid has an equal ratio, which will allow us to see if our fit looks visually quite sensible.

```python
plt.axes().set_aspect('equal')
```

and do some prettifying to obtain...

![The Tyne Bridge curve](/static/images/week2/tynebridge.png)


It sort of looks about right. For completeness I'm going to check our working with a real picture (taken as straight-on as I could find!)

![The Tyne Bridge curve with background image](/static/images/week2/tynebridge-fit.png)

Not bad at all!
