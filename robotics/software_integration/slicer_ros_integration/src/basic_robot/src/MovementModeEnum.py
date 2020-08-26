import enum


class MovementModeEnum(enum.Enum):
    NONE = 0, "None"
    JOINT_POSITION = 1, "Joint Position"
    END_EFFECTOR_POSITION = 2, "End Effector Position"

    @property
    def getId(self):
        return self.value[0]

    @property
    def getLabel(self):
        return self.value[1]

    @property
    def isJointPosition(self):
        return self == MovementModeEnum.JOINT_POSITION

    @property
    def isEndEffectorPosition(self):
        return self == MovementModeEnum.END_EFFECTOR_POSITION


class Utils:

    @staticmethod
    def getEnumFromLabel(value):
        for mode in MovementModeEnum:
            if mode.getLabel == value:
                return mode
        return None

    @staticmethod
    def getEnumFromId(value):
        for mode in MovementModeEnum:
            if mode.getId == value:
                return mode
        return None
