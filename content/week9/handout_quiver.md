

## Plotting direction fields with `quiver`

*[Link to the MATLAB documentation for quiver](https://uk.mathworks.com/help/matlab/ref/quiver.html){target="_blank"}*


Consider the ODE

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2} $$

Numerical methods to solve ODEs are based on the idea that the solution close to a known point $y(t_0)$ can be estimated by using the tangent line to $y(t)$ at $t_0$. Since the right hand side gives the derivative of $y(t)$, we can apply this idea to plot the *direction field* of an ODE. This will show the trajectories of solutions. 

Constructing a direction field by hand is straightforward but it is also time-consuming and repetitive: exactly the sort of problem a computer is good for! 

The following figure shows the direction field for the above ODE, along with two solution curves for $y(0)=5$ and $y(0)=-5$ .

![](/static/images/week4/quiverode.png){width=90%}

The MATLAB plotting function `quiver` is used to plot these arrows. 

Before we do that, a 2D grid of points needs to be defined. This can be done as follows:

```octave
t = 0:10
y = -10:10
[T,Y] = meshgrid(t,y)
```

I've chosen those ranges and step-sizes fairly arbitrarily, feel free to play around with them.

Now we can create the vector components: we can choose $\mathrm{d}t = 1$ and then from the ODE above, $\mathrm{d}y = -y/2$:

```octave
DT = ones(size(T))     % Creates a matrix of 1s the same size as T
DY = -Y./2

quiver(T,Y,DT,DY)
```

If you don't recall what the function `ones` does, then try out, for example

```octave
ones(1,10)
ones(5)
```

*[Link to the MATLAB documentation for ones](https://uk.mathworks.com/help/matlab/ref/ones.html){target="_blank"}*


How did I add the two curves? Well that's the next part... 

### Exercise 4.1 {: .exercise}

Plot the direction field for 

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = \frac{1}{5}\sqrt{y} + \frac{1}{2}t^2 $$

in the domain $-2 \le t \le 2$, $0 \le y \le 3$, to get something like the below:

![](/static/images/week4/ex4p1.png){width=90%}
