## Topics

 * Announcements
 * Differential equations

 ---

## Announcements

 * Assignment 2
    * Available now
    * Due 4pm Monday 14th December

. . .

 * Assignment 3 format and date
    * 24 hour assessment opening 4pm Monday 18th January

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
<td colspan="5" style="text-align: center; background-color: #CCC;">Enrichment week</td>
</tr>
<tr>
<td></td>
<td>5: 23rd Nov</td>
<td>Numerical differentiation and integration</td>
<td>Live online Thursday</td>
<td></td>
</tr>
<tr style="background: rgba(146,190,50,0.3)">
<td></td>
<td>6: 30th Nov</td>
<td>Differential equations I</td>
<td>Live online Thursday</td>
<td>Assessment 2 released (Mon 4pm)</td>
</tr>
<tr>
<td></td>
<td>7: 7th Dec</td>
<td>Differential equations II</td>
<td><s>PiP</s> live online Tuesday</td>
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



---

##  &nbsp; {: data-background="/static/images/MathSocMurderMystery1.jpg"}

---

##  &nbsp; {: data-background="/static/images/MathSocMurderMystery2.jpg"}

---

## Differential equations


* They are vitally important in so many fields, including fluid dynamics, economics, epidemiology, population dynamics...

* They can often be solved "by hand", but complicated ones can often only be solved with the help of a computer.

* We are going to have a go at solving them "numerically" using Python

----


## Solving differential equations with a computer


We'll be solving equations of the form

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$

sometimes called an "initial value problem".


----

We know $y(0)=5$ and $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}t}(0)=-\frac{5}{2}$

![](/static/images/week6/explanation3.png){width=80%}

----

So this can be used to estimate $y$ at some later point

![](/static/images/week6/explanation5.png){width=80%}

$y(1) = 5 -\left(\frac{5}{2}h\right)$, where we've used a distance between $t$ values of $h = 1$


---

## `odeint`

Next week we'll look at the underlying algorithms for solving differential equations with a computer.

This week we look at a function that does the work for us: `odeint`.

---

## First order ODE

Let's start off with a first order ODE:

$$ \frac{\mathrm{d}x}{\mathrm{d}t}=\frac{1}{2}x(1-x)\text{.}$$

---

## Sending parameters to `odeint`


We'll look at this equation in more depth next week. It's usually written as:

$$ \frac{\mathrm{d}x}{\mathrm{d}t}=rx(1-x)\text{.}$$

for parameter `r`. 

. . . 

How do we send that to `odeint`?

---

## Lotka-Volterra equations

System of ODEs:

$$ \frac{\mathrm{d}x}{\mathrm{d}t} =\alpha x-\beta xy, $$

and

$$  \frac{\mathrm{d}y}{\mathrm{d}t}  =\delta xy-\gamma y $$

---

## Lotka-Volterra dynamics

![](/static/images/week6/lotka1.png){width=80%}

---

## Lotka-Volterra phase portrait


![](/static/images/week6/lotka2.png){width=80%}


---

## Summary

Next week we'll look at the algorithms used by a function such as `odeint`.