
import math
import json

########################
### Json integration ###
########################

with open('data.json') as f:
    data = json.load(f)

########################

# roundup to the first decimal 

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model


    # controller erechnet base metrics 

    def set_base_metrics(self):
        ATTACK_VECTOR = data['base_metric']['ATTACK_VECTOR']
        ATTACK_COMPLEXITY = data['base_metric']['ATTACK_COMPLEXITY']
        PRIVILEGES_REQUIRED = data['base_metric']['PRIVILEGES_REQUIRED']
        USER_INTERACTION = data['base_metric']['USER_INTERACTION']
        SCOPE = data['base_metric']['SCOPE']
        CONFIDENTIALITY = data['base_metric']['CONFIDENTIALITY']
        INTEGRITY = data['base_metric']['INTEGRITY']
        AVAILABILITY = data['base_metric']['AVAILABILITY']

        base_score = self._view.set_base_metrics([ATTACK_VECTOR, ATTACK_COMPLEXITY, PRIVILEGES_REQUIRED, USER_INTERACTION, SCOPE,
                                                  CONFIDENTIALITY, INTEGRITY, AVAILABILITY])
        print(self._model.set_base_metric(base_score))

    def set_all(self):
        self.set_base_metrics()
        self.set_temp_metrics()
        self.set_env_metrics()

    # BERECHNUNG DES ENVIRONMENTAL SCORE

    def set_env_metrics(self):
        ATTACK_VECTOR = data['base_metric']['ATTACK_VECTOR']
        ATTACK_VECTOR["X"] = "Not Defined"
        ATTACK_COMPLEXITY = data['base_metric']['ATTACK_COMPLEXITY']
        ATTACK_COMPLEXITY["X"] = "Not Defined"
        PRIVILEGES_REQUIRED = data['base_metric']['PRIVILEGES_REQUIRED']
        PRIVILEGES_REQUIRED["X"] = "Not Defined"
        USER_INTERACTION = data['base_metric']['USER_INTERACTION']
        USER_INTERACTION["X"] = "Not Defined"
        SCOPE = data['base_metric']['SCOPE']
        SCOPE["X"] = "Not Defined"
        CONFIDENTIALITY = data['base_metric']['CONFIDENTIALITY']
        CONFIDENTIALITY["X"] = "Not Defined"
        INTEGRITY = data['base_metric']['INTEGRITY']
        INTEGRITY["X"] = "Not Defined"
        AVAILABILITY = data['base_metric']['AVAILABILITY']
        AVAILABILITY["X"] = "Not Defined"
        CONFIDENTIALITY_REQUIREMENT = data["env_metric"]["CONFIDENTIALITY_REQUIREMENT"]
        INTEGRITY_REQUIREMENT = data["env_metric"]["INTEGRITY_REQUIREMENT"]
        AVAILABILITY_REQUIREMENT = data["env_metric"]["AVAILABILITY_REQUIREMENT"]

        environmental_score = self._view.set_env_metrics([ATTACK_VECTOR, ATTACK_COMPLEXITY, PRIVILEGES_REQUIRED, USER_INTERACTION, SCOPE,
                                                  CONFIDENTIALITY, INTEGRITY, AVAILABILITY, CONFIDENTIALITY_REQUIREMENT,
                                                  INTEGRITY_REQUIREMENT, AVAILABILITY_REQUIREMENT])
        print(self._model.set_env_metrics(environmental_score))

    # DER CONTROLLER BEKOMMT DIE IMPACT METRIC ZUGEWIESEN

    def set_temp_metrics(self):
        EXPLOIT_CODE_MATURITY = data['temp_metric']['EXPLOIT_CODE_MATURITY']
        REMIDATION_LEVEL = data['temp_metric']['REMIDATION_LEVEL']
        REPORT_CONFIDENCE = data['temp_metric']['REPORT_CONFIDENCE']

        temporary_score = self._view.set_temp_metrics(
            [EXPLOIT_CODE_MATURITY, REMIDATION_LEVEL, REPORT_CONFIDENCE])
        print(self._model.set_temp_metrics(temporary_score))


class View:
    def __init__(self):
        pass

    # view for set_base_metrics 

    def set_base_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return answer

    # view for set_env_metrics
    
    def set_env_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return answer

    # view for set_temp_metrics

    def set_temp_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return answer

class Model:
    def __init__(self):
        self._base_metrics = None
        self._temporary_metrics = None
        self._temp_score_vec = None
        self._complexity = None
        self._impact = None
        self._base_score = None
        self._base_score_vec = None
        self._env_score = None
        self._env_score_vec = None

    def _get_impact_function(self):
        if self._impact == 0:
            return 0
        else:
            return 1.176

    # set metrics

    def set_base_metric(self, new_base):
        self._base_metrics = new_base
        self._calculate_base_score(self._base_metrics)

    def set_temp_metrics(self, new_temporary):
        self._temporary_metrics = new_temporary
        return self._calculate_temp_score(self._temporary_metrics)

    def set_env_metrics(self, new_env): 
        self._env_metrics = new_env
        self._calculate_env_score(self._env_score)

    # calculation for the score of each three

    def _calculate_base_score(self, inp):
        print(inp)
        ATTACK_VECTOR_VALUE = {"L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ATTACK_COMPLEXITY_VALUE = {"H": 0.44, "L": 0.77}
        PRIVILEGES_VALUE = {"H": 0.27, "L": 0.62, "N": 0.85}
        USER_INTERACTION_VALUE = {"N": 0.85, "R": 0.62}
        # CONTAINS CONFINDENTIALITY, INTEGRITY AND AVAILABILITY
        AVAILABILITY_VALUE = {"H": 0.56, "L": 0.22, "N": 0}

        self._base_score_vec = f"AV:{inp[0]}/AC:{inp[1]}/PR:{inp[2]}/UI:{inp[3]}/S:{inp[4]}/C:{inp[5]}/I:{inp[6]}/A:{inp[7]}"

        base_score = []

        base_score.append(ATTACK_VECTOR_VALUE[inp[0]])
        base_score.append(ATTACK_COMPLEXITY_VALUE[inp[1]])
        base_score.append(PRIVILEGES_VALUE[inp[2]])
        base_score.append(USER_INTERACTION_VALUE[inp[3]])
        base_score.append(AVAILABILITY_VALUE[inp[5]])  # Confidentiality
        base_score.append(AVAILABILITY_VALUE[inp[6]])  # Integrity
        base_score.append(AVAILABILITY_VALUE[inp[7]])  # Availability

        exploitability = round_up(
            8.22*base_score[0]*base_score[1]*base_score[2]*base_score[3], 1)

        impact = (1 - ((1 - AVAILABILITY_VALUE[inp[5]]) * (
            1 - AVAILABILITY_VALUE[inp[6]]) * (1 - AVAILABILITY_VALUE[inp[7]])))

        impact_subscore = 0

        if(inp[4] == "U"):
            impact_subscore = 6.42 * impact
        else:
            impact_subscore = ((7.52 * (impact - 0.029)) -
                               (3.25 * math.pow((impact - 0.02), 15)))

        print("BASE: " + str(exploitability))
        print("IMPACT: " + str(impact_subscore))

        if (impact_subscore <= 0):
            self._base_score = 0
        else:
            if inp[4] == "U":
                self._base_score = round_up(
                    (impact_subscore+exploitability), 1)
            else:
                self._base_score = round_up(
                    (1.08 * (impact_subscore+exploitability)), 1)

        print(self._base_score)
        print(self._base_score_vec)
        return self._base_score

    def _calculate_temp_score(self, li):

        print(li)

        EXPLOIT_CODE_MATURITY_VALUE = {
            "X": 1, "U": 0.91, "P": 0.94, "F": 0.97, "H": 1}
        REMIDATION_LEVEL_VALUE = {
            "X": 1, "O": 0.95, "T": 0.96, "W": 0.97, "U": 1}
        REPORT_CONFIDENCE_VALUE = {"X": 1, "U": 0.92, "R": 0.96, "C": 1}

        self._temp_score_vec = f"E:{li[0]}/RL:{li[1]}/RC:{li[2]}"

        temporary_score = []

        temporary_score.append(EXPLOIT_CODE_MATURITY_VALUE[li[0]])
        temporary_score.append(REMIDATION_LEVEL_VALUE[li[1]])
        temporary_score.append(REPORT_CONFIDENCE_VALUE[li[2]])

        self._temporary_metrics = round_up(
            (self._base_score * temporary_score[0] * temporary_score[1] * temporary_score[2]), 1)

        print(self._temp_score_vec)

        return self._temporary_metrics

    def _calculate_env_score(self, inp):
        print(inp)
        ATTACK_VECTOR_VALUE = {"X": 0, "L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ATTACK_COMPLEXITY_VALUE = {"X": 0, "H": 0.44, "L": 0.77}
        PRIVILEGES_VALUE = {"X": 0, "H": 0.27, "L": 0.62, "N": 0.85}
        USER_INTERACTION_VALUE = {"X": 0,"N": 0.85, "R": 0.62}
        AVAILABILITY_VALUE = {"X": 0,"H": 0.56, "L": 0.22, "N": 0}
        AVAILABILITY_REQUIREMENT_VALUE = {"X": 1.0, "H": 1.5, "L": 1.0, "N": 0.5}

        self._env_score_vec = f"CR:{inp[8]}/IR:{inp[9]}/AR:{inp[10]}/MAV:{inp[0]}/MAC:{inp[1]}/MPR:{inp[2]}/MUI:{inp[3]}/MS:{inp[4]}/MC:{inp[5]}/MI:{inp[6]}/MA:{inp[7]}"
        env_score = []

        env_score.append(ATTACK_VECTOR_VALUE[inp[0]])
        env_score.append(ATTACK_COMPLEXITY_VALUE[inp[1]])
        env_score.append(PRIVILEGES_VALUE[inp[2]])
        env_score.append(USER_INTERACTION_VALUE[inp[3]])
        env_score.append(AVAILABILITY_VALUE[inp[5]])  # Confidentiality
        env_score.append(AVAILABILITY_VALUE[inp[6]])  # Integrity
        env_score.append(AVAILABILITY_VALUE[inp[7]])  # Availability
        env_score.append(AVAILABILITY_REQUIREMENT_VALUE[inp[8]])
        env_score.append(AVAILABILITY_REQUIREMENT_VALUE[inp[9]])
        env_score.append(AVAILABILITY_REQUIREMENT_VALUE[inp[10]])

        print(self._env_score_vec)
        return 0


if __name__ == "__main__":
    v = View()
    m = Model()
    c = Controller(v, m)
    c.set_all()
