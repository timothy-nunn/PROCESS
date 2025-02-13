from data import example_module


class MyClass:
    """My docstring"""

    my_var: str = None
    """vars docs"""


my_variable: str = None
"""Docstring for variable"""


if __name__ == "__main__":
    for _ in range(2):
        print("\n")
        print(
            example_module.example_double,
            example_module.example_double_nodescr,
            example_module.example_double_uninit,
            example_module.example_double_array,
            example_module.example_double_array_uninit,
            example_module.example_int,
            example_module.example_int_uninit,
            example_module.example_string,
            example_module.example_string_uninit,
        )
        print("\n")
        example_module.init_example_variables()
