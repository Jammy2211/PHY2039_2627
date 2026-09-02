## Plan for today

* Announcements
* Recap
* Bisection Method

---

## Meet the MAS2805 Python team: 

#### AKA "The Array Team"

<div style="float:left; width: 140px; width: 130px; margin: 10px; margin-bottom: 30px;"> 
<b>Chris</b>
</div>
![Chris](/static/images/staff/chris.jpg){style="float: left; width: 140px; margin: 10px;"}

. . .

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

* Office hours
* Assignment 1 
    * Opens this Friday
    * via the Numbas app 
    * some work will be uploaded in addition
    * Based on the content in weeks 1-3
* [Feedback](https://forms.ncl.ac.uk/view.php?id=9655705){target="_blank"}



---

## Recap - For, if and while


```runnable lang="python"


```

---

## Recap - Functions

```runnable lang="python"


```

---

## Function example

Write a function that returns the **sign** of a variable.


```runnable lang="python"


```


---

## The Bisection Method

The bisection method homes-in on a root of a function f(x) using systematic trial and error:

* Identify lower and upper bounds $[x_l, x_h]$, such that $f(x_l)<0$ and $f(x_{h})>0$, The root $x_*$ is therefore in between: $x_l < x_* < x_h$.

* Evaluate the function at the midpoint of the bound (is it positive or negative?) to eliminate half of the range.

* Repeat until $x_h - x_l$ is sufficiently small.

---

In the breakout rooms we'll look at how we can make this more sophisticated with the tools we've looked at this week (functions, if statements and for loops)


---

## Round-up

Next week... two more methods for root finding...

* The Secant Method
* The Newton-Raphson Method
