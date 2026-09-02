## Plan for today

* Announcements
* Improving our Bisection function 
* The Newton-Raphson Method

---

## Meet the MAS2805 Python team: 

#### *root* ing for you this week

<div style="float:left; width: 140px; width: 130px; margin: 10px; margin-bottom: 30px;"> 
<b>Chris</b>
</div>
![Chris](/static/images/staff/chris.jpg){style="float: left; width: 140px; margin: 10px;"}

<div style="clear: both; float:left; width: 140px; width: 130px; margin: 10px"> 
<b>Laura</b>
</div>
![Laura](/static/images/staff/laura.png){style="float: left; width: 140px; margin: 10px;"}

<div style="float:left; width: 140px; width: 130px; margin: 10px"> 
<b>Jordan</b>
</div>
![Jordan](/static/images/staff/jordan.jpg){style="float: left; width: 140px; margin: 10px;"}



<div style="float:left; width: 140px; width: 130px; margin: 10px"> 
<b>Ryan</b>
</div>
![Ryan](/static/images/staff/ryan.jpg){style="float: left; width: 140px; margin: 10px;"}

<br style="clear: both;">

---

## Announcements

* Office hour Thursday 1-2pm
* Assignment 1 
    * Closes Friday 4pm
    * FAQ
* [Feedback still open](https://forms.ncl.ac.uk/view.php?id=9655705){target="_blank"}


---

## Bisection Method

Let's do some tidying up of last week's code.

* bug fixing
* error handling
* lambda functions
* counting the iterations

----

### The Newton-Raphson Method

![the Newton-Raphson Method](/static/images/week4/newtonraphson1.png){width=65%}


---

### The Method

This is generally quicker than the Bisection Method, but requires a known derivative $f'(x)$.

The Newton-Raphson Method goes like this

* Make an initial guess $x_0$.

* Find the gradient at $f(x_0)$ to locate the intersect of the tangent line with the $x$ axis.

* This point will generally be closer to the root. Call this $x_1$ and repeat.

* Repeat until the value converges.

----

#### Newton-Raphson Method Animation

![Animation of the Newton-Raphson Method](/static/images/week2/newtonrhapson_animation.gif){width=65%}

<small>Image: Wikipedia</small>

---

#### First steps

Let's take a look at the recursion relation in action

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

---

#### Breakout rooms

In breakout rooms we'll take this on to create an awsome Newton-Raphson function to go alongside our Bisection one.

---

## Round up

We've seen now how to code up two algorithms now. In the handout we'll meet a third, the Secant method. 

Good luck with your assessment.

And have a relaxing buffer week!

