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

    # if node is ast.AnnAssign, this is the vars being initialised so need to add to list of var names
    # if node is ast.AnnAssign then add its initial value to the list (= None) (will update later on - see below)
    # if ast.Assign then this is assigning the initial values in the init_example_variables fn, so update
    # the initial values dict with these (will overwrite the None in the dict)
    # need to check for pairs of ast.AnnAssign followed by an ast.Expr - this is the form of
    # a variable being declared followed by a docstring expression. can get these var descriptions
    # from here, and if there is no ast.Expr immediately after an ast.AnnAssign then this var does not
    # have a docstring and so set the description to be ""
    for node in ast.walk(example_module_tree):
        if isinstance(node, ast.AnnAssign):
            initial_values_dict[node.target.id] = node.value.value
            var_name = node.target.id
            if var_name not in variable_names:
                variable_names.append(var_name)
        if isinstance(node, ast.Assign):
            initial_values_dict[node.targets[0].id] = node.value.value
    # doing as 2 separate for loops for now - example_tree.body only has AnnAssign, Expr and FunctionDef
    # components, and no Assign components (unless you look inside the FunctionDef, will investigate combining
    # into one for loop)
    for a, b in pairwise(example_module_tree.body):
        if isinstance(a, ast.AnnAssign) and isinstance(b, ast.Expr):
            var_names_and_descriptions[a.target.id] = b.value.value
        if isinstance(a, ast.AnnAssign) and not isinstance(b, ast.Expr):
            var_names_and_descriptions[a.target.id] = ""
    # create each of the 3 components seen in what_you_want.json
    dict_module_entry["example_module"] = variable_names
    module_dict["DICT_MODULE"] = dict_module_entry
    default_dict["DICT_DEFAULT"] = initial_values_dict
    descriptions_dict["DICT_DESCRIPTIONS"] = var_names_and_descriptions
    # create combined dict to go in json file
    new_dict = {**default_dict, **descriptions_dict, **module_dict}
    # create json file
    with open(Path("./dicts_test/data/example_dicts_recreated.json"), "w") as f:
        json.dump(new_dict, f, indent=4)


if __name__ == "__main__":
    data_structure_dicts()
