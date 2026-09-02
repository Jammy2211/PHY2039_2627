
<h2>Content by Python module</h2>
<p>Use the following tables to search for a function by module/name.</p>
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
