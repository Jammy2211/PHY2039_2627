<div id="profile1" class="tab-pane fade">
	<h2>Content by Python module</h2>
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