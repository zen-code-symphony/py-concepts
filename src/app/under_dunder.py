"""Provide example usage of underscore and dunders member naming in Python.

Key takeways:
- _var: Naming convention indicates internal use. Hint for developers but not
  enforced by enterpreter.
- var_: Naming convention to avoid conflicts with Python keywords.
- __var: Results in naming mangling; enforced by interpreter.
- __var__: Special methods defined by Python language. Avoid using this.
- _: Temporary or insignificant variables. Stores results os last expression
  in Python REPL.
"""


class UnderDunder:
    """Represents a class with underscore and dunder members for demo."""

    def __init__(self) -> None:
        self._single_lead_under: str = "i'm _single_lead_under"
        self.__dunder: str = "i'm __dunder"
        self.class_: str = "i'm class_"

    def get_dunder(self) -> str:
        return self.__dunder

    def __dunder__(self) -> str:
        return "avoid me"

    def return_temporary_increment_by_one(self, _):
        return _ + 1
