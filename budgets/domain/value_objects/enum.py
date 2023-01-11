import enum
import typing

class ChoiceEnum(enum.Enum):
    @classmethod
    def choices(cls) -> typing.List[typing.Tuple[str, str]]:
        return ((option.name, option.value) for option in cls)