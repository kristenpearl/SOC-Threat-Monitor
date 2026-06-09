ATTACK_TECHNIQUES = {

    "Brute Force Login Attempt": {

        "id": "T1110",

        "name": "Brute Force"

    },

    "Suspicious Account Access": {

        "id": "T1078",

        "name": "Valid Accounts"

    },

    "Command Execution": {

        "id": "T1059",

        "name": "Command and Scripting Interpreter"

    }

}

def get_mitre_mapping(incident):

    return ATTACK_TECHNIQUES.get(

        incident,

        {

            "id":"Unknown",

            "name":"Unknown"

        }

    )
