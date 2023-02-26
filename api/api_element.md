# Element


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## _class_ Element(model, name, function_string=None)
=======
### _class_ Element(model, name, function_string=None)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
## _class_ Element(model, name, function_string=None)
>>>>>>> master
=======
## _class_ Element(model, name, function_string=None)
>>>>>>> master
=======
## _class_ Element(model, name, function_string=None)
>>>>>>> master
=======
## _class_ Element(model, name, function_string=None)
>>>>>>> master
Generic element in a SD DSL model.

Concrete elements are Biflows, Flows, Constants and Converters.

In general elements are created via an instance of the Model class, using the appropriate methods.


* **Parameters**

    
    * **Model** – Model.
    The model the element belongs to.


    * **Name** – String.
    The name of the model.


    * **Function_string** – String (Default=None)
    The function string of the element. This is set by the framework.



<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### _property_ equation()
=======
#### _property_ equation()
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
### _property_ equation()
>>>>>>> master
=======
### _property_ equation()
>>>>>>> master
=======
### _property_ equation()
>>>>>>> master
=======
### _property_ equation()
>>>>>>> master
Returns the equation as originally set.


* **Returns**

    The equation, either a SD DSL Element or Operator.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
### _property_ function_string()
Returns a string representation of the underlying function.


### plot(starttime=None, stoptime=None, dt=None, return_df=False)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======


#### _property_ function_string()
Returns a string representation of the underlying function.


#### plot(starttime=None, stoptime=None, dt=None, return_df=False)
>>>>>>> c4b007f0983e9b9f720f83627e97c51e2fe58b6f
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
=======
>>>>>>> master
Plot the equation.


* **Parameters**

    
    * **starttime** – Integer (Default None).
    The timestep where to begin the plot. If set to None the plot starts at the Models starttime.


    * **stoptime** – Integer (Default None)
    The timestep when to end the plot.


    * **dt** – Fraction of 1 (Default None)
    The timestep to plot. If set to None, then the plot uses the Models dt.


    * **return_df** – Boolean (Default False).
    Whether to plot the equation or return the underlying dataframe.



* **Returns**

    The plot (via matplotlib) or a Pandas dataframe if return_df=True
