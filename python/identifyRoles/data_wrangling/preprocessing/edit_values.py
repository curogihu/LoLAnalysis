def convert_role_to_num(role):
    if role == "NONE":
        return 1

    elif role == "SOLO":
        return 2

    elif role == "DUO":
        return 3

    elif role == "DUO_CARRY":
        return 4

    elif role == "DUO_SUPPORT":
        return 5

    else:
        return 99


def convert_lane_to_num(lane):
    if lane == "TOP":
        return 1

    elif lane == "JUNGLE":
        return 2

    elif lane == "MIDDLE":
        return 3

    elif lane == "BOTTOM":
        return 4

    else:
        return 99


def adjust_participantId(participantId):
    if participantId < 6:
        return participantId

    else:
        return participantId - 5