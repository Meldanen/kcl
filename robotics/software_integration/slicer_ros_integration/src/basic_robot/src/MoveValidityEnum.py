import enum


class MoveValidityEnum(enum.Enum):
    VALID = "Valid Position"
    INVALID = "Invalid Position"
    NOT_AVAILABLE = "N/A"

    @property
    def isValid(self):
        return self == MoveValidityEnum.VALID

    @property
    def isInvalid(self):
        return self == MoveValidityEnum.INVALID
