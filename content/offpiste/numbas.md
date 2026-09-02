[Click here to open this handout in a new browser tab](#){target="_blank"}

<div class="interlude">
	<p>The material on this page is outside the scope of the module, and is not testable in the assignments or examinations. There is no requirement or expectation to read any of this material: it is presented to provide a selection of interesting things related to the skills and techniques covered in PHY2039.</p>
</div>

<h1><span style="font-size: 25px;">PHY2039 Off-Piste 3:</span><br/>Behind the Scenes of Numbas</h1>

I often get asked how Numbas manages to mark your code automatically, which is a really good question! It's a really good question because it's something I get very excited talking about... I've been working on it with colleagues for the past few years. But also because it links in really well with some of our other activities including control flow / logical operators. And you get to find out more about how your assessment questions are marked.

I've even written you a Numbas question, in which you can write your own question... very surrealist!

## Who develops Numbas

The short answer is my colleague Christian! The longer answer is that it's developed here in the School of MSP by our [award-winning E-Learning Team](https://www.ncl.ac.uk/maths-physics/engagement/digital-learning/){target="_blank"}. 

And it's used all over the World, which is pretty cool.

## Isn't Numbas for maths?

Numbas was (and mostly still is) used for maths, until I started teaching programming. Numbas  marks mathematical expressions/equations and numeric answers as well as things like multiple choice, matrices etc, as you will have seen in your other modules.

Believe it or not, 5 years ago when I took on the two maths computing modules - what was then MAS1801 and MAS2602 - there were no Numbas questions at all. I vividly remember a student ask me "can we have some Numbas practice like our other modules", and the rest is history... there are currently more than 200 questions powering the handout and Test Yourself quizzes, and what I was really interested in is being able to give immediate feedback on your work, rather than you sitting there wondering if what you're doing is correct! So with the help of my clever colleagues, we can now accept code answers in Numbas, mark it and immediately give feedback (and without any dependancy on anything outside of your web browser, but that's a longer story). 

## So how does it work?

Well, consider the following... I've asked you to create a function called `square` that squares a number and here's your answer...

```python
def square(x)
   return x**2
```

To check whether your function works, I can run what are called "unit tests" on your code. These are tests that are either `True` or `False`. For example:

```python
square(2)==4
```
```output
True
```

I would normally add more tests than this, but based on that evidence, the function was correct! So you can imagine bits of code like

```python
if square(2)==4:
    # Add mark to total or whatever
```

We could also run other tests, which are a bit tricker, for example:

```python
'square' in locals()
```
```output
True
```

That object `locals()` basically contains all of the currently defined variables and other "stuff", so this basically asks, is there a thing called `square` defined.

Or even better

```python
callable(square)
```
```output
True
```

Which basically asks if there is something "callable" (i.e. a function) called "square".

These are getting a bit complicated, but hopefully you can see how a combination of these different tests gives the opportunity to give feedback on the exercises in the handout and Test Yourself quizzes.

<div class="exercise" markdown=true>

### Have a go

This might be a bit buggy, but here's a little thing I created where you can "create your own" question and "unit test", before having a go at answering your own question, yourself!

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/131532/write-your-own-programming-question/embed/?token=e66c33df-ff31-444d-b6d5-997889681ee5" data-id="offpiste-numbas" data-cta="Try it out"></numbas-embed>

</div>

### Walk through

And here's me talking you through how to use it and about a couple of functions that I use a lot (`np.isclose` and `np.allclose`). Enjoy!

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=1cec3b4b-b305-4b0d-a847-af47007cd233&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=false&interactivity=all" style="border: 1px solid #464646;height: 405px; width: 720px;" allowfullscreen allow="autoplay"></iframe>

<style>

.numbas_container iframe.numbas_iframe {
    height: 1100px;
}

</style>
