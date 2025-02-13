example_double: float = None
"""an example double"""

example_double_nodescr: float = None

example_double_uninit: float = None
"""another example double (uninitialised)"""

example_double_array: list[float] = None
"""an example double array"""

example_double_array_uninit: list[float] = None

example_int: int = None
"""and example integer
with a description over two lines
"""

example_int_uninit: int = None
"""yet another integer"""

example_string: str = None
"""and example string"""

example_string_uninit: str = None
"""another example string (uninitialised)"""


def init_example_variables():
    global example_double
    example_double = 0.0

    global example_double_nodescr
    example_double_nodescr = 1.5e1

    global example_int
    example_int = 5

    global example_string
    example_string = "string____"
