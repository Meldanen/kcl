import enum


class NodeTypeEnum(enum.Enum):

    BASIC_ROBOT_MODEL_CLIENT = "BasicRobotModelClient"

    BASIC_ROBOT_MODEL_SERVER = "BasicRobotModelServer"

    TWO_WAY_COMMUNICATION_CHATTER = "TwoWayCommunication"

    SERVER = "Server"

    CLIENT = "Client"

    JOINT_STATES = "joint_states"
