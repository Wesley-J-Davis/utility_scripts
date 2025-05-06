# Working with ncdump

General Options
-h → Display only the header (metadata).

-c → Show dimensions and coordinate variables.

-v var1,var2,... → Display only the specified variables.

-t → Show time metadata in a human-readable format.

-f format → Control floating-point precision in the output.

-l length → Limit line length in the output.

-s → Display string data as text.

-b → Show data in binary representation.

-x → Convert NetCDF metadata into XML format.

Data Output Options
-d → Output data using CDL (Common Data Language) notation.

-p precision → Set precision for floating-point numbers.

-g → Show group structure (for NetCDF-4 files).

-m → Print memory layout information.

Filtering and Formatting
-F → Use FORTRAN-style indices in variable output.

-D → Enable debug mode for more verbose information.

To show only the metadata:
ncdump -h myfile.nc

To display specific variables:
ncdump -v temperature,pressure myfile.nc

