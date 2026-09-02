# Module Directory

Use this as a quick reference of where in the course we look at functions and topics

<ul id="tabs" class="nav nav-tabs">
    <li class="nav-item active"><a href="" data-target="#home1" data-toggle="tab" class="nav-link active">Content by Week</a></li>
    <li class="nav-item"><a href="" data-target="#profile1" data-toggle="tab" class="nav-link">Content by Python Module (NumPy, SciPy etc)</a></li>
</ul>
<div id="tabsContent" class="tab-content">
    <div id="home1" class="tab-pane fade active show">
       <h2>Content by week</h2>
       <p>Here are all of the functions and algorithms in PHY2039 by week</p>
       <a class="btn btn-primary" style="margin-bottom: 20px;" href="../learning_material_di_1/learning_material_di_1.pdf" target="_blank"><i class="fa fa-file-pdf-o" aria-hidden="true" title="PDF"></i> Download content by week as PDF</a>
       <h3>Week 1</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>
       	<tr>
       		<th colspan="2">Python Standard Library</th>
       	</tr>
	   		<td>Standard Library Functions
	   		</td>
	   		<td><code>abs</code>,<code>len</code>,<code>max</code>,<code>min,<code>print</code>,<code>round</code>,<code>sum</code>,<code>pow</code></td>
       	</tr>
       	<tr>
       		<td>Data types</td>
	   		<td><code>int</code>,<code>float</code>,<code>bool</code>,<code>str</code></td>
       	</tr>
       	<tr>
       		<td><code>range</code></td>
       		<td><code>range(1,10,2)</code></td>
       	</tr>
       	<tr>
       		<td><code>list</code></td>
       		<td><code>list(range(2,10,2))</code></td>
       	</tr>
       	<tr>
       		<th colspan="2">NumPy Functions<br/><small>Commands assume <code>import numpy as np</code></small></th>
       	</tr>       	
       	<tr>
       		<td><code>np.sqrt</code></td>
       		<td><code>np.sqrt(2)</code></td>
       	</tr>
       	<tr>
       		<td><code>np.pi</code></td>
       		<td><code>np.pi</code></td>
       	</tr>  
       	<tr>
       		<td><code>np.array</code></td>
       		<td><code>np.array([1,2,3])</code></td>
       	</tr>    
       	<tr>
       		<td><code>np.arange</code></td>
       		<td><code>np.arange(1,7,2)</code></td>
       	</tr> 
       	<tr>
       		<td><code>np.linspace</code></td>
       		<td><code>np.linspace(0,5,100)</code></td>
       	</tr> 
       	<tr>
       		<td><code>np.polyfit</code></td>
       		<td><code>np.polyfit(x,y,2)</code></td>
       	</tr>     
       	<tr>
       		<th colspan="2">Control Flow</th>
       	</tr>
       	<tr>
       		<td colspan="2">for loops</td>
       	</tr>      
       	<tr>
       		<td colspan="2">while loops</td>
       	</tr>       	 		     
       	<tr>
       		<td colspan="2">if statements</td>
       	</tr> 
       	<tr>
       		<td colspan="2">Functions</td>
       	</tr> 
       	<tr>
       		<th colspan="2">Matplotlib<br/>
       			<small>Commands assume <code>import matplotlib.pyplot as plt</small></th>
       	</tr>       	       	    
       	<tr>
       		<td><code>plt.plot</code></td>
       		<td><code>plt.plot(x,y)</code></td>
       	</tr> 	
       	<tr>
       		<td><code>plt.xlabel</code></td>
       		<td><code>plt.xlabel('x'))</code></td>
       	</tr> 
       	<tr>
       		<td><code>plt.ylabel</code></td>
       		<td><code>plt.ylabel('y'))</code></td>
       	</tr>   
       	<tr>
       		<td><code>plt.legend</code></td>
       		<td><code>plt.legend(['f(x)','y(x)'])</code></td>
       	</tr>        	     	
       </table>
       <h3 style="margin-top:60px;">Week 2</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>
       	<tr>
       		<td>Colon operator</td>
       		<td><code>x[:,1]</code></td>
       	</tr>          	
       	<tr>
       		<th colspan="2">NumPy Functions<br/><small>Commands assume <code>import numpy as np</code></small></th>
       	</tr> 
       	<tr>
       		<td><code>np.random.rand</code></td>
       		<td><code>np.random.rand(25)</code></td>
       	</tr>  
       	<tr>
       		<td><code>np.random.randint</code></td>
       		<td><code>np.random.randint(1,200,25)</code></td>
       	</tr> 
       	<tr>
       		<td><code>np.polyfit</code></td>
       		<td><code>p = np.polyfit(x,y,2)</code></td>
       	</tr> 
       	<tr>
       		<td><code>np.polyval</code></td>
       		<td><code>np.polyval(p,x)</code></td>
       	</tr> 
       	<tr>
       		<th colspan="2">Matplotlib<br/>
       			<small>Commands assume <code>import matplotlib.pyplot as plt</small></th>
       	</tr>       	       	    
       	<tr>
       		<td><code>plt.scatter</code></td>
       		<td><code>plt.scatter(x,y)</code></td>
       	</tr> 
       	<tr>
       		<td><code>plt.errorbar</code></td>
       		<td><code>plt.errorbar(x, y, yerr=err)</code></td>
       	</tr>
       	<tr>
       		<td><code>plt.semilogx</code></td>
       		<td><code>plt.semilogx(x, y)</code></td>
       	</tr>
       	<tr>
       		<td><code>plt.semilogy</code></td>
       		<td><code>plt.semilogy(x, y)</code></td>
       	</tr>
       	<tr>
       		<td><code>plt.loglog</code></td>
       		<td><code>plt.loglog(x, y)</code></td>
       	</tr>
       	<tr>
       		<th colspan="2">SciPy Curve Fit</th>
       	</tr> 
        <tr>
       		<td><code>curve_fit</code></td>
       		<td><code>import scipy.optimize as opt
<br/>popt, pcov = opt.curve_fit(model, x, y) 
</code></td>
       	</tr>      	       	
       	<tr>
       		<th colspan="2">Transforming functions to a polynomial</th>
       	</tr> 
       	<tr>
       		<th colspan="2">Working with files</th>
       	</tr> 
       	<tr>
       		<td><code>np.loadtxt</code></td>
       		<td><code>np.loadtxt('data.txt')</code></td>
       	</tr> 
       </table>
       <h3 style="margin-top:60px;">Week 3</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>         	
       	<tr>
       		<th colspan="2">NumPy Functions<br/><small>Commands assume <code>import numpy as np</code></small></th>
       	</tr>
       	<tr>
       		<td><code>np.zeros</code></td>
       		<td><code>np.zeros(10)</code></td>
       	</tr>  
       	<tr>
       		<td><code>np.ones</code></td>
       		<td><code>np.ones(10)</code></td>
       	</tr>  
       	<tr>
       		<td><code>np.full</code></td>
       		<td><code>np.full([2,3],np.pi)</code></td>
       	</tr>          	      	
       	<tr>
       		<td><code>np.fill_diagonal</code></td>
       		<td><code>np.fill_diagonal(np.zeros([3,3]), 1)</code></td>
       	</tr>     
       	<tr>
       		<td><code>np.dot</code></td>
       		<td><code>np.dot(vec1, vec2)</code></td>
       	</tr> 
       	<tr>
       		<td><code>np.cross</code></td>
       		<td><code>np.cross(vec1, vec2)</code></td>
       	</tr>  
       	<tr>
       		<th colspan="2">Matrix Operations</th>
       	</tr>
       	<tr>
       		<td>Matrix multiplication</td>
       		<td><code>X @ Y</code></td>
       	</tr> 
       	<tr>
       		<td>Matrix transpose</td>
       		<td><code>X.T</code></td>
       	</tr>        	       	
       	<tr>
       		<th colspan="2">SciPy Functions</th>
       	</tr>
       	<tr>
       		<td><code>scipy.sparse.diags</code></td>
       		<td><code>import scipy.sparse as sparse<br/>
sparse.diags([1, -2, 1], [-1, 0, 1], [3, 3]).toarray()</code></td>
       	</tr>         	
       	<tr>
       		<td><code>scipy.linalg.det</code></td>
       		<td><code>import scipy.linalg as sla<br/>sla.det(X))</code></td>
       	</tr> 
       	<tr>
       		<td><code>scipy.linalg.inv</code></td>
       		<td><code>import scipy.linalg as sla<br/>sla.inv(X))</code></td>
       	</tr>        	
       	<tr>
       		<td><code>scipy.linalg.solve</code></td>
       		<td><code>import scipy.linalg as sla<br/>sla.solve(A,b))</code></td>
       	</tr> 
       	<tr>
       		<td><code>scipy.linalg.eig</code></td>
       		<td><code>import scipy.linalg as sla<br/>sla.eig(X))</code></td>
       	</tr>        	
       </table>
       <h3 style="margin-top:60px;">Week 4</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>         	
       	<tr>
       		<th colspan="2">Control Flow</th>
       	</tr>
       	<tr>
       		<td>Logical Operators</td>
       		<td><code><</code>,<code>></code>,<code>==</code>,<code><=</code>,<code>!=</code> etc</td>
       	</tr> 
       	<tr>
       		<td colspan="2">for loops</td>
       	</tr>      
       	<tr>
       		<td colspan="2">while loops</td>
       	</tr>       	 		     
       	<tr>
       		<td colspan="2">if statements</td>
       	</tr> 
       	<tr>
       		<td colspan="2">Functions</td>
       	</tr>
       	<tr>
       		<td>time.time()</td>
       		<td><code>import time<br/>time.time()</code> </td>
       	</tr>         	        	
       	<tr>
       		<td>List Comprehension</td>
       		<td><code>[x > 2 for x in a]</code> </td>
       	</tr>  
       	<tr>
       		<th colspan="2">Root Finding Methods</th>
       	</tr> 
       	<tr>
       		<td colspan="2">The Bisection Method</td>
       	</tr>        	   
       	<tr>
       		<td colspan="2">The Newton-Raphson Method</td>
       	</tr>       	   
      </table>
       <h3 style="margin-top:60px;">Week 5</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>         	  
       	<tr>
       		<th colspan="2">Root Finding Methods</th>
       	</tr> 
       	<tr>
       		<td colspan="2">The Bisection Method</td>
       	</tr>        	   
       	<tr>
       		<td colspan="2">The Newton-Raphson Method</td>
       	</tr> 
       	<tr>
       		<td colspan="2">The Secant Method</td>
       	</tr>  
       	<tr>
       		<td colspan="2">The False Position Method</td>
       	</tr>
       	<tr>
       		<td><code>np.roots</code></td>
       		<td><code>np.roots([1,0,-2])</code> </td>
       	</tr> 
       	<tr>
       		<td><code>scipy.optimize.fsolve</code></td>
       		<td><code>import scipy.optimize as opt
<br/>opt.fsolve(func, 4)</code> </td>
       	</tr>  
       	<tr>
       		<td colspan="2">Basins of attraction (Newton Fractals)</td>
       	</tr>       	        	      	
       	<tr>
       		<th colspan="2">Error handling</th>
       	</tr> 
       	<tr>
       		<td>Raising an error</td>
       		<td><code>Raise ValueError('Message')</code> </td>
       	</tr>        	       	
       	<tr>
       		<th colspan="2">Lambda Functions</th>
       	</tr> 
       	<tr>
       		<td><code>lambda</code></td>
       		<td><code>lambda x : x**2</code> </td>
       	</tr>         	      	   
      </table>
       <h3 style="margin-top:60px;">Week 6</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>         	  
       	<tr>
       		<th colspan="2">NumPy Functions<br/><small>Commands assume <code>import numpy as np</code></small></th>
       	</tr>
       	<tr>
       		<td><code>np.meshgrid</code></td>
       		<td><code>np.meshgrid(x,y)</code> </td>
       	</tr> 
       	<tr>
       		<th colspan="2">Matplotlib<br/>
       			<small>Commands assume <code>import matplotlib.pyplot as plt</small></th>
       	</tr> 
       	<tr>
       		<td>New figure (<code>plt.figure</code>)</td>
       		<td><code>plt.figure()</code></td>
       	</tr>        	            
       	<tr>
       		<td>Save figure (<code>plt.savefig</code>)</td>
       		<td><code>plt.savefig('filename.png')</code></td>
       	</tr>
       	<tr>
       		<td>Change font size</td>
       		<td><code>plt.rcParams['font.size'] = 20</code></td>
       	</tr>
       	<tr>
       		<td>Add a plot grid</td>
       		<td><code>plt.grid()</code></td>
       	</tr>        
       	<tr>
       		<td><code>plt.quiver</code></td>
       		<td><code>plt.quiver(X,Y,U,V)</code></td>
       	</tr> 
       	<tr>
       		<td>3D axes</td>
       		<td><code>plt.axes(projection='3d')</code></td>
       	</tr>
       	<tr>
       		<td>3D paramteric plotting</td>
       		<td><code>ax = plt.axes(projection='3d')<br/>ax.plot(x,y,z)</code></td>
       	</tr>
       	<tr>
       		<td>3D surface plotting</td>
       		<td><code>ax.plot_surface(X, Y, Z)</code></td>
       	</tr>       	
       	<tr>
       		<td>Contour plotting</td>
       		<td><code>ax.contourf(X, Y, Z)</code></td>
       	</tr>          	      	   
      </table> 
       <h3 style="margin-top:60px;">Week 7</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr>                    
       	<tr>
       		<th colspan="2">Numerical Differentiation</th>
       	</tr>  
       	<tr>
       		<td colspan="2">
       			Finite Difference Methods
       		</td>
       	</tr>        	        	
       	<tr>
       		<td><code>np.roll</code></td>
       		<td><code>np.roll(x,-2)</code></td>
       	</tr>       	
       	<tr>
       		<td><code>np.gradient</code></td>
       		<td><code>np.gradient(x,t,edge_order=2)</code></td>
       	</tr> 
       	<tr>
       		<td><code>scipy.misc.derivative</code></td>
       		<td><code>import scipy.misc as sm<br/>sm.derivative(func, x0, dx=1e-6)</code></td>
       	</tr>         	       	     
       	<tr>
       		<th colspan="2">Numerical Integration</th>
       	</tr>  
       	<tr>
       		<td colspan="2">Midpoint Rule</td>
       	</tr>         		   
       	<tr>
       		<td colspan="2">Trapezoid Rule</td>
       	</tr> 
       	<tr>
       		<td colspan="2">Simpson's Rule</td>
       	</tr>  
       	<tr>
       		<td><code>scipy.integrate.quad</code></td>
       		<td><code>from scipy import integrate<br/>integrate.quad(myfunc, 0, 2*np.pi)</code></td>
       	</tr>
       	<tr>
       		<td><code>scipy.integrate.trapezoid</code></td>
       		<td><code>from scipy import integrate<br/>integrate.trapezoid(y,x)</code></td>
       	</tr>        	        	
       	<tr>
       		<td><code>scipy.integrate.dblquad</code></td>
       		<td><code>from scipy import integrate<br/>integrate.dblquad(f, 0, 2, 0, 1)</code></td>
       	</tr> 
       	<tr>
       		<td><code>scipy.integrate.tplquad</code></td>
       		<td><code>from scipy import integrate<br/>integrate.tplquad(f, 0, 2, 0, 1, 0, 1)</code></td>
       	</tr>       	          
      </table> 
       <h3 style="margin-top:60px;">Week 8</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr> 	
       	<tr>
       		<td><code>scipy.integrate.odeint</code></td>
       		<td><code>from scipy.integrate import odeint<br/>y = odeint(rhs,y0,t)</code></td>
       	</tr>       	
       	<tr>
       		<td colspan="2"><code>odeint</code> for initial value problems</td>
       	</tr>   
       	<tr>
       		<td colspan="2"><code>odeint</code> for systems of ODEs</td>
       	</tr>          	   	
       	<tr>
       		<td colspan="2"><code>odeint</code> for higher order ODEs</td>
       	</tr>    
       	<tr>
       		<td colspan="2">Direction fields (quiver plots)</td>
       	</tr>        	           
      </table> 
       <h3 style="margin-top:60px;">Week 9</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr> 	 
       	<tr>
       		<td colspan="2">The Euler Method</td>
       	</tr>          	   	
       	<tr>
       		<td colspan="2">Truncation errors</td>
       	</tr>    
       	<tr>
       		<td colspan="2">Stability</td>
       	</tr>
       	<tr>
       		<td colspan="2">Runge-Kutte Methods</td>
       	</tr>        	        	           
      </table>
       <h3 style="margin-top:60px;">Week 10</h3>
       <table class="table table-striped">
       	<tr style="font-size: 1.2em;">
       		<th>FUNCTION/TOPIC</th>
       		<th>EXAMPLE</th>
       	</tr> 
       	<tr>
       		<td colspan="2">ODE Method Module</td>
       	</tr>       		 
       	<tr>
       		<td colspan="2">Stability in 2D</td>
       	</tr>        	        	
       	<tr>
       		<th colspan="2">Dynamical Systems</th>
       	</tr>       
       	<tr>
       		<td colspan="2">Lotka-Voltera system</td>
       	</tr>
       	<tr>
       		<td colspan="2">Logistic Map</td>
       	</tr>
       </table>        
    </div>
    <div id="profile1" class="tab-pane fade">
    	<h2>Content by Python module</h2>
    	<p>Use the following tables to search for a function by module/name.</p>
       <a class="btn btn-primary" style="margin-bottom: 20px;" href="../learning_material_di_2/learning_material_di_2.pdf" target="_blank"><i class="fa fa-file-pdf-o" aria-hidden="true" title="PDF"></i> Download content by Python module as PDF</a>
	    <h3 style="margin-top:60px;">Python Standard Library</h3>
	    <table class="table table-striped">
	   	<tr style="font-size: 1.2em;">
	   		<th>FUNCTION</th>
	   		<th>EXAMPLE</th>
	   		<th>FIND IN...</th>
	   	</tr> 
	   	<tr>
	   		<td>Standard Library Functions
	   		</td>
	   		<td><code>abs</code>,<code>len</code>,<code>max</code>,<code>min,<code>print</code>,<code>round</code>,<code>sum</code>,<code>pow</code></td>
	   		<td>Handout 1</td>
	   	</tr>
	   	<tr>
	   		<td>Data types</td>
	   		<td><code>int</code>,<code>float</code>,<code>bool</code>,<code>str</code></td>
	   		<td>Handout 1</td>
	   	</tr>
	   	<tr>
	   		<td><code>range</code></td>
	   		<td><code>range(1,10,2)</code></td>
	   		<td>Handout 1</td>		
	   	</tr>
	   	<tr>
	   		<td><code>list</code></td>
	   		<td><code>list(range(2,10,2))</code></td>
	   		<td>Handout 1</td>   		
	   	</tr>
		<tr>
			<td>Colon operator</td>
			<td><code>x[:,1]</code></td>
	   		<td>Handout 4</td>		
		</tr>   	
		<tr>
			<td>Logical Operators</td>
			<td><code><</code>,<code>></code>,<code>==</code>,<code><=</code>,<code>!=</code> etc</td>
	   		<td>Handout 4</td>
		</tr>    	
		<tr>
			<td colspan="2">for loops</td>
	   		<td>Handout 1, Handout 4</td>
		</tr>      
		<tr>
			<td colspan="2">while loops</td>
	   		<td>Handout 1, Handout 4</td>
		</tr>       	 		     
		<tr>
			<td colspan="2">if statements</td>
	   		<td>Handout 1, Handout 4</td>
		</tr> 
		<tr>
			<td colspan="2">Functions</td>
	   		<td>Handout 1, Handout 4</td>
		</tr>
		<tr>
			<td>Raising an error</td>
			<td><code>Raise ValueError('Message')</code> </td>
   			<td>Handout 4</td>		
		</tr> 
		<tr>
			<td>List Comprehension</td>
			<td><code>[x > 2 for x in a]</code> </td>
			<td>Handout 4</td>
		</tr> 
		<tr>
			<td><code>lambda</code> functions</td>
			<td><code>lambda x : x**2</code> </td>
   			<td>Handout 4</td>			
		</tr> 
		</table>   
	    <h3 style="margin-top:60px;">NumPy</h3>
	    <small>Commands assume <code>import numpy as np</code></small>
	    <table class="table table-striped">
	   	<tr style="font-size: 1.2em;">
	   		<th>FUNCTION</th>
	   		<th>EXAMPLE</th>
	   		<th>FIND IN...</th>
	   	</tr> 
	   	<tr>
			<th colspan="3">Working with arrays</th>
		</tr>  
		<tr>
			<td><code>np.array</code></td>
			<td><code>np.array([1,2,3])</code></td>
			<td>Handout 1</td>
		</tr>    
		<tr>
			<td><code>np.arange</code></td>
			<td><code>np.arange(1,7,2)</code></td>
			<td>Handout 1</td>
		</tr>  
		<tr>
			<td><code>np.linspace</code></td>
			<td><code>np.linspace(0,5,100)</code></td>
			<td>Handout 1</td>
		</tr>
		<tr>
			<td><code>np.random.rand</code></td>
			<td><code>np.random.rand(25)</code></td>
			<td>Handout 2</td>
		</tr>  
		<tr>
			<td><code>np.random.randint</code></td>
			<td><code>np.random.randint(1,200,25)</code></td>
			<td>Handout 2</td>
		</tr>
		<tr>
			<td><code>np.zeros</code></td>
			<td><code>np.zeros(10)</code></td>
			<td>Handout 3</td>
		</tr>
		<tr>
			<td><code>np.ones</code></td>
			<td><code>np.ones(10)</code></td>
			<td>Handout 3</td>
		</tr>  
		<tr>
			<td><code>np.full</code></td>
			<td><code>np.full([2,3],np.pi)</code></td>
			<td>Handout 3</td>
		</tr>          	      	
		<tr>
			<td><code>np.fill_diagonal</code></td>
			<td><code>np.fill_diagonal(np.zeros([3,3]), 1)</code></td>
			<td>Handout 3</td>
		</tr>     
		<tr>
			<td><code>np.dot</code></td>
			<td><code>np.dot(vec1, vec2)</code></td>
			<td>Handout 3</td>
		</tr> 
		<tr>
			<td><code>np.cross</code></td>
			<td><code>np.cross(vec1, vec2)</code></td>
			<td>Handout 3</td>
		</tr>  
		<tr>
			<td><code>np.meshgrid</code></td>
			<td><code>np.meshgrid(x,y)</code> </td>
			<td>Handout 5</td>
		</tr> 
		<tr>
			<td><code>np.roll</code></td>
			<td><code>np.roll(x,-2)</code></td>
			<td>Handout 7</td>
		</tr>  	 			 	
		<tr>
			<th colspan="3">Working with files</th>
		</tr> 
		<tr>
			<td><code>np.loadtxt</code></td>
			<td><code>np.loadtxt('data.txt')</code></td>
			<td>Handout 2</td>
		</tr>
	   	<tr>
			<th colspan="3">Curve Fitting</th>
		</tr>  		
		<tr>
			<td><code>np.polyfit</code></td>
			<td><code>np.polyfit(x,y,2)</code></td>
			<td>Handout 1, Handout 2</td>
		</tr>
		<tr>
			<td><code>np.polyval</code></td>
			<td><code>np.polyval(p,x)</code></td>
			<td>Handout 2</td>
		</tr>
	   	<tr>
			<th colspan="3">Root Finding</th>
		</tr> 
		<tr>
			<td><code>np.roots</code></td>
			<td><code>np.roots([1,0,-2])</code> </td>
			<td>Handout 5</td>
		</tr>
	   	<tr>
			<th colspan="3">Numerical Differentiation</th>
		</tr> 
		<tr>
			<td><code>np.gradient</code></td>
			<td><code>np.gradient(x,t,edge_order=2)</code></td>
			<td>Handout 7</td>
		</tr>						  
		</table>
	    <h3 style="margin-top:60px;">SciPy</h3>
	    <table class="table table-striped">
	   	<tr style="font-size: 1.2em;">
	   		<th>FUNCTION</th>
	   		<th>EXAMPLE</th>
	   		<th>FIND IN...</th>
	   	</tr> 
	   	<tr>
			<th colspan="3">Curve Fitting</th>
		</tr>  
		 <tr>
			<td><code>curve_fit</code></td>
			<td><code>import scipy.optimize as opt
	<br/>popt, pcov = opt.curve_fit(model, x, y) 
	</code></td>
			<td>Handout 2</td>
			</tr>
	   	<tr>
			<th colspan="3">Linear Algebra</th>
		</tr> 
		<tr>
			<td><code>scipy.sparse.diags</code></td>
			<td><code>import scipy.sparse as sparse<br/>
	sparse.diags([1, -2, 1], [-1, 0, 1], [3, 3]).toarray()</code></td>
			<td>Handout 3</td>
		</tr>        	
		<tr>
			<td><code>scipy.linalg.det</code></td>
			<td><code>import scipy.linalg as sla<br/>sla.det(X))</code></td>
			<td>Handout 3</td>
		</tr>   
		<tr>
			<td><code>scipy.linalg.inv</code></td>
			<td><code>import scipy.linalg as sla<br/>sla.inv(X))</code></td>
			<td>Handout 3</td>
		</tr>         	
		<tr>
			<td><code>scipy.linalg.solve</code></td>
			<td><code>import scipy.linalg as sla<br/>sla.solve(A,b))</code></td>
			<td>Handout 3</td>
		</tr>   
		<tr>
			<td><code>scipy.linalg.eig</code></td>
			<td><code>import scipy.linalg as sla<br/>sla.eig(X))</code></td>
			<td>Handout 3</td>
		</tr>  
	   	<tr>
			<th colspan="3">Root Finding</th>
		</tr>
		<tr>
			<td><code>scipy.optimize.fsolve</code></td>
			<td><code>import scipy.optimize as opt
	<br/>opt.fsolve(func, 4)</code> </td>
			<td>Handout 5</td>  		
		</tr> 	
		<tr>
			<th colspan="3">Numerical Differentiation</th>
		</tr>  	
		<tr>
			<td><code>scipy.misc.derivative</code></td>
			<td><code>import scipy.misc as sm<br/>sm.derivative(func, x0, dx=1e-6)</code></td>
			<td>Handout 7</td>  		
		</tr>          	       	     
		<tr>
			<th colspan="3">Numerical Integration</th>
		</tr>  
		<tr>
			<td><code>scipy.integrate.quad</code></td>
			<td><code>from scipy import integrate<br/>integrate.quad(myfunc, 0, 2*np.pi)</code></td>
			<td>Handout 7</td>  		
		</tr> 
		<tr>
			<td><code>scipy.integrate.trapezoid</code></td>
			<td><code>from scipy import integrate<br/>integrate.trapezoid(y,x)</code></td>
			<td>Handout 7</td>  		
		</tr>        	        	
		<tr>
			<td><code>scipy.integrate.dblquad</code></td>
			<td><code>from scipy import integrate<br/>integrate.dblquad(f, 0, 2, 0, 1)</code></td>
			<td>Handout 7</td>  		
		</tr> 
		<tr>
			<td><code>scipy.integrate.tplquad</code></td>
			<td><code>from scipy import integrate<br/>integrate.tplquad(f, 0, 2, 0, 1, 0, 1)</code></td>
			<td>Handout 7</td>  		
		</tr>  
		<tr>
			<th colspan="3">Differential Equations</th>
		</tr> 
		<tr>
			<td><code>scipy.integrate.odeint</code></td>
			<td><code>from scipy.integrate import odeint<br/>y = odeint(rhs,y0,t)</code></td>
			<td>Handout 8</td>  		
		</tr> 	
		</table>
	   <h3 style="margin-top:60px;">Matplotlib</h3>
	    <small>Commands assume <code>import matplotlib.pyplot as plt</code></small>
	    <table class="table table-striped">
	   	<tr style="font-size: 1.2em;">
	   		<th>FUNCTION</th>
	   		<th>EXAMPLE</th>
	   		<th>FIND IN...</th>
	   	</tr> 
		<tr>
			<th colspan="3">Basic Plotting</th>
		</tr>   	
		<tr>
			<td><code>plt.plot</code></td>
			<td><code>plt.plot(x,y)</code></td>
			<td>Handout 1</td>
		</tr> 	
		<tr>
			<td><code>plt.xlabel</code></td>
			<td><code>plt.xlabel('x'))</code></td>
			<td>Handout 1</td>
		</tr> 	 
		<tr>
			<td><code>plt.ylabel</code></td>
			<td><code>plt.ylabel('y'))</code></td>
			<td>Handout 1</td>
		</tr> 	   
		<tr>
			<td><code>plt.legend</code></td>
			<td><code>plt.legend(['f(x)','y(x)'])</code></td>
			<td>Handout 1</td>
		</tr> 	
		<tr>
			<td><code>plt.scatter</code></td>
			<td><code>plt.scatter(x,y)</code></td>
			<td>Handout 2</td>
		</tr> 
		<tr>
			<td><code>plt.errorbar</code></td>
			<td><code>plt.errorbar(x, y, yerr=err)</code></td>
			<td>Handout 2</td>
		</tr> 
		<tr>
			<td>New figure (<code>plt.figure</code>)</td>
			<td><code>plt.figure()</code></td>
			<td>Handout 6</td>
		</tr>        	            
		<tr>
			<td>Save figure (<code>plt.savefig</code>)</td>
			<td><code>plt.savefig('filename.png')</code></td>
			<td>Handout 6</td>
		</tr>
		<tr>
			<td>Change font size</td>
			<td><code>plt.rcParams['font.size'] = 20</code></td>
			<td>Handout 6</td>
		</tr>
		<tr>
			<td>Add a plot grid</td>
			<td><code>plt.grid()</code></td>
			<td>Handout 6</td>
		</tr>      	
		<tr>
			<th colspan="3">Log plots</th>
		</tr> 	
		<tr>
			<td><code>plt.semilogx</code></td>
			<td><code>plt.semilogx(x, y)</code></td>
			<td>Handout 2</td>
		</tr> 
		<tr>
			<td><code>plt.semilogy</code></td>
			<td><code>plt.semilogy(x, y)</code></td>
			<td>Handout 2</td>
		</tr> 
		<tr>
			<td><code>plt.loglog</code></td>
			<td><code>plt.loglog(x, y)</code></td>
			<td>Handout 2</td>
		</tr> 
		<tr>
			<th colspan="3">Advanced Plotting</th>
		</tr> 
		<tr>
			<td><code>plt.quiver</code></td>
			<td><code>plt.quiver(X,Y,U,V)</code></td>
			<td>Handout 6, Handout 9</td>
		</tr> 
		<tr>
			<td>3D axes</td>
			<td><code>plt.axes(projection='3d')</code></td>
			<td>Handout 6</td>
		</tr> 
		<tr>
			<td>3D paramteric plotting</td>
			<td><code>ax = plt.axes(projection='3d')<br/>ax.plot(x,y,z)</code></td>
			<td>Handout 6</td>
		</tr> 
		<tr>
			<td>3D surface plotting</td>
			<td><code>ax.plot_surface(X, Y, Z)</code></td>
			<td>Handout 6</td>
		</tr>       	
		<tr>
			<td>Contour plotting</td>
			<td><code>ax.contourf(X, Y, Z)</code></td>
			<td>Handout 6</td>
		</tr>          	     		
		</table>  		 		
    </div>
</div>
