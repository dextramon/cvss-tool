
import math
import json

########################
### Json integration ###
########################

with open('data.json') as f:
    data = json.load(f)

########################


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model

    def set_base_metrics(self):
        ATTACK_VECTOR = data['set_base_metrics']['ATTACK_VECTOR']
        ATTACK_COMPLEXITY = data['set_base_metrics']['ATTACK_COMPLEXITY']
        PRIVILEGES_REQUIRED = data['set_base_metrics']['PRIVILEGES_REQUIRED']
        USER_INTERACTION = data['set_base_metrics']['USER_INTERACTION']
        SCOPE = data['set_base_metrics']['SCOPE']
        CONFIDENTIALITY = data['set_base_metrics']['CONFIDENTIALITY']
        INTEGRITY = data['set_base_metrics']['INTEGRITY']
        AVAILABILITY = data['set_base_metrics']['AVAILABILITY']

        base_score = self._view.set_base_metrics([ATTACK_VECTOR, ATTACK_COMPLEXITY, PRIVILEGES_REQUIRED, USER_INTERACTION, SCOPE,
                                                  CONFIDENTIALITY, INTEGRITY, AVAILABILITY])
        print(self._model.set_base_metric(base_score))

    def set_all(self):
        self.set_base_metrics()
        self.set_impact_metrics()

    def set_impact_metrics(self):
        EXPLOIT_CODE_MATURITY = data['set_impact_metrics']['EXPLOIT_CODE_MATURITY']
        REMIDATION_LEVEL = data['set_impact_metrics']['REMIDATION_LEVEL']
        REPORT_CONFIDENCE = data['set_impact_metrics']['REPORT_CONFIDENCE']

        temporary_score = self._view.set_temporary_metrics(
            [EXPLOIT_CODE_MATURITY, REMIDATION_LEVEL, REPORT_CONFIDENCE])
        print(self._model.set_temporary_metrics(temporary_score))


class View:
    def __init__(self):
        pass

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

    def set_temporary_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return answer

    def get_base_metrics():
        pass


class Model:
    def __init__(self):
        self._base_metrics = None
        self._temporary_metrics = None
        self._complexity = None
        self._impact = None
        self._base_score = None

    def get_impact_function(self):
        if self._impact == 0:
            return 0
        else:
            return 1.176

    def set_temporary_metrics(self, new_temporary):
        self._temporary_metrics = new_temporary
        return self._calculate_temporary_score(self._temporary_metrics)

    def set_base_metric(self, new_base):
        self._base_metrics = new_base
        self._calculate_base_score(self._base_metrics)

    def _calculate_temporary_score(self, li):

        print(li)

        EXPLOIT_CODE_MATURITY_VALUE = {
            "X": 1, "U": 0.91, "P": 0.94, "F": 0.97, "H": 1}
        REMIDATION_LEVEL_VALUE = {
            "X": 1, "O": 0.95, "T": 0.96, "W": 0.97, "U": 1}
        REPORT_CONFIDENCE_VALUE = {"X": 1, "U": 0.92, "R": 0.96, "C": 1}

        temporary_score = []

        temporary_score.append(EXPLOIT_CODE_MATURITY_VALUE[li[0]])
        temporary_score.append(REMIDATION_LEVEL_VALUE[li[1]])
        temporary_score.append(REPORT_CONFIDENCE_VALUE[li[2]])

        self._temporary_metrics = round_up(
            (self._base_score * temporary_score[0] * temporary_score[1] * temporary_score[2]), 1)

        return self._temporary_metrics

    def _calculate_base_score(self, inp):
        print(inp)
        ATTACK_VECTOR_VALUE = {"L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ATTACK_COMPLEXITY_VALUE = {"H": 0.44, "L": 0.77}
        PRIVILEGES_VALUE = {"H": 0.27, "L": 0.62, "N": 0.85}
        USER_INTERACTION_VALUE = {"N": 0.85, "R": 0.62}
        AVAILABILITY_VALUE = {"H": 0.56, "L": 0.22, "N": 0}

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
        return self._base_score


if __name__ == "__main__":
    v = View()
    m = Model()
    c = Controller(v, m)
    c.set_all()
