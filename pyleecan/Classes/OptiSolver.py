# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Optimization/OptiSolver.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Optimization/OptiSolver
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError
from .OptiProblem import OptiProblem
from .XOutput import XOutput


class OptiSolver(FrozenClass):
    """Optimization solver class"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        problem=-1,
        xoutput=-1,
        logger_name="Pyleecan.OptiSolver",
        is_keep_all_output=False,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if problem == -1:
            problem = OptiProblem()
        if xoutput == -1:
            xoutput = XOutput()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            problem = obj.problem
            xoutput = obj.xoutput
            logger_name = obj.logger_name
            is_keep_all_output = obj.is_keep_all_output
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "problem" in list(init_dict.keys()):
                problem = init_dict["problem"]
            if "xoutput" in list(init_dict.keys()):
                xoutput = init_dict["xoutput"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
        # Initialisation by argument
        self.parent = None
        # problem can be None, a OptiProblem object or a dict
        if isinstance(problem, dict):
            self.problem = OptiProblem(init_dict=problem)
        elif isinstance(problem, str):
            from ..Functions.load import load

            self.problem = load(problem)
        else:
            self.problem = problem
        # xoutput can be None, a XOutput object or a dict
        if isinstance(xoutput, dict):
            self.xoutput = XOutput(init_dict=xoutput)
        elif isinstance(xoutput, str):
            from ..Functions.load import load

            self.xoutput = load(xoutput)
        else:
            self.xoutput = xoutput
        self.logger_name = logger_name
        self.is_keep_all_output = is_keep_all_output

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiSolver_str = ""
        if self.parent is None:
            OptiSolver_str += "parent = None " + linesep
        else:
            OptiSolver_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.problem is not None:
            tmp = self.problem.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OptiSolver_str += "problem = " + tmp
        else:
            OptiSolver_str += "problem = None" + linesep + linesep
        if self.xoutput is not None:
            tmp = self.xoutput.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OptiSolver_str += "xoutput = " + tmp
        else:
            OptiSolver_str += "xoutput = None" + linesep + linesep
        OptiSolver_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OptiSolver_str += (
            "is_keep_all_output = " + str(self.is_keep_all_output) + linesep
        )
        return OptiSolver_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.problem != self.problem:
            return False
        if other.xoutput != self.xoutput:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.is_keep_all_output != self.is_keep_all_output:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiSolver_dict = dict()
        if self.problem is None:
            OptiSolver_dict["problem"] = None
        else:
            OptiSolver_dict["problem"] = self.problem.as_dict()
        if self.xoutput is None:
            OptiSolver_dict["xoutput"] = None
        else:
            OptiSolver_dict["xoutput"] = self.xoutput.as_dict()
        OptiSolver_dict["logger_name"] = self.logger_name
        OptiSolver_dict["is_keep_all_output"] = self.is_keep_all_output
        # The class name is added to the dict fordeserialisation purpose
        OptiSolver_dict["__class__"] = "OptiSolver"
        return OptiSolver_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.problem is not None:
            self.problem._set_None()
        if self.xoutput is not None:
            self.xoutput._set_None()
        self.logger_name = None
        self.is_keep_all_output = None

    def _get_problem(self):
        """getter of problem"""
        return self._problem

    def _set_problem(self, value):
        """setter of problem"""
        check_var("problem", value, "OptiProblem")
        self._problem = value

        if self._problem is not None:
            self._problem.parent = self

    problem = property(
        fget=_get_problem,
        fset=_set_problem,
        doc=u"""Problem to solve

        :Type: OptiProblem
        """,
    )

    def _get_xoutput(self):
        """getter of xoutput"""
        return self._xoutput

    def _set_xoutput(self, value):
        """setter of xoutput"""
        check_var("xoutput", value, "XOutput")
        self._xoutput = value

        if self._xoutput is not None:
            self._xoutput.parent = self

    xoutput = property(
        fget=_get_xoutput,
        fset=_set_xoutput,
        doc=u"""Optimization results containing every output

        :Type: XOutput
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_is_keep_all_output(self):
        """getter of is_keep_all_output"""
        return self._is_keep_all_output

    def _set_is_keep_all_output(self, value):
        """setter of is_keep_all_output"""
        check_var("is_keep_all_output", value, "bool")
        self._is_keep_all_output = value

    is_keep_all_output = property(
        fget=_get_is_keep_all_output,
        fset=_set_is_keep_all_output,
        doc=u"""Boolean to keep every output

        :Type: bool
        """,
    )
