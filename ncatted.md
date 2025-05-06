# Working with ncatted
ncatted -a [attribute],[variable],[mode],[type],[value] file.nc
Where:

attribute → Name of the attribute to modify.

variable → Associated variable (global for file-wide attributes).

mode → Action to perform:

c → Create new attribute

m → Modify existing attribute

d → Delete attribute

type → Data type:

char, byte, short, int, float, double

value → New attribute value.

Available Options
-h → Display help information.

-O → Overwrite the existing file.

-o output.nc → Write changes to a new output file instead of overwriting.

-v variable_name → Specify a variable.

-a attribute_name → Specify an attribute.

-m → Modify an existing attribute.

-c → Create a new attribute.

-d → Delete an attribute.

-t type → Set attribute type.

-p precision → Set precision for floating-point attributes.

##Modify a global attribute
ncatted -a title,global,m,char,"Updated Title" file.nc

##Delete an attribute
ncatted -a units,temperature,d,, file.nc

##Create a new attribute
ncatted -a source,pressure,c,char,"Sensor Data" file.nc
