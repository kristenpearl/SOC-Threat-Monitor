KNOWN_THREATS = {

    "45.83.91.12": {

        "risk": "Critical",

        "source": "Threat Feed"

    },

    "203.55.11.40": {

        "risk": "High",

        "source": "Threat Feed"

    },

    "91.204.14.18": {

        "risk": "Medium",

        "source": "Threat Feed"

    }

}

def check_ip(ip):

    return KNOWN_THREATS.get(

        ip,

        {

            "risk":"Low",

            "source":"Unknown"

        }

    )
