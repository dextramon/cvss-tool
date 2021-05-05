
import re 
import math
import json
import subprocess
import os
import platform

#JSON Integration
with open('templates/data.json') as f:
    data = json.load(f)

#round-up 
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


class View: 
    def __init__(self):
        pass

    def get_name(self): 
        asset_name = input("Geben Sie den Namen des Assets ein: ")
        return asset_name

    def set_base_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return f"AV:{answer[0]}/AC:{answer[1]}/PR:{answer[2]}/UI:{answer[3]}/S:{answer[4]}/C:{answer[5]}/I:{answer[6]}/A:{answer[7]}"

    def set_temp_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return f"/E:{answer[0]}/RL:{answer[1]}/RC:{answer[2]}"

    def set_env_metrics(self, metrics):
        answer = []
        for m in metrics:
            for i in m:
                print(i + ": " + m[i])
            a = input().upper()
            while a not in m:
                a = input().upper()
            answer.append(a)
        return f"/CR:{answer[0]}/IR:{answer[1]}/AR:{answer[2]}/MAV:{answer[3]}/MAC:{answer[4]}/MPR:{answer[5]}/MUI:{answer[6]}/MS:{answer[7]}/MC:{answer[8]}/MI:{answer[9]}/MA:{answer[10]}"

    
class Controller: 
    def __init__(self): 
        self._view = View() 
        self._model = Vulnerability()

    def main_loop(self): 
        self._model.set_name(self._view.get_name())
        vector_string = self._calculate_base_score()
        vector_string += self._calculate_temp_score()
        vector_string += self._calculate_env_score()
        print(vector_string)
        self._model.set_vector(vector_string)
        print(self._model.get_name())
        print(self._model.get_base_score())
        print(self._model.get_temp_score())
        print(self._model.get_env_score())
        self.print_json()
        # self.print_pdf()
        self.print_txt()

    def _calculate_base_score(self):
        ATTACK_VECTOR = data['base_metric']['ATTACK_VECTOR']
        ATTACK_COMPLEXITY = data['base_metric']['ATTACK_COMPLEXITY']
        PRIVILEGES_REQUIRED = data['base_metric']['PRIVILEGES_REQUIRED']
        USER_INTERACTION = data['base_metric']['USER_INTERACTION']
        SCOPE = data['base_metric']['SCOPE']
        CONFIDENTIALITY = data['base_metric']['CONFIDENTIALITY']
        INTEGRITY = data['base_metric']['INTEGRITY']
        AVAILABILITY = data['base_metric']['AVAILABILITY']

        return self._view.set_base_metrics([ATTACK_VECTOR, ATTACK_COMPLEXITY, PRIVILEGES_REQUIRED, USER_INTERACTION, SCOPE,
                                                  CONFIDENTIALITY, INTEGRITY, AVAILABILITY])

    def _calculate_env_score(self): 
        CONFIDENTIALITY_REQUIREMENT = data["env_metric"]["CONFIDENTIALITY_REQUIREMENT"]
        INTEGRITY_REQUIREMENT = data["env_metric"]["INTEGRITY_REQUIREMENT"]
        AVAILABILITY_REQUIREMENT = data["env_metric"]["AVAILABILITY_REQUIREMENT"]
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

        return self._view.set_env_metrics([CONFIDENTIALITY_REQUIREMENT, INTEGRITY_REQUIREMENT, AVAILABILITY_REQUIREMENT, ATTACK_VECTOR, ATTACK_COMPLEXITY, PRIVILEGES_REQUIRED, USER_INTERACTION, SCOPE,
                                                CONFIDENTIALITY, INTEGRITY, AVAILABILITY])

    def _calculate_temp_score(self): 
        EXPLOIT_CODE_MATURITY = data['temp_metric']['EXPLOIT_CODE_MATURITY']
        REMIDATION_LEVEL = data['temp_metric']['REMIDATION_LEVEL']
        REPORT_CONFIDENCE = data['temp_metric']['REPORT_CONFIDENCE']

        return self._view.set_temp_metrics(
            [EXPLOIT_CODE_MATURITY, REMIDATION_LEVEL, REPORT_CONFIDENCE])

    def print_json(self): 
        with open('templates/template_output_json.json') as out:
            JSON_OUT = json.load(out)
        
        JSON_OUT['asset_name'] = self._model.get_name()
        JSON_OUT['vektor'] = self._model.get_vector()
        JSON_OUT['base_score'] = self._model.get_base_score()
        JSON_OUT['temp_score'] = self._model.get_temp_score()
        JSON_OUT['env_score'] = self._model.get_env_score()

        create_name = self._model.get_name() + '_output.json'
        
        with open(create_name, 'w') as out2:
            out2.write(json.dumps(JSON_OUT, indent=4))


    def print_txt(self): 
        with open('templates/template_output_txt.txt' , 'r') as file:
            TXT_OUT = file.read()
            TXT_OUT = TXT_OUT.replace('$asset_name$', self._model.get_name())
            TXT_OUT = TXT_OUT.replace('$vektor$', str(self._model.get_vector()))
            TXT_OUT = TXT_OUT.replace('$base_score$', str(self._model.get_base_score()))
            TXT_OUT = TXT_OUT.replace('$temp_score$', str(self._model.get_temp_score()))
            TXT_OUT = TXT_OUT.replace('$env_score$', str(self._model.get_env_score()))

            create_name = self._model.get_name() + '_output.txt'

            with open(create_name , 'w') as output:
                output.write(TXT_OUT)

    def print_pdf(self): 
        with open('templates/template_output_tex.tex' , 'r') as file:
            PDF_OUT = file.read()
            PDF_OUT = PDF_OUT.replace('$asset_name$', self._model.get_name())
            PDF_OUT = PDF_OUT.replace('$vektor$', str(self._model.get_vector()))
            PDF_OUT = PDF_OUT.replace('$base_score$', str(self._model.get_base_score()))
            PDF_OUT = PDF_OUT.replace('$temp_score$', str(self._model.get_temp_score()))
            PDF_OUT = PDF_OUT.replace('$env_score$', str(self._model.get_env_score()))

            create_name = self._model.get_name() + '_output.tex'

            with open(create_name , 'w') as output:
                output.write(PDF_OUT)

        subprocess.call('pdflatex ' + create_name)

        EXTENSIONS = ['.aux','.bcf','.lof','.log','.lot','.out','.run.xml','.toc' ,'.tex']
        OS_DIC = {'Linux' : 'rm', 'Darwin': 'rm', 'Windows': 'del'}
        OPERTOR = OS_DIC[platform.system()]
        for i in range(len(EXTENSIONS)):
            os.system(OPERTOR + ' ' + self._model.get_name()+ '_output' + EXTENSIONS[i])


    def _set_name(self):
        print(self._view.get_name())

class Vulnerability: 
    def __init__(self): 
        self._name = "Unknown"
        self._total_score = None
        self._tv = {"AV": None, "AC": None, "PR": None, "UI": None, "S": None, "C": None, "I": None, "A": None,
                    "E": "X", "RL": "X", "RC": "X", "CR": "X", "IR": "X", "AR": "X", "MAV": "X", "MAC": "X", 
                    "MPR": "X", "MUI": "X", "MS": "X", "MC": "X", "MI": "X", "MA": "X"} 
        self._base_score = None 
        self._temp_score = None
        self._env_score = None

    def _calculate_base_score(self): 
        AVV = {"L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ACV = {"H": 0.44, "L": 0.77}
        PRV = {"H": 0.27, "L": 0.62, "N": 0.85}
        UIV = {"N": 0.85, "R": 0.62}
        # CONTAINS CONFINDENTIALITY, INTEGRITY AND AVAILABILITY
        AVAILABILITY_VALUE = {"H": 0.56, "L": 0.22, "N": 0}

        #impact sub-score
        print(self._tv["C"])
        print(self._tv["I"])
        print(self._tv["A"])
        iss = 1 - ((1-AVAILABILITY_VALUE[self._tv["C"]])*(1-AVAILABILITY_VALUE[self._tv["I"]])*(1-AVAILABILITY_VALUE[self._tv["A"]]))
        
        impact = 0 

        if(self._tv["S"] == "U"):
            impact = 6.42*iss

        if(self._tv["S"] == "C"):
            impact = 7.52*(iss-0.029)-3.25*pow((iss-0.02), 15)

        exploitability = 8.22*AVV[self._tv["AV"]]*ACV[self._tv["AC"]]*PRV[self._tv["PR"]]*UIV[self._tv["UI"]]

        if impact <= 0: 
            self._base_score = 0
        elif self._tv["S"] == "U": 
            self._base_score = round_up((impact+exploitability), 1)
        elif self._tv["S"] == "C": 
            self._base_score = round_up((1.08*(impact+exploitability)), 1)
        else: 
            print("ERRO")

        print(self._base_score)

    def _calculate_temp_score(self): 
        ECMV = {
            "X": 1, "U": 0.91, "P": 0.94, "F": 0.97, "H": 1}
        RLV = {
            "X": 1, "O": 0.95, "T": 0.96, "W": 0.97, "U": 1}
        RCV = {"X": 1, "U": 0.92, "R": 0.96, "C": 1}

        self._temp_score = round_up(( self._base_score * ECMV[self._tv["E"]] * RLV[self._tv["RL"]] * RCV[self._tv["RC"]] ), 1)
        print(self._temp_score)

    def _calculate_env_score(self):
        AVVO = {"L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ACVO = {"H": 0.44, "L": 0.77}
        PRVO = {"H": 0.27, "L": 0.62, "N": 0.85}
        UIVO = {"N": 0.85, "R": 0.62}
        # CONTAINS CONFINDENTIALITY, INTEGRITY AND AVAILABILITY
        AVO = {"H": 0.56, "L": 0.22, "N": 0}

        AVV = {"X": AVVO[self._tv["AV"]], "L": 0.55, "A": 0.62, "N": 0.55, "P": 0.2}
        ACV = {"X": ACVO[self._tv["AC"]], "H": 0.44, "L": 0.77}
        PRV = {"X": PRVO[self._tv["PR"]], "H": 0.27, "L": 0.62, "N": 0.85}
        UIV = {"X": UIVO[self._tv["UI"]],"N": 0.85, "R": 0.62}
        AV = {"X": AVO[self._tv["A"]],"H": 0.56, "L": 0.22, "N": 0}
        IV = {"X": AVO[self._tv["I"]],"H": 0.56, "L": 0.22, "N": 0}
        CV = {"X": AVO[self._tv["C"]],"H": 0.56, "L": 0.22, "N": 0}
        ARV = {"X": 1.0, "H": 1.5, "M": 1.0, "L": 0.5}
        ECMV = {
            "X": 1, "U": 0.91, "P": 0.94, "F": 0.97, "H": 1}
        RLV = {
            "X": 1, "O": 0.95, "T": 0.96, "W": 0.97, "U": 1}
        RCV = {"X": 1, "U": 0.92, "R": 0.96, "C": 1}


        miss = 1 - ( ( 1-ARV[self._tv["CR"]] * CV[self._tv["MC"]] )  * ( 1-ARV[self._tv["IR"]] * IV[self._tv["MI"]] ) * ( 1-ARV[self._tv["AR"]] * AV[self._tv["MA"]] ))

        modified_impact = 0
        if( ( self._tv["MS"] == "U" ) or ( self._tv["S"] == "U" and self._tv["MS"] == "X" ) ): 
            modified_impact = 6.42*miss
        
        if(( self._tv["MS"] == "C" ) or ( self._tv["S"] == "C" and self._tv["MS"] == "X" ) ): 
            modified_impact = 7.52*(miss-0.029)-3.25*pow((miss*0.9731-0.02), 13)

        modified_exploitability = 8.22*AVV[self._tv["MAV"]]*ACV[self._tv["MAC"]]*PRV[self._tv["MPR"]]*UIV[self._tv["MUI"]]

        print(modified_impact)

        if(modified_impact <= 0): 
            self._env_score = 0
        
        if(( self._tv["MS"] == "U" ) or ( self._tv["S"] == "U" and self._tv["MS"] == "X" ) ): 
            self._env_score = round_up((round_up((modified_impact+modified_exploitability),1)*ECMV[self._tv["E"]]*RLV[self._tv["RL"]]*RCV[self._tv["RC"]] ),1)

        if(( self._tv["MS"] == "C" ) or ( self._tv["S"] == "C" and self._tv["MS"] == "X" ) ): 
            self._env_score = round_up((round_up(1.08*(modified_impact+modified_exploitability),1)*ECMV[self._tv["E"]]*RLV[self._tv["RL"]]*RCV[self._tv["RC"]] ),1)

    def _is_valid(self, vector):

        input_vector = vector

        # abbr for the metric for temp and env score and their valid values 
        base_score_values = {"AV": "LANP", "AC": "HL", "PR": "HLN", "UI": "NR", "S": "UC", "C": "HLN", "I": "HLN", "A": "HLN"} 
        temp_scores = {'E': 'XUPFH', 'RL': 'XOTWU', 'RC': 'XURC'}
        env_scores = {'CR': 'XHLM', 'IR': 'XHLM', 'AR': 'XHLM', 'MAV': 'XLANP', 'MAC': 'XHL', 'MPR': 'XHLN', 'MUI': 'XNR', 'MS': 'XUC', 'MC': 'XHLN', 'MI': 'XHLN', 'MA': 'XHLN'}

        base_score = re.compile('AV:[LANP]/AC:[HL]/PR:[HLN]/UI:[NR]/S:[CU]/C:[NHL]/I:[NHL]/A:[NHL].*')
        base_score_part = re.compile('AV:[LANP]/AC:[HL]/PR:[HLN]/UI:[NR]/S:[CU]/C:[NHL]/I:[NHL]/A:[NHL]')

        temp_score = re.compile(f'/E:[XUPFH]/RL:[XOTWU]/RC:[XURC].*')
        temp_score_part = re.compile(f'/E:[XUPFH]/RL:[XOTWU]/RC:[XURC]')

        env_score = re.compile('/CR:[XHLM]/IR:[XHLM]/AR:[XHLM]/MAV:[XLANP]/MAC:[XHL]/MPR:[XHLN]/MUI:[XNR]/MS:[XUC]/MC:[XHLN]/MI:[XHLN]/MA:[XHLN]')
        env_score_part = re.compile('/CR:[XHLM]/IR:[XHLM]/AR:[XHLM]/MAV:[XLANP]/MAC:[XHL]/MPR:[XHLN]/MUI:[XNR]/MS:[XUC]/MC:[XHLN]/MI:[XHLN]/MA:[XHLN]')

        temp_env_score = re.compile("/E:[XUPFH]/RL:[XOTWU]/RC:[XURC]/CR:[XHLM]/IR:[XHLM]/AR:[XHLM]/MAV:[XLANP]/MAC:[XHL]/MPR:[XHLN]/MUI:[XNR]/MS:[XUC]/MC:[XHLN]/MI:[XHLN]/MA:[XHLN]")

        #as the base score is mandatory for a vector, this if-condition checks if it has a proper base score otherwise it will throw an error
        if(base_score.match(input_vector)):
            input_vector = re.sub(base_score_part, '', input_vector)
        else: 
            return False
        print(input_vector)
        """
        COMMENT:
        As NIST and first use different techniques to calculate their score (NIST fills empty metrices with an X if at least one of temp or env has a value != 'X')
        first uses another standard and only adds metrices != 'X' to it. To make things simple, this functions checks if the new_input string has:
        - temp elements (NIST) -> checks temp_score template and remove temp_score_part template from input_string
        - env metrices (NIST) -> checks env_score template and remove env_score_part template from input_string
        - temp and env metrices (NIST) -> checks temp_env_score template and remove temp_env_score from input_string 
        - temp and/or env metrices (first) -> checks for all metrices from temp_scores and env_scores and remove them from the input_string
        """
        if(temp_env_score.match(input_vector)): 
            # removes the temp_score from the input_string

            input_vector = re.sub(temp_env_score, '', input_vector)
        elif(env_score.match(input_vector)): 
            # removes the env_score from the input_string
            input_vector = re.sub(env_score_part, '', input_vector)
        elif(temp_score.match(input_vector)):
            # removes the temp_score and the env_score from the input_string
            input_vector = re.sub(temp_score_part, '', input_vector)
        else: 
            # checks the input string for elements from temp_scores and removes them from the string if they are in the string
            for key in temp_scores: 
                if(re.match(f"/{key}:[{temp_scores[key]}].*", input_vector)):
                    print(f"{key}")
                    input_vector = re.sub(f'/{key}:[{temp_scores[key]}]', '', input_vector)

            # checks the input_string for elements from env_scores and removes them from the string if they are in the string
            for key in env_scores: 
                if(re.match(f"/{key}:[{env_scores[key]}].*", input_vector)):
                    print(f"{key}")
                    input_vector = re.sub(f'/{key}:[{env_scores[key]}]', '', input_vector)

        """
        COMMENT:
        after removing valid parts from the string, the string has to be empty otherwise the vector is corrupted and isn't valid for further process
        """

        print(input_vector)
        if input_vector == "": 
            # TO-DO: return a dictionary, which assinges each vector a dictionary the second dictionary contains the metrices. if
            return True
        else: 
            # TO-DO: throw and error if the string isn't empty
            return False

    def set_vector(self, vector): 
        if(self._is_valid(vector) == True): 
            all_parts = vector.split("/")

            for i in all_parts: 
                hel = i.split(":")
                self._tv[hel[0]] = hel[1]
            self._calculate_base_score()
            self._calculate_temp_score()
            self._calculate_env_score()
        else: 
            print("ERROR")

    def set_metric(self, key_name, key_value):
        base_score_values = {"AV": "LANP", "AC": "HL", "PR": "HLN", "UI": "NR", "S": "UC", "C": "HLN", "I": "HLN", "A":"HLN"} 
        temp_scores = {'E': 'XUPFH', 'RL': 'XOTWU', 'RC': 'XURC'}
        env_scores = {'CR': 'XHLN', 'IR': 'XHLN', 'AR': 'XHLN', 'MAV': 'XLANP', 'MAC': 'XHL', 'MPR': 'XHLN', 'MUI': 'XNR', 'MS': 'XUS', 'MC': 'XHLN', 'MI': 'XHLN', 'MA': 'XHLN'}

        if key_name in base_score_values: 
            if key_value in base_score_values[key_name]:
                self._tv[key_name] = key_value
                self._calculate_base_score()
            else: 
                print("ERROR 2")
        elif key_name in temp_scores:
            if key_value in temp_scores[key_name]:
                self._tv[key_name] = key_value
                self._calculate_temp_score()
            else: 
                print("ERROR 2")
        elif key_name in env_scores: 
            if key_value in env_scores[key_name]:
                self._tv[key_name] = key_value
                self._calculate_env_score()
            else: 
                print("ERROR 2")
        else: 
            print("ERROR")


    def get_metric(self, name): 
        return self._tv[name] 

    def get_vector(self): 
        return self._tv

    def set_name(self, name):
        self._name = name

    def get_name(self): 
        return self._name

    def get_total(self): 
        pass

    def get_base_score(self): 
        return self._base_score

    def get_temp_score(self): 
        return self._temp_score

    def get_env_score(self): 
        return self._env_score


if __name__ == "__main__":
    c1 = Controller() 

    c1.main_loop()