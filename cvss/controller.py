import os
import platform
import subprocess
import json 
import hashlib
from vulnerability import Vulnerability
from view import View
from tkinter import *
from tkinter import ttk
from graphical import CreationView
from graphical import GetCredentials

#JSON Integration
with open('templates/data.json') as f:
    data = json.load(f)

class Controller: 
    def __init__(self): 
        self._view = View() 
        self._model = Vulnerability()
        self.username = ""
        self.password = ""

    def gui_loop(self): 
        root = Tk()
        root.geometry("300x300") 
        get_credentials(root, self)
        #creation_view = CreationView(root, self)
        root.mainloop()
        print(self.username)

    def start(self):
        #self.check_auth_terminal()
        self.check_auth_gui()

    def main_loop(self): 
        self._model.set_asset(self._view.get_asset_name())
        self._model.set_name(self._view.get_vuln_name())
        print("BASE SCORE:")
        vector_string = self._calculate_base_score()
        print("TEMPORAL SCORE:")
        vector_string += self._calculate_temp_score()
        print("ENVIRONMENTAL SCORE")
        vector_string += self._calculate_env_score()
        self._model.set_vector(vector_string)
        print(f"Asset Name: {self._model.get_name()}")
        print(f"Base Score: {self._model.get_base_score()}")
        print(f"Temporal Score: {self._model.get_temp_score()}")
        print(f"Environmental Score: {self._model.get_env_score()}")
        print(f"CVSS3.1 Vektor: {self._model.get_vector()}")
        values =  {"1": "Create PDF", "2": "Create TXT", "3": "Create JSON", "4": "Exit"}
        get_input = self._view.get_option(values)
        while get_input != "4": 
            if(get_input == "1" and "1" in values): 
                del values["1"]
                self.print_pdf()
            elif(get_input == "2" and "2" in values): 
                del values["2"]
                self.print_txt()
            elif(get_input == "3" and "3" in values): 
                del values["3"]
                self.print_json()
            else:
                pass

            get_input = self._view.get_option(values)
        

    def check_auth_terminal(self):
    
        if os.path.isfile('templates/auth.json'):
            user_input = self._view.get_credentials()
            hash_object = hashlib.sha256(user_input[1].encode('ascii'))
            hash_password = str(hash_object.hexdigest())


            with open('templates/auth.json') as auth:
                credentials = json.load(auth)

                if user_input[0] == credentials['user'] and hash_password == credentials['password']:
                    print('Login successful')
                    self.main_loop()

                else:
                    print('Login failed')
                    self.start()
        else:
            user_input = self._view.create_user()
            hash_object = hashlib.sha256(user_input[1].encode('ascii'))
            hash_password = str(hash_object.hexdigest())

            credentials = {
                'user': user_input[0],
                'password': hash_password

            }

            with open('templates/auth.json', 'w') as auth:
                json.dump(credentials, auth)
            
            print('Account is created')
            self.main_loop()

    def check_auth_gui(self):
    
        root = Tk()
        root.geometry("300x300") 
    
        if os.path.isfile('templates/auth.json'):
            tet = GetCredentials(root, self)
            root.mainloop()
            root.destroy()
            hash_object = hashlib.sha256(self.password.encode('ascii'))
            hash_password = str(hash_object.hexdigest())


            with open('templates/auth.json') as auth:
                credentials = json.load(auth)

                if self.username == credentials['user'] and hash_password == credentials['password']:
                    CreationView(root, self)
                    root.mainloop()
                
                else:
                    GetCredentials(root, self)
                    root.mainloop()
        else:
            user_input = self._view.create_user()
            hash_object = hashlib.sha256(self.password.encode('ascii'))
            hash_password = str(hash_object.hexdigest())

            credentials = {
                'user': self.username,
                'password': hash_password

            }

            with open('templates/auth.json', 'w') as auth:
                json.dump(credentials, auth)
            
            #start graphical
             

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
        with open('../templates/template_output_json.json') as out:
            JSON_OUT = json.load(out)
        
        JSON_OUT['asset_name'] = self._model.get_asset()
        JSON_OUT['vuln_name'] = self._model.get_name()
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
            TXT_OUT = TXT_OUT.replace('$asset_name$', self._model.get_asset())
            TXT_OUT = TXT_OUT.replace('$vul_name$', self._model.get_name())
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
            PDF_OUT = PDF_OUT.replace('$asset_name$', self._model.get_asset())
            PDF_OUT = PDF_OUT.replace('$vul_name$', self._model.get_name())
            PDF_OUT = PDF_OUT.replace('$base_score$', str(self._model.get_base_score()))
            PDF_OUT = PDF_OUT.replace('$temp_score$', str(self._model.get_temp_score()))
            PDF_OUT = PDF_OUT.replace('$env_score$', str(self._model.get_env_score()))
            vektor = str(self._model.get_vector())
            PDF_OUT = PDF_OUT.replace('$vektor1$', vektor[:69])
            PDF_OUT = PDF_OUT.replace('$vektor2$', vektor[69:])


            create_name = self._model.get_name() + '_output.tex'

            with open(create_name , 'w') as output:
                output.write(PDF_OUT)

        x = subprocess.call('pdflatex ' + create_name)

        extensions = ['.aux','.bcf','.lof','.log','.lot','.out','.run.xml','.toc' ,'.tex']
        os1 = {'Linux' : 'rm', 'Darwin': 'rm', 'Windows': 'del'}
        opertor = os1[platform.system()]
        for i in range(len(extensions)):
            os.system(opertor + ' ' + self._model.get_name()+ '_output' + extensions[i])



    def _set_name(self):
        print(self._view.get_name())

    def get_vector(self): 
        return self._model.get_vector()

    def set_metric(self, base_string, value=None):
        if value == None:
            self._model.set_vector(base_string)
        else: 
            self._model.set_metric(base_string, value)

    def print_hello(self): 
        print("Hello Wold!")

    def get_metric(self, type): 
        if type == "BASE": 
            return self._model.get_base_vector()
        elif type=="TEMP": 
            return self._model.get_temp_vector()
        elif type=="ENV": 
            return self._model.get_env_vector()
        else: 
            pass

    def get_base_score(self): 
        return self._model.get_base_score()

    def get_env_score(self): 
        return self._model.get_env_score()

    def get_temp_score(self): 
        return self._model.get_temp_score()

    def set_vul(self, value): 
        self._model.set_name(value)
    
    def set_asset(self, value):
        self._model.set_asset(value)
    
    def set_user(self, value):
        self.username = value
    
    def set_password(self, value):
        self.password = value