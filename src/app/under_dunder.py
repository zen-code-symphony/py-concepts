"""Provide example usage of underscore and dunders in Python."""


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
