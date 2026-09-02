# Hand-in 1 solution 

```python
import numpy as pi

k = np.arange(0,20)
pi_approx = (12**0.5)*sum(1/((2*k+1)*(-3)**k))

print("Pi approximation: {}".format(pi_approx))
print("Pi actual: {}".format(np.pi))
```