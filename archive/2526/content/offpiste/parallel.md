[Click here to open this handout in a new browser tab](#){target="_blank"}

<div class="interlude">
    <p>This is an extension topic and does not form part of the PHY2039 exam.</p>
</div>

# Parallel code

<div class="alert alert-warning">
	<p>I strongly recommend using your own device for this handout.</p>
	<p>If you are using University machines, you may see warnings if you try to use too many jobs/cores and would recommend <code>n_jobs=2</code>  in the below code at most.</p>
</div>


## The idea 

The idea is that, rather than using a single "core" on our device, we split a Python problem up to run many tasks in parallel, either using multiple connected devices - a supercomputer (as is typically done in scientific research) - or using multiple cores on one device (as we'll do in this handout).

<div style="float: left; width: 45%; margin-left: 5%" markdown=true>
**Serial programming:**

![Serial programming](/static/images/week10/serial.png){width=75%}
</div>
<div style="float: left; width: 45%; margin-left: 5%" markdown=true>

**Parallel programming:**

![Parallel programming](/static/images/week10/parallel.png){width=100%}
</div>

<br style="clear: both;">

<div class="interlude" markdown=true>

### What is a core?

A core is the basic computation unit of a CPU (Central Processing Unit), and typically handles one task at a time. Back when I first had a laptop, dual-core was the big thing, because it let you do two whole things at a time! Then it was quad-core, which are now very common. Taking a quick look at the PC World website, roughly half of laptops are quad-core, a quarter dual-core and the others hexa- or octa-core. A High Performance Computing (HPC) system used for scientific research might be made up of individual devices (nodes) each made up of 10, 20, 30 cores or more.

</div>

### Some code

There are several methods (and Python modules) for running code in parallel. I have no chance of introducing you to all the methods, but two words that often come up are *OpenMP* and *MPI*:

* In *OpenMP* (Open Multi-Processing) code, each task has access to everything (data, variables etc), all of the time, so is suited to "shared memory" devices (think like one device, e.g. your laptop). 

* In *MPI* (Message Passing Interface) code, messages can be passed between individual tasks, even if not on the same hardware. This code runs on what are called "distributed memory" devices (think many computers chained together). Then, of course, the speed and efficiency with which messages are passed becomes incredibly important.

We're going to basically be doing the former here. Well, at least a simple taste of it anyway!


```python
from joblib import Parallel, delayed

n = 1000

def func(i):
    """
    Silly function to sum values from 0 to i
    """
    s = 0
    for j in range(i):
        s += j
    return s

Parallel(n_jobs=4)(delayed(func)(i) for i in range(n))
```

The `Parallel` "function" (which is actually a class not a function, but let's not get into that here...) does the magic. The `delayed` function captures the name and input arguments of the function `func` without actually executing `func(i)`, so that the work doesn't happen until the code is in parallel (hence "delayed").

Worth saying, there are many alternatives to `joblib`, but it's a relatively lightweight module in terms of how many new things we need to introduce in order to get it running.

## Exercise {: .exercise}

Use the module `time` to time the above code. and compare to calling the same function `n` times in a for loop. 

The time module/function goes like this:

```python
import time

t1 = time.time()
# do something
t2 = time.time()
```

You'll likely find that your parallel code was not quicker at all, and that's because there's overhead involved in the actual set up of the parallel "stuff". Try increasing `n` (slowly, as this is going to scale in time like $n^2$)


### Joblib options

You can set the `verbose` option to a non-zero value to see what's going on under the hood

```python
Parallel(n_jobs=4,verbose=10)(delayed(func)(i) for i in range(n))
```

When you do that you'll actually see some of the "overhead", as the `Parallel` function tests the water with how to split the work into batches:

```output
[Parallel(n_jobs=4)]: Using backend LokyBackend with 4 concurrent workers.
[Parallel(n_jobs=4)]: Batch computation too fast (0.0025s.) Setting batch_size=2.
[Parallel(n_jobs=4)]: Done   5 tasks      | elapsed:    0.0s
[Parallel(n_jobs=4)]: Batch computation too fast (0.0043s.) Setting batch_size=4.
[Parallel(n_jobs=4)]: Done  12 tasks      | elapsed:    0.0s
[Parallel(n_jobs=4)]: Done  28 tasks      | elapsed:    0.0s
[Parallel(n_jobs=4)]: Batch computation too fast (0.0043s.) Setting batch_size=8.
```



## Worked example

Consider the following code:

```python
import numpy as np

n = 5

# Array to store values in
M = np.zeros([n,n])

# Loop through i and j
for i in range(n):
    for j in range(n):
        M[i,j] = i**2+j**2
```

Let's suppose we want to do this to create a very large matrix, big enough that it takes a while.


```python
n = 5000

t1 = time.time()

# Array to store values in
M = np.zeros(n,n)

# Loop through i and j
for i in range(0,A.shape[0]):
    for j in range(0,A.shape[1]):
        M[i,j] = i**2+j**2
t2 = time.time()
print(t2-t1)
```

Setting `n` to 5000 takes around 18 seconds on my laptop. Bear in mind that's then $5000 \times 5000 = 25,000,000$ matrix elements. Again, this problem is $\mathcal{O}(n^2)$.

OK, so how could we parallelise? Well we could do so over the top for loop. Consider this:

```python
from joblib import Parallel, delayed
import numpy as np
import time

t1 = time.time()


n = 5000

def calc_row(i):
    row = np.zeros(n)
    for j in range(0,n):
        row[j] = i**2+j**2
    return row


# Loop through i and j
rows = Parallel(n_jobs=4)(delayed(calc_row)(i) for i in range(n))

# Put in array
M = np.array(rows)

t2 = time.time()
print(t2-t1)
```


It works! 5 seconds compared to 18 in serial and `M` is consistent with the serial version (you can run both to check).


## Find out more

This mini handout is just a flavour to give you a sense of the idea of parallel code. For more info you might like to check out

* [The joblib documentation](https://joblib.readthedocs.io/en/latest/parallel.html){target="_blank"} to find out a bit more about using `joblib`.
* [Another article on joblib](https://towardsdatascience.com/using-joblib-to-speed-up-your-python-pipelines-dd97440c653d){target="_blank"} which looks at one of its other features: the idea of *caching* your results so that time can be saved when the same function is called with the same input repeatedly.
* [Introduction to parallel computing](https://hpc.llnl.gov/training/tutorials/introduction-parallel-computing-tutorial){target="_blank"} a nice tutorial going into some motivation, technical details and maths-y examples by the Livermore Computing Center (one of the biggest scientific computing facilities in the US). Not Python-specific

Finally, a reminder, parallel code <u>will not</u> form part of your assessment for this module!

