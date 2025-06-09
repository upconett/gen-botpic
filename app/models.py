class Emoji:
    id: str

class Color:
    """ Color in hex code """
    code: str

    def __init__(self, code: str):
        self.code = code.replace('#', '')

    @property
    def hex(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"#{self.code}"
