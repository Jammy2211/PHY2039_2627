<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Scientific computation with Python

---

## Contact details

Dr James Nightingale

Email me via [James.Nightingale@newcastle.ac.uk](mailto:James.Nightingale@newcastle.ac.uk)

My office is Herschel Annex 2.12 (NOT the main building, the annex opposite it, door has "Dr Colin Woods" written on it currently)

Office hours are After Monday's Lecture / Workshop, 11am - 1pm, however please don't hesitate to contact me to arrange a meeting via email, either in-person or via Zoom. 

---

### Lecture notes and materials

* The lectures for PHY2039 are recorded and will be posted to Canvas.

* All slides and other lecture materials will also be posted to Canvas.

* It's therefore not necessary for you to make extensive notes during lectures. 

* However, in future lectures you may wish to follow along by coding on a personal laptop.

---

### Today

This lecture is split into two halves:

**1) Some administration and motivation**

Structure of the module and some examples of the benefits of programming skills

**2) Week 1 content overview**

Description of what's covered in this week's practical session.

---

<div class="title-slide" style="background-image: url('../../static/images/intro/module.png');">
    <h2>Module introduction</h2>
</div>

---

### Module content


![Python logo](/static/images/intro/python-logo.png){style="width: 14%"}

This module covers the programming language **Python** and its use in tackling a variety of numerical methods, useful in particular to applied mathematics and physics.

The module builds on the Python course you completed in your first year.

The first few weeks are a recap, and by the second or third week it won't make much difference how much Python you have studied previously.

---

### Timetable

One lecture and one practical sesssion each week.

<table class="table"  style="font-size: 0.8em;">
	<tr><th>Monday</th><td>Lecture </td><td>10:00-11:00</td><td>See Timetable due to Variation</td></tr>
    <tr><th>Friday</th><td>Practical</td><td>11:00-13:00</td><td>KGVI.IT Service Cluster (LAWN.PC 2.33), (KGVI University Map ref:19)</td></tr>
</table>

---


## Full timetable

<div style="height: 500px; overflow-y: scroll;">
<table style="line-height: 1.05em; font-size: 0.75em;">
    <tbody>
        <tr >
            <th>Week No</th>
            <th>Week Begin</th>
            <th>Topic</th>
            <th>Assessment</th>
        </tr>
        <tr >
            <td>1</td>
            <td>22nd Sept</td>
            <td>Foundations + Curve Fitting I</td>
            <td></td>
        </tr>
        <tr >
            <td>2</td>
            <td>29th Sept</td>
            <td>Curve Fitting II</td>
            <td>Assessment 1 opens Friday 16:00</td>
        </tr>
        <tr >
            <td>3</td>
            <td>6th Oct</td>
            <td>Matrices and Linear Algebra</td>
            <td></td>
        </tr>
        <tr >
            <td>4</td>
            <td>13th Oct</td>
            <td>Algorithms + Root Finding I</td>
            <td>Assessment 1 due Friday 16:00</td>
        </tr>
        <tr >
            <td>5</td>
            <td>20th Oct</td>
            <td>Root Finding II</td>
            <td></td>
        </tr>
        <tr >
            <td>6</td>
            <td>27th Oct</td>
            <td>Advanced Plotting</td>
            <td>Assessment 2 opens Friday 16:00</td>
        </tr>
        <tr >
            <td style="background-color: #ced4d9; text-align: center;" colspan="4"><em><strong>Enrichment week</strong></em></td>
        </tr>
        <tr >
            <td>7</td>
            <td>10th Nov</td>
            <td>Numerical differentiation and integration</td>
            <td></td>
        </tr>
        <tr >
            <td>8</td>
            <td>17th Nov</td>
            <td>Differential equations I</td>
            <td>Assessment 2 due Friday 16:00</td>
        </tr>
        <tr >
            <td>9</td>
            <td>24th Nov</td>
            <td>Differential equations II</td>
            <td></td>
        </tr>
        <tr >
            <td>10</td>
            <td>1st Dec</td>
            <td>Looking forward</td>
            <td></td>
        </tr>
        <tr >
            <td>11</td>
            <td>8th Dec</td>
            <td>Revision</td>
            <td></td>
        </tr>
        <tr >
            <td style="background-color: #ced4d9; text-align: center;" colspan="5"><em><strong>Christmas break</strong></em></td>
        </tr>
    </tbody>
</table>
</div>


---

### Assessment

- Assessment 1: 5%
- Assessment 2: 15%
- End of module exam: 80%


---


### Canvas page

The module Canvas page is organised into a dashboard for each week.

. . .

Each week contains:

* ReCap recording
* Lecture slides
* The virtual handout for the practical session, containing notes and exercises 
* Test yourself quiz

---

### Canvas overview

[![PHY2039 on Canvas](/static/images/intro/canvas.png){style="height:450px; border: 2px solid #AAA !important;"}](https://ncl.instructure.com/courses/53586){target="_blank"}


---


## Student voice

School modules have evolved over a number of years thanks to the feedback and input of students. 

See our [Student voice page](https://ncl.instructure.com/courses/59162/pages/student-voice){target="_blank"} for more information.

* You can send feedback to me any time via email or anonymously via the suggestions form (linked on the above page)
* Survey will be released around Week 4
* End of stage student evaluation at the end of the semester

---

### Suggestions when working on PHY2039

**There are no stupid questions:** please don't hesitate to ask questions during or after lectures and practical sessions, by email, by visiting my office. Questions of any type and at any level are welcome:

* Tech support e.g. 'my cursor has disappeared'
* Technical e.g. 'my code won't compile' or 'I get this error'
* Abstract e.g. 'can I accomplish this task with a shorter program?'
* Outlook e.g. 'what will I need these programming skills for?'

Also be prepared to have a go at diagnosing problems with your code. Code almost never works first time, and debugging a crucial skill.

---

<div class="title-slide" style="background-image: url('../../static/images/intro/screensaver.gif');">
    <h2>PHY2039 off-piste</h2>
</div>

---

### Off-piste section

The module Canvas page contains an Off-piste section: these are **optional** and **not testable** extra activities that use some of the skills developed in PHY2039.

There is no expectation or requirement that you look at this material, but you may find it interesting.

---

## Motivation

---

<div class="title-slide" style="background-image: url('../../static/images/intro/wmap.png');">
    <h3>Research </h3>
</div>

---

The vast majority of modern mathematics and physics research involves programming to some degree.

A good way to get some examples of this is by asking lecturers in your other modules, or the postgraduate demonstrators in the PHY2039 practical sessions: how do they use programming in their research work?

---

<div class="title-slide" style="background-image: none;">
    <h3>Programming in your course </h3>
</div>

---

We could spend hours discussing the many ways in which programming will be useful to you as you progress through your degree.

We'll suffice ourselves by making the following observation:

> Computer implementation of mathematics often has a low price and a (very) high payoff

---

### AI and Large Language Models

Tools like ChatGPT are now extremely good at coding — they could pass this module’s exam with a first-class mark.

They are an excellent learning aid: you are strongly encouraged to use them to help you understand and practice coding.

But beware: it’s easy to become over-reliant and use them in ways that stop you from actually learning the course material yourself.

---

### AI And Exams

Assessment 1 & 2: You may use AI tools (e.g. ChatGPT).

Exam: AI tools will be blocked and not available.

Advice: At the end of each workshop, spend ~30 minutes doing the exercises without AI to prepare for the exam.

---

<div class="title-slide" style="background-image: url('../../static/images/intro/swing.jpg');">
    <h2>An example</h2>
</div>


---

### Simple pendulum 

Consider the following differential equation:

$$ 
\frac{d^2\theta}{dt^2}+\theta =0 
$$

<div style="display: grid; grid-template-columns: repeat(2, 1fr); grid-gap: 0 60px;">
    <div class="item" markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/smallangle.png" style="height:300px;"/>
    </div>
    <div class="item"  markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/smallangle.gif" style="height:290px;"/>
    </div>
</div>

Pen and paper difficulty: 🌶 &nbsp;&nbsp;&nbsp;Computer difficulty: 🌶🌶

---

### Nonlinear pendulum

$$ 
\frac{d^2\theta}{dt^2}+\sin \left( \theta \right) =0 
$$

<div style="display: grid; grid-template-columns: repeat(2, 1fr); grid-gap: 0 60px;">
    <div class="item" markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/notsmallangle.png" style="height:300px;"/>
    </div>
    <div class="item"  markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/notsmallangle.gif" style="height:290px;"/>
    </div>
</div>



Pen and paper difficulty: 🌶🌶🌶 &nbsp;&nbsp;&nbsp;Computer difficulty: 🌶🌶


---

### Damped nonlinear pendulum 

$$ 
\frac{d^2\theta}{dt^2}+c\frac {d\theta }{dt} + \sin \theta =0 
$$

<div style="display: grid; grid-template-columns: repeat(2, 1fr); grid-gap: 0 60px;">
    <div class="item" markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/damped.png" style="height:300px;"/>
    </div>
    <div class="item"  markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/damped.gif" style="height:290px;"/>
    </div>
</div>




Pen and paper difficulty: 🌶🌶🌶🌶🌶 &nbsp;&nbsp;&nbsp;Computer difficulty: 🌶🌶🌶

---

### Driven damped nonlinear pendulum 

$$ 
\frac{d^2\theta}{dt^2}+c\frac {d\theta }{dt} + \sin \theta = a\cos(bt)  
$$

<div style="display: grid; grid-template-columns: repeat(2, 1fr); grid-gap: 0 60px;">
    <div class="item" markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/dampeddriven.png" style="height:300px;"/>
    </div>
    <div class="item"  markdown=true>
        <img alt="A swing" src="../../static/images/intro/pendulum/dampeddriven.gif" style="height:290px;"/>
    </div>
</div>


Pen and paper difficulty: &infin; &nbsp;&nbsp;&nbsp;Computer difficulty: 🌶🌶🌶


---

<div class="title-slide" style="background-image: none;">
    <h2>Outside academia</h2>
</div>

---

As with the world of research, many careers pursued by mathematics and physics graduates involve a programming element.

E.g. an increasing number of undergraduates go on to MSc courses and internships in data science or analytics.

Newcastle graduates are in an excellent position to succeed in these roles.




