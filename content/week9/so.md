## Plan for today

* More solving differential equations!

---

## Announcements

* Assignment 2 closes Monday 14th December 4pm
* Mock test before Christmas

---

##  &nbsp; {: data-background="/static/images/MathSocMurderMystery1.jpg"}

---

##  &nbsp; {: data-background="/static/images/MathSocMurderMystery2.jpg"}

---

## Where are we?

<table style="font-size: 0.7em;">
<tr>
<th></th>
<th>Week Begin</th>
<th>Topic</th>
<th>Scheduled</th>
<th>Assessment</th>
</tr>
<tr>
<td></td>
<td>6: 30th Nov</td>
<td>Differential equations I</td>
<td>Live online Thursday</td>
<td>Assessment 2 released (Mon 4pm)</td>
</tr>
<tr style="background: rgba(146,190,50,0.3)">
<td></td>
<td>7: 7th Dec</td>
<td>Differential equations II</td>
<td>live online Tuesday</td>
<td></td>
</tr>
<tr>
<td></td>
<td>8: 14th Dec</td>
<td>Differential equations III</td>
<td>Live online Thursday</td>
<td>Assessment 2 Due (Mon 4pm)</td>
</tr>
<tr>
<td colspan="5" style="text-align: center; background-color: #CCC;">Christmas vacation</td>
</tr>
<tr>
<td></td>
<td>9: 11th Jan</td>
<td>Revision</td>
<td>Live online Thursday</td>
<td></td>
</tr>
<tr>
<td></td>
<td>10: 18th Jan</td>
<td>Assessment</td>
<td></td>
<td>Assessment 3 (24 hours from Mon 4pm)</td>
</tr>
<tr>
<td colspan="5" style="text-align: center; background-color: #CCC;">Semester 2...</td>
</tr>
</table>

[View full timetable](https://ncl.instructure.com/courses/32310/pages/timetable)



----

## Euler Method

The method we're going to use today is the Euler Method to solve initial value problems e.g.

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$


---

## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation0.png){width=70%}

What's our goal?



## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation1.png){width=70%}

We want to know what the function $y(t)$ looks like.



## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation0.png){width=70%}

What do we know?



## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation2.png){width=70%}

We know that $y(0)=5$



## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation3.png){width=70%}

And $\frac{\mathrm{d}y}{\mathrm{d}t}(0)=-\frac{5}{2}$


## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation4.png){width=70%}

Suppose we use this to estimate $y$ at $t = 1$...

## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation5.png){width=70%}

$y(1) = 5 -\left(\frac{5}{2}h\right)$, where $h$ is the distance between $t$ values


## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation6.png){width=70%}

So $y(1) = \frac{5}{2}$



## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation7.png){width=70%}

Now we have $\frac{\mathrm{d}y}{\mathrm{d}t}=-\frac{5}{4}$
 

## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation8.png){width=70%}

And so on...
 

## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation9.png){width=70%}

And so on...

## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation10.png){width=70%}

And so on...


## &nbsp; {: data-transition="none"}

Solving $\displaystyle \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5$

![](/static/images/week6/explanation11.png){width=70%}

And so on...


----

![](/static/images/week6/euler.gif){width=100%}

----

How does this numerical (approximate) solution compare to the exact solution of the equation solved "by hand"?

$$ y(t) = 5e^{-t/2} $$

---

## &nbsp; {: data-transition="none"}


$h = 1$

![](/static/images/week6/h1.png){width=90%}


## &nbsp; {: data-transition="none"}


$h = 0.5$

![](/static/images/week6/h0p5.png){width=90%}


----

![](/static/images/week6/euler_animation.gif){width=100%}


----

In equation form, for an equation

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = f(t,y). $$

The Euler Method is

$$ \displaystyle y_{n+1} = y_{n} + h f(t_n,y_n). $$

---

In breakout rooms we'll have a go at coding up the Euler method to solve this differential equation...

$$ \frac{\mathrm{d}x}{\mathrm{d}t}=\frac{1}{2}x(1-x)\text{.}$$

---

## Logistic equation


This apparently quite pedestrian differential equation is known as the logistic equation and is used for population modelling.

$$ \frac{\mathrm{d}x}{\mathrm{d}t}=rx(1-x)\text{.}$$

$r$ represents the growth rate.

. . .

It is the continuous form of the so-called logistic map, a model of population dynamics with some fascinating (chaotic) behaviour that we won't get into here (Googe it)!

---

### Solutions to the logistic equation

![](/static/images/week6/logistic_family.png){width=80%}

---

## Runge-Kutta Methods

Euler's method can be improved upon by more carefully advancing from a known $y_n$ to $y_{n+1}$. One way to do this is to first make a trial half-step forwards, from $t_0$ to $t_0 + h/2$, find $y(t_0 + h/2)$ and use this to move forward to $y(t_1)$.

---

![](/static/images/week7/rk4.png){width=70%}

---

The "Classic Runge-Kutta Method" (sometimes just Runge-Kutte Method or RK4) solves

\[ \frac{\mathrm{d}y}{\mathrm{d}t}=f(t,y) ,\quad y(0) = y_0\] 

using the iterative formula

\[ y_{n+1}=y_{n}+\frac{1}{6}h\left(k_1+2k_2+2k_3+k_4\right), \]

---

where 

\[
\begin{align}
k_1 &= f(t_n,y_n), \\[0.7em]
k_2 &= f\left(t_n+\frac{h}{2},y_n+h\frac{k_1}{2}\right), \\[0.7em]
k_3 &= f\left(t_n+\frac{h}{2},y_n+h\frac{k_2}{2}\right), \\[0.7em]
k_4 &= f\left(t_n+h,y_n+hk_3\right).
\end{align}
\]

---

![](/static/images/week7/runge-kutta-1.png){width=80%}

---

let's have a go at coding this up.

---

## Summary

That's all for today. Lots of practice this week coding up the algorithms and next week we'll look a bit further into comparing the two.

Don't forget assignment 2, due Monday 4pm.
