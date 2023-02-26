# Element


## _class_ Element(model, name, function_string=None)
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



### _property_ equation()
Returns the equation as originally set.


* **Returns**

    The equation, either a SD DSL Element or Operator.

### _property_ function_string()
Returns a string representation of the underlying function.


### plot(starttime=None, stoptime=None, dt=None, return_df=False)
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
