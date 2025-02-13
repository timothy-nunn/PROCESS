The dicts are used in PROCESS to get information at runtime about variables.

There is a lot of information in the dicts, most of which can be removed as I convert things. However, there are several dicts which hold data about every single PROCESS variable which will need to be replicated when I convert the data structure to Python (Phase I).

You can generate a reduced version of the dicts by running
```shell
./example_dicts.sh 
```
from the PROCESS root, creating a `example_dicts.json` file in this directory.

Have a look through this file and look for every variable that I define in `example_module.f90`.


What we want to ensure is that when the data structure moves from Fortran to Python, we retain the entries in 
* `DICT_DEFAULT`
* `DICT_DESCRIPTIONS`
* `DICT_MODULE`
The other dictionaries can be handeled during their respective modules conversion.


