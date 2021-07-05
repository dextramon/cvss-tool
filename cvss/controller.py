
import os
import platform
import subprocess
import json 
import hashlib
from vulnerability import Vulnerability
from tkinter import *
from tkinter import ttk
from graphical import CreationView
from graphical import GetCredentials
from graphical import CreateUser

#JSON Integration
with open('../templates/data.json') as f:
    data = json.load(f)

class Controller: 
    def __init__(self): 
        self._model = Vulnerability()
        self.username = ""
        self.password = ""
        self.msg = ""

    def gui_loop(self): 
        root = Tk()
        #get_credentials(root, self)
        self._view = CreationView(root, self)
        root.mainloop()

    def start(self):
        self.msg = "Please enter your credentials"
        self.check_auth_gui()

    def check_auth_gui(self):
    
        if os.path.isfile('../templates/auth.json'):

            GetCredentials(self, self.msg)
            
            if self.username == "" and self.password == "":
                 return False
            else:
                hash_object = hashlib.sha256(self.password.encode('ascii'))
                hash_password = str(hash_object.hexdigest())



                with open('templates/auth.json') as auth:
                   credentials = json.load(auth)


                if self.username == credentials['user'] and hash_password == credentials['password']:
                        self.username = ""
                        self.password = ""
                        self.gui_loop()
                        return True

                else:
                        self.username = ""
                        self.password = ""
                        self.msg = "wrong username or password"
                        self.check_auth_gui()
                        return False
        else:

            CreateUser(self)

            hash_object = hashlib.sha256(self.password.encode('ascii'))
            hash_password = str(hash_object.hexdigest())

            credentials = {
                'user': self.username,
                'password': hash_password

            }

            with open('../templates/auth.json', 'w') as auth:
                json.dump(credentials, auth)
            
            self.username = ""
            self.password = ""
            
            self.gui_loop()
            return "set"
    
    def set_user(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password
    
    def set_msg(self, msg):
        self.mdg = msg

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
        with open('../templates/template_output_txt.txt' , 'r') as file:
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

    def _set_name(self):
        print(self._view.get_name())

    def get_vector(self): 
        return self._model.get_vector()

    def set_metric(self, base_string, value=None):
        if value == None:
            self._model.set_vector(base_string)
        else: 
            self._model.set_metric(base_string, value)

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
    
    def get_user(self):
        return self.username
    
    def set_password(self, value):
        self.password = value
    
    def get_password(self):
        return self.password

