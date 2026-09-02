## Plan for today

* Announcements
* Breakout rooms
* Plotting!

---

## Meet the MAS2805 Python team: 

#### AKA "PG Tips"

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
    * via the Numbas app 
    * some work will be uploaded in addition
    * Opens 4pm Friday 6th November, closes 6pm Friday 13th November
    * Based on the content in weeks 1-3
* Feedback

---

## Breakout rooms

Today we'll be in much smaller breakout rooms. Say a quick hello!

. . .

If you need help, click on *Ask for Help*. Note it may take us a few minutes to get to you.

. . .

Once in the breakout rooms you can share screen and the chat is for your room only. Try to work together.


---

## This week

A very quick recap on `polyfit` and `polyval`.


---

## Problem for today


A scientist measures the weight of an unstable isotope over a number of days and records the results.


Day       |   1  |  2   |  3   |  4  |  5  |  6  |  7  |  8  |  9  |  10
----------|------|------|------|-----|-----|-----|-----|-----|-----|-----
Weight(g) | 24.3 | 18.1 | 11.7 | 7.3 | 4.9 | 2.9 | 2.6 | 1.5 | 1.0 | 0.5


. . .


(a) Set up some variables and make a plot of the data. Investigate the following Matplotlib functions. Which one gives a straight line?

   * `plt.plot()`
   * `plt.semilogx()`
   * `plt.semilogy()`
   * `plt.loglog()`

Any thoughts on what sort of function to fit to the data?

---

We're going to fit an exponential function of the form $y=a\exp(bx)$.


(b) Transform the equation into a linear polynomial by making a suitable change of variables in order to use `polyfit`, to find $a$ and $b$.

. . .

(c) Illustrate the fit with some plots.


---

## Round-up

* Some final thoughts on the exercise
* Looking ahead to next week...