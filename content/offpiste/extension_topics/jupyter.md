<div class="interlude">
    <p>This is an extension topic and does not form part of the PHY2039 exam.</p>
</div>

# Jupyter Notebooks


## About Jupyter notebooks

Jupyter notebooks are another way of running Python code, they do so in a web browser, allowing "cells" of code to be run and displaying the output right below. In user testing, before we brought Python into the curriculum, students favoured Spyder, partially because of the similarity to the RStudio interface. However, Jupyter notebooks are widely used, including by some of our academics.


## Downloading a notebook

You can download most of my handouts, including this one, as a Jupyter Notebook. 

Right click on the Download Notebook link and save the file to your device (somewhere that you'll be able to find it in a moment).

## Opening a notebook

Open up Anaconda navigator and select the Jupyter Notebook tile by clicking "Launch" (JupyterLab could also be used).

Jupyter will open in your web browser where you will be presented with your computer's file directory. Navigate to the notebook file that you saved and click to open it. 

## Using a notebook

Once opened, the handout is split into what are called "cells". You can use the Run button to run the code in a cell and move on to the next.

Here's a cell that you can run if you open this in Jupyter

```python
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-5,5,100)
plt.plot(x,np.sin(x))
```

Note that you can edit it and then run again.

You can use the "+" button to create new cells if you want to try anything out as you move through the handout.

Your work will be autosaved as you go along, or you can go to File -> Save as... to save it somewhere else.

There you go, a crash course! This was very brief, so if you plan to use the notebooks then don't hesitate to give me a shout and I'll be happy to talk through more details.

Enjoy!

