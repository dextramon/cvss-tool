

from os import EX_CANTCREAT
from tkinter import *
from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractclassmethod

class BaseView(tk.Toplevel): 

    def __init__(self, parent, value, brother):
        super().__init__(parent)

        self.mainframe = ttk.Frame(self)
        self._tv = {"AV": StringVar(), "AC": StringVar(), "PR": StringVar(), "UI": StringVar(), "S": StringVar(), "C": StringVar(), "I": StringVar(), "A":StringVar()}
        self.error_var = StringVar()
        self.title("cvvslator Base")

        self.value = value
        # This frame is needed ot have access to the function of the previous frame, to enable it
        self.brother = brother

        self.view_label = ttk.Label(self.mainframe, text="Base Metrics: ")
        self.error_label = ttk.Label(self.mainframe, textvariable=self.error_var)
        
        self.view_label.grid(pady=10)
        # TO-DO This button has to be put blow create_labels once ScrollView is implemented
        self.create_labels(self._get_base_metrics())
        self.mainframe.grid(pady=10, padx=10)
        self.error_label.grid(pady=10)
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)
        self.submit_button.grid()


    def print_text(self):
        
        output_string = f'AV:{self._tv["AV"].get()}/AC:{self._tv["AC"].get()}/PR:{self._tv["PR"].get()}/UI:{self._tv["UI"].get()}/S:{self._tv["S"].get()}/C:{self._tv["C"].get()}/I:{self._tv["I"].get()}/A:{self._tv["A"].get()}'
        
        try:
            self.brother.controller.set_metric(output_string)
            self.value.set(self.brother.controller.get_metric(type="BASE"))
            self.brother.base_score_var.set(self.brother.controller.get_base_score())
            self.brother.temp_score_var.set(self.brother.controller.get_temp_score())
            self.brother.env_score_var.set(self.brother.controller.get_env_score())
            self.brother.check_status()
            self.brother.destroy_top_level(self)
        except Exception:
            self.error_var.set("YOU HAVE TO SELECT ALL VALUES")

    def _get_base_metrics(self):
        return {
            "AV": {
            "name": "Attack Vector", 
            "options": {
                "N": {
                    "description": "asd",
                    "name": "Network",
                    "value": 0,
                },
                "A": {
                    "description": "asd",
                    "name": "Adjacent",
                    "value": 0,
                },
                "L": {
                    "description": "asd",
                    "name": "Local",
                    "value": 0,
                },
                "P": {
                    "description": "asd",
                    "name": "Physical",
                    "value": 0,
                },
            }
        }, 
        "AC": {
        "name": "Attack Complexity", 
        "options": {
            "L": {
                "description": "", 
                "name": "Low",
                "value": 0,
            },
            "H": {
                "description": "", 
                "name": "High",
                "value": 0,
            }
        }
    }, 
    "PR": {
        "name": "Privileges Required", 
        "options": {
            "N": {
                "description": "", 
                "name": "None",
                "value": 0,
            },
            "H": {
                "description": "", 
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "f", 
                "name": "Low",
                "value": 0,
            },
        }
    },
    "UI": {
        "name": "User Interaction",
        "options": {
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
            "R": {
                "description": "",
                "name": "Required",
                "value": 0,
            }
        }
    },
    "S": {
        "name": "Scope", 
        "options": {
            "C": {
                "description": "",
                "name": "Changed",
                "value": 0, 
            }, 
            "U": {
                "description": "",
                "name": "Unchanged",
                "value": 0,
            }
        }
    }, 
    "C": {
        "name": "Confidentiality",
        "options": {
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    },
    "I": {
        "name": "Integrity",
        "options": {
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    },
    "A": {
        "name": "Availability",
        "options": {
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    }
}

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self._tv[i], values=i, dict=self._get_base_metrics())

class TempView(tk.Toplevel): 
    def __init__(self, parent, value, brother):
        super().__init__(parent)
        self.mainframe = ttk.Frame(self)
        self.value_hold = {"E": StringVar(), "RL": StringVar(), "RC": StringVar()}
        self.value = value
        self.title("cvvslator Temporal")
        self.brother = brother

        self.view_label = ttk.Label(self.mainframe, text="Temporal Metrics: ") 
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)

        self.view_label.grid(pady=10)
        self.create_labels(self._get_temp_metrics())
        self.submit_button.grid()
        self.mainframe.grid(pady=10, padx=10)

    def print_text(self):
        for i in self.value_hold: 
            self.brother.controller.set_metric(i, self.value_hold[i].get())
        self.value.set(self.brother.controller.get_metric(type="TEMP"))
        self.brother.temp_score_var.set(self.brother.controller.get_temp_score())
        self.brother.check_status()
        self.brother.destroy_top_level(self)

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self.value_hold[i], values=i, dict=self._get_temp_metrics(), val="X")

    def _get_temp_metrics(self):
        return  {
        "E": {
            "name": "Exploit Code Maturity", 
            "options": {
                "X": {
                    "description": "asd",
                    "name": "Not Defined",
                    "value": 0,
                },
                "H": {
                    "description": "asd",
                    "name": "High",
                    "value": 0,
                },
                "F": {
                    "description": "asd",
                    "name": "Functional",
                    "value": 0,
                },
                "P": {
                    "description": "asd",
                    "name": "Proof Of Concept",
                    "value": 0,
                },
                "U": {
                    "description": "asd",
                    "name": "Unproven",
                    "value": 0,
                },
            }
        }, 
    "RL": {
        "name": "Remidation Level", 
        "options": {
            "X": {
                "description": "", 
                "name": "Not Defined",
                "value": 0,
            },
            "U": {
                "description": "", 
                "name": "Unavailable",
                "value": 0,
            },
            "W": {
                "description": "", 
                "name": "Workaround",
                "value": 0,
            },
            "T": {
                "description": "", 
                "name": "Temporary Fix",
                "value": 0,
            },
            "O": {
                "description": "", 
                "name": "Official Fix",
                "value": 0,
            }
        }
    }, 
    "RC": {
        "name": "Remidation Confidence", 
        "options": {
            "X": {
                "description": "", 
                "name": "Not Defined",
                "value": 0,
            },
            "C": {
                "description": "", 
                "name": "Confirmed",
                "value": 0,
            },
            "R": {
                "description": "f", 
                "name": "Reasonable",
                "value": 0,
            },
            "U": {
                "description": "f", 
                "name": "Unknown",
                "value": 0,
            },
        }
    },
    
}


class EnvView(tk.Toplevel): 
    def __init__(self, parent, value, brother):
        super().__init__(parent)
        self.mainframe = ttk.Frame(self)
        self.value_hold = {"CR": StringVar(), "IR": StringVar(), "AR": StringVar(), "MAV": StringVar(), "MAC": StringVar(), "MPR": StringVar(), "MUI": StringVar(), "MS": StringVar(), "MC": StringVar(), "MI": StringVar(), "MA":StringVar()}
        self.value = value
        self.title("cvvslator Environmental")
        self.brother=brother

        self.view_label = ttk.Label(self.mainframe, text="Environmental Score: ")
        
        self.view_label.grid(pady=10)
        # TO-DO This button has to be put blow create_labels once ScrollView is implemented
        self.create_labels(self._get_env_metric())
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)
        self.submit_button.grid()
        self.mainframe.grid(pady=10, padx=10)

    def print_text(self):
        for i in self.value_hold: 
            self.brother.controller.set_metric(i, self.value_hold[i].get())
        self.value.set(self.brother.controller.get_metric(type="ENV"))
        self.brother.env_score_var.set(self.brother.controller.get_env_score())
        self.brother.check_status()
        self.brother.destroy_top_level(self)

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self.value_hold[i], values=i, dict=self._get_env_metric(), val="X")

    def _get_env_metric(self):
        return {
        "CR": {
            "name": "Confidentiality Requirement", 
            "options": {
                "X": {
                    "description": "NIY",
                    "name": "Not Defined",
                    "value": 0,
                },
                "H": {
                    "description": "DIY",
                    "name": "High",
                    "value": 0,
                },
                "M": {
                    "description": "DIY",
                    "name": "Medium",
                    "value": 0,
                },
                "L": {
                    "description": "DIY",
                    "name": "Low",
                    "value": 0,
                },
            }
        },
        "IR": {
            "name": "Integrity Requirement", 
            "options": {
                "X": {
                    "description": "NIY",
                    "name": "Not Defined",
                    "value": 0,
                },
                "H": {
                    "description": "DIY",
                    "name": "High",
                    "value": 0,
                },
                "M": {
                    "description": "DIY",
                    "name": "Medium",
                    "value": 0,
                },
                "L": {
                    "description": "DIY",
                    "name": "Low",
                    "value": 0,
                },
            }
        },
        "AR": {
            "name": "Availability Requirement", 
            "options": {
                "X": {
                    "description": "NIY",
                    "name": "Not Defined",
                    "value": 0,
                },
                "H": {
                    "description": "DIY",
                    "name": "High",
                    "value": 0,
                },
                "M": {
                    "description": "DIY",
                    "name": "Medium",
                    "value": 0,
                },
                "L": {
                    "description": "DIY",
                    "name": "Low",
                    "value": 0,
                },
            }
        },
        "MAV": {
        "name": "Modified Attack Vector", 
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "N": {
                "description": "asd",
                "name": "Network",
                "value": 0,
            },
            "A": {
                "description": "asd",
                "name": "Adjacent",
                "value": 0,
            },
            "L": {
                "description": "asd",
                "name": "Local",
                "value": 0,
            },
            "P": {
                "description": "asd",
                "name": "Physical",
                "value": 0,
            },
        }
        }, 
        "MAC": {
        "name": "Modified Attack Complexity", 
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "L": {
                "description": "", 
                "name": "Low",
                "value": 0,
            },
            "H": {
                "description": "", 
                "name": "High",
                "value": 0,
            }
        }
    }, 
    "MPR": {
        "name": "Modified Privileges Required", 
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "N": {
                "description": "", 
                "name": "None",
                "value": 0,
            },
            "H": {
                "description": "", 
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "f", 
                "name": "Low",
                "value": 0,
            },
        }
    },
    "MUI": {
        "name": "Modified User Interaction",
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
            "R": {
                "description": "",
                "name": "Required",
                "value": 0,
            }
        }
    },
    "MS": {
        "name": "Modified Scope", 
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "C": {
                "description": "",
                "name": "Changed",
                "value": 0, 
            }, 
            "U": {
                "description": "",
                "name": "Unchanged",
                "value": 0,
            }
        }
    }, 
    "MC": {
        "name": "Modified Confidentiality",
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    },
    "MI": {
        "name": "Modified Integrity",
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    },
    "MA": {
        "name": "Modified Availability",
        "options": {
            "X": {
                "description": "NIY",
                "name": "Not Defined",
                "value": 0,
            },
            "H": {
                "description": "",
                "name": "High",
                "value": 0,
            },
            "L": {
                "description": "",
                "name": "Low",
                "value": 0,
            },
            "N": {
                "description": "",
                "name": "None",
                "value": 0,
            },
        }
    }
}


class CreationView: 
    def __init__(self, parent, controller): 
        self.frame = ttk.Frame(parent)

        self.t1 = None 

        self.controller = controller
        self.vul_str = StringVar()
        vul_name = ttk.Label(self.frame, text="Vulnerability Name: ")
        vul_entry = ttk.Entry(self.frame, textvariable=self.vul_str, width=50)

        self.asset_str = StringVar() 
        asset_name = ttk.Label(self.frame, text="Asset Name: ")
        asset_entry = ttk.Entry(self.frame, textvariable=self.asset_str, width=50)

        self.txtbutton = ttk.Button(self.frame, text="Print .TXT", command=self.submit_txt, state=DISABLED)
        self.jsonbutton = ttk.Button(self.frame, text="Print .JSON", command=self.submit_json, state=DISABLED)

        base_score = ttk.Label(self.frame, text="Base Score: ")
        self.base_score_var = DoubleVar()
        self.base_score_var.set(0.0)
        base_score_value = ttk.Label(self.frame, textvariable=self.base_score_var)
        self.base_score_button_var =  StringVar() 
        self.base_score_button_var.set("Not set yet!")
        base_score_button = ttk.Button(self.frame, textvariable=self.base_score_button_var, command=self.base_top_level, width=50)

        temp_score = ttk.Label(self.frame, text="Temporal Score: ")
        self.temp_score_var = DoubleVar()
        self.temp_score_var.set(0.0)
        temp_score_value = ttk.Label(self.frame, textvariable=self.temp_score_var)
        self.temp_score_button_var =  StringVar() 
        self.temp_score_button_var.set("Not set yet!")
        self.temp_score_button = ttk.Button(self.frame, textvariable=self.temp_score_button_var, command=self.temp_top_level ,width=50, state=DISABLED)

        env_score = ttk.Label(self.frame, text="Environmental Score: ")
        self.env_score_var = DoubleVar()
        self.env_score_var.set(0.0)
        env_score_value = ttk.Label(self.frame, textvariable=self.env_score_var)
        self.status_var = StringVar()
        self.status_label = ttk.Label(self.frame, textvariable=self.status_var)
        self.env_score_button_var =  StringVar() 
        self.env_score_button_var.set("Not set yet!")
        self.env_score_button = ttk.Button(self.frame, textvariable=self.env_score_button_var, command=self.env_top_level, width=50, state=DISABLED)


        asset_name.grid(column=0,row=0, columnspan=2, pady=5) 
        asset_entry.grid(column=0,row=1, columnspan=2, pady=5)
        vul_name.grid(column=0,row=2, columnspan=2, pady=5)
        vul_entry.grid(column=0,row=3, columnspan=2, pady=5)
        base_score.grid(column=0,row=4, pady=5)
        base_score_value.grid(column=1, row=4)
        base_score_button.grid(column=0,row=5, columnspan=2)
        temp_score.grid(column=0, row=6, pady=5)
        temp_score_value.grid(column=1, row=6)
        self.temp_score_button.grid(column=0, row=7, columnspan=2)
        env_score.grid(column=0, row=8, pady=5)
        env_score_value.grid(column=1, row=8)
        self.env_score_button.grid(column=0, row=9, columnspan=2)


        self.status_label.grid(column=0, columnspan=2, row=10 ,pady=10)
        self.txtbutton.grid(column=0, row=11,pady=10)
        self.jsonbutton.grid(column=1, row=11, pady=10)

        self.frame.grid(padx=10, pady=10) 

    def submit_txt(self): 
        self.controller.set_vul(self.vul_str.get())
        self.controller.set_asset(self.asset_str.get())
        self.status_var.set(f"{self.asset_str.get()}.txt has been created!")
        self.controller.print_txt()

    def submit_json(self): 
        self.controller.set_vul(self.vul_str.get())
        self.controller.set_asset(self.asset_str.get())

        if self.controller.print_json() == True:
        	self.status_var.set(f"{self.asset_str.get()}.json has been created!")                
        else:
        	self.status_var.set("JSON Template is corrupted!")

    def destroy_top_level(self, view):
        view.destroy()

    def base_top_level(self): 
        BaseView(self.frame, self.base_score_button_var, self)

    def temp_top_level(self): 
        TempView(self.frame, self.temp_score_button_var, self)

    def env_top_level(self): 
        EnvView(self.frame, self.env_score_button_var, self)

    def check_status(self): 
        if self.base_score_button_var.get() != "Not set yet!": 
            self.txtbutton.configure(state=NORMAL)
            self.jsonbutton.configure(state=NORMAL)
            self.env_score_button.configure(state=NORMAL)
            self.env_score_button_var.set(self.controller.get_metric(type="ENV"))
            self.temp_score_button_var.set(self.controller.get_metric(type="TEMP"))
            self.temp_score_button.configure(state=NORMAL)


class MetricOptions: 
    def __init__(self, parent, valueholder, values, dict, val=None): 
        self.mainframe = ttk.Frame(parent)

        if val == None: 
            valueholder.set("")
        else: 
            valueholder.set("X")

        for h,i in enumerate(dict[values]["options"]):
            self.option = ttk.Radiobutton(self.mainframe, text=dict[values]["options"][i]["name"], variable=valueholder, value=i)
            self.option.grid(column=h, row=0)
        self.mainframe.grid()

class GetCredentials: 
    def __init__(self, controller, msg): 
        self.root = Tk()
        self.root.title('cvsslator Login')
        self.root.resizable(False,False)

        self.frame = ttk.Frame(self.root)
        self.controller = controller

        self.msg = StringVar()
        msg = ttk.Label(self.frame, text=msg)

        self.user_str = StringVar()
        user_name = ttk.Label(self.frame, text="Username")
        user_entry = ttk.Entry(self.frame, textvariable=self.user_str)

        self.password_str = StringVar() 
        password_name = ttk.Label(self.frame, text="Password")
        password_entry = ttk.Entry(self.frame,show="*", textvariable=self.password_str)

        self.button = ttk.Button(self.frame, text="Submit", command=self.submit_form, state=ACTIVE)

        msg.grid(column=0,row=0, pady=10)
        user_name.grid(column=0, row=1)
        user_entry.grid(column=0,row=2)
        password_name.grid(column=0, row=3)
        password_entry.grid(column=0, row=4)
        self.button.grid(column=0, row=5, pady=10)

        self.frame.grid(padx=25, pady=25) 

        self.root.mainloop()

    def submit_form(self): 
        if self.user_str.get() == "" and self.password_str.get() == "": 
                self.root.destroy()
                GetCredentials(self.controller, "Field may not be empty")
        else:
            self.controller.set_user(self.user_str.get())
            self.controller.set_password(self.password_str.get())
            self.root.destroy()

    
class CreateUser: 
    def __init__(self, controller): 
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.title('cvsslator Registrierung')
        self.frame = ttk.Frame(self.root)
        self.controller = controller

        self.notification_var = StringVar()
        title_label = ttk.Label(self.frame, text="CREATE YOUR ACCOUNT")
        notification_label = ttk.Label(self.frame, textvariable=self.notification_var)

        self.user_str = StringVar()
        user_name = ttk.Label(self.frame, text="Username")
        user_entry = ttk.Entry(self.frame, textvariable=self.user_str)

        self.password_str = StringVar() 
        password_name = ttk.Label(self.frame, text="Password")
        password_entry = ttk.Entry(self.frame, show="*", textvariable=self.password_str)

        self.button = ttk.Button(self.frame, text="Submit", command=self.submit_form, state=ACTIVE)

        title_label.grid(column=0,row=0, pady=10)
        notification_label.grid(column=0, row=1)
        user_name.grid(column=0, row=2)
        user_entry.grid(column=0,row=3)
        password_name.grid(column=0, row=4)
        password_entry.grid(column=0, row=5)
        self.button.grid(column=0, row=6, pady=10)

        self.frame.grid(padx=25, pady=25) 

        self.root.mainloop()

    def submit_form(self): 
        if self.user_str.get() == "" or self.password_str.get() == "" or len(self.password_str.get()) < 8: 
            self.notification_var.set("Choose a strong combination")
        else:
            self.controller.check_auth = True
            self.controller.set_user(self.user_str.get())
            self.controller.set_password(self.password_str.get())
            self.root.destroy()
  
