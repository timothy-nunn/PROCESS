import ast
import inspect
import json
from itertools import pairwise
from pathlib import Path

from dicts_test.data import example_module
from dicts_test.data.example_module import init_example_variables


def data_structure_dicts():
    # initialise example module variables
    init_example_variables()
    # parse the example module using ast
    example_module_tree = ast.parse(inspect.getsource(example_module))

    # initialise dictionaries and lists to write to
    descriptions_dict = {}
    default_dict = {}
    module_dict = {}
    variable_names = []
    dict_module_entry = {}
    initial_values_dict = {}
    var_names_and_descriptions = {}
    var_names_and_descriptions = {}

    # look through the nodes in the tree in a pairwise manner
    # want to do this to find things of the form: variable initialised \n variable docstring

    # if node is ast.AnnAssign, this is the vars being initialised so need to add to list of var names
    # if node is ast.AnnAssign then add its initial value to the list (= None) (will update later on using getattr)

    # need to check for pairs of ast.AnnAssign followed by an ast.Expr - this is the form of
    # a variable being declared followed by a docstring expression. can get these var descriptions
    # from here, and if there is no ast.Expr immediately after an ast.AnnAssign then this var does not
    # have a docstring and so set the description to be ""

    # use the variable name list and getattr to get the initial values of the variables from the example_module

    for a, b in pairwise(example_module_tree.body):
        if isinstance(a, ast.AnnAssign):
            # get the variable names
            initial_values_dict[a.target.id] = a.value.value
            var_name = a.target.id
            # add variable name to the list if not already there
            if var_name not in variable_names:
                variable_names.append(var_name)
            # if docstring immediately follows the variable declaration, add docstring to descriptions dict
            if isinstance(b, ast.Expr):
                var_names_and_descriptions[a.target.id] = b.value.value
            # if no docstring for variable, have a blank description
            if not isinstance(b, ast.Expr):
                var_names_and_descriptions[a.target.id] = ""

    # for each variable in the file, get the initial value (either is None, or value initialised in init_example_variables fn)
    for var in variable_names:
        initial_values_dict[var] = getattr(example_module, var)

    dict_module_entry["example_module"] = variable_names

    # create each of the 3 dict components seen in what_you_want.json
    module_dict["DICT_MODULE"] = dict_module_entry
    default_dict["DICT_DEFAULT"] = initial_values_dict
    descriptions_dict["DICT_DESCRIPTIONS"] = var_names_and_descriptions

    # create combined dict to go in json file
    new_dict = {**default_dict, **descriptions_dict, **module_dict}

    # create json file
    with open(Path("./dicts_test/data/example_dicts_recreated3.json"), "w") as f:
        json.dump(new_dict, f, indent=4)


if __name__ == "__main__":
    data_structure_dicts()
