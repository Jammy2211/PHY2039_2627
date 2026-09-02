## Plan for today

* Announcements
* Numerical differentiaton
* Numerical integration

---

## Meet the MAS2805 Python team: 

#### Integral team members

<div style="float:left; width: 140px; width: 130px; margin: 10px; margin-bottom: 30px;"> 
<b>Chris</b>
</div>
![Chris](/static/images/staff/chris.jpg){style="float: left; width: 140px; margin: 10px;"}

<div style="clear: both; float:left; width: 140px; width: 130px; margin: 10px"> 
<b>Laura</b>
</div>
![Laura](/static/images/staff/laura.png){style="float: left; width: 140px; margin: 10px;"}


<div style="float:left; width: 140px; width: 130px; margin: 10px"> 
<b>Ryan</b>
</div>
![Ryan](/static/images/staff/ryan.jpg){style="float: left; width: 140px; margin: 10px;"}

<br style="clear: both;">


---

## Announcements

* Office hour 1-2pm

. . .

 * Assignment 1 
    * marks and feedback tomorrow

. . .

 * Assignment 2
    * Released 4pm Monday 30th November
    * Due 4pm Monday 14th December
    * More of a presentation focus

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
<tr style="background: rgba(146,190,50,0.3)">
<td></td>
<td>5: 23rd Nov</td>
<td>Numerical differentiation and integration</td>
<td>Live online Thursday</td>
<td></td>
</tr>
<tr>
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
<td>9: 18th Jan</td>
<td>Assessment</td>
<td></td>
<td>Assessment 3 (24 hours from Mon 4pm)</td>
</tr>
<tr>
<td colspan="5" style="text-align: center; background-color: #CCC;">Semester 2...</td>
</tr>
</table>

----

## Numerical differentiation


---


### Forward-difference method

![](/static/images/week3/finite_forwarddiff.png){width=60%}

$$ \frac{\mathrm{d}f}{\mathrm{d}x} = \frac{f(x+h)-f(x)}{h} + \mathcal{O}(h) $$


----

### Central difference method

![](/static/images/week3/finite_central.png){width=70%}

$$ \frac{\mathrm{d}f}{\mathrm{d}x} = \frac{f(x+h)-f(x-h)}{2h} + \mathcal{O}(h^2)  $$

----

### Right-sided second-order method

![](/static/images/week3/finite_onesided_forward.png){width=70%}

$$ \frac{\mathrm{d}f}{\mathrm{d}x} = \frac{-3f(x_0)+4f(x_1)-f(x_2)}{2h}  + \mathcal{O}(h^2) $$


----

### Left-sided second-order method

![](/static/images/week3/finite_onesided_backward.png){width=70%}


$$ \frac{\mathrm{d}f}{\mathrm{d}x} = \frac{3f(x_n)-4f(x_{n-1})+f(x_{n-2})}{2h}  + \mathcal{O}(h^2) $$


---

## Numerical integration

---

![](/static/images/week5/trapezoid_new.png){width=70%}

In the handout this week we looked at some quadrature rules.

---

![](/static/images/week5/trapezoid_zoom.png){width=70%}

Basic idea: break up the area under a curve into shapes for which we can easily calculate the area.

---

### Creating our own quadrature function

In breakout rooms we'll have a go at coding up the trapezoid method for 

$$ \int_0^{10} x^2 \mathrm{d}x $$

---


## Summary

Next week we move on to numerically solving differential equations.

. . .

![](/static/images/week5/bunny.jpg){width=40%}

. . .

Don't forget - assignment 2 available from Monday!



