def calculate_risk(severity):

    if severity == "Critical":
        return 100

    elif severity == "High":
        return 75

    elif severity == "Medium":
        return 50

    return 25
