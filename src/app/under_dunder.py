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


if __name__ == "__main__":
    # Internal-use only but still accessible.
    under_dunder = UnderDunder()
    print(under_dunder._single_lead_under)

    # Name mangling hides the real member name.
    try:
        print(under_dunder.__dunder)
    except AttributeError:
        print("Not accessible as name mangled")
        print(under_dunder._UnderDunder__dunder)  # type: ignore

    # Special methods allowed, but avoid using them.
    print(under_dunder.__dunder__())

    # Temporary name.
    print(under_dunder.return_temporary_increment_by_one(1))
