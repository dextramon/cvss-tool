

from tkinter import *
from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractclassmethod

def return_temp(): 
    dic = {
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
            "R": {
                "description": "f", 
                "name": "Unknown",
                "value": 0,
            },
        }
    },
    
}
    return dic

def return_env(): 
    dic = {
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
    return dic

def return_dict(): 
    dic = {
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
    return dic



class Controller:
    def __init__(self): 
        root = Tk() 
        root.geometry("400x400")
        mv = auth(root, self)
        # mv = CreationView(root, self)
        root.mainloop()

class BaseView(tk.Toplevel): 
    def __init__(self, parent, value, brother):
        super().__init__(parent)

        self.geometry("300x300")
        self.mainframe = ttk.Frame(self)
        self._tv = {"AV": StringVar(), "AC": StringVar(), "PR": StringVar(), "UI": StringVar(), "S": StringVar(), "C": StringVar(), "I": StringVar(), "A":StringVar()}
        base_dict = return_dict()

        self.value = value
        # This frame is needed ot have access to the function of the previous frame, to enable it
        self.brother = brother

        self.view_label = ttk.Label(self.mainframe, text="Base Metrics: ")
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)
        
        self.view_label.grid()
        # TO-DO This button has to be put blow create_labels once ScrollView is implemented
        self.submit_button.grid()
        self.create_labels(base_dict)
        self.mainframe.grid()

    def print_text(self):
        output_string = f'AV:{self._tv["AV"].get()}/AC:{self._tv["AC"].get()}/PR:{self._tv["PR"].get()}/UI:{self._tv["UI"].get()}/S:{self._tv["S"].get()}/C:{self._tv["C"].get()}/I:{self._tv["I"].get()}/A:{self._tv["A"].get()}'
        self.brother.controller.set_metric(output_string)
        self.value.set(self.brother.controller.get_metric(type="BASE"))
        self.brother.base_score_var.set(self.brother.controller.get_base_score())
        self.brother.controller.print_hello()
        self.brother.check_status()

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self._tv[i], values=i, dict=return_dict())


class TempView(tk.Toplevel): 
    def __init__(self, parent, value, brother):
        super().__init__(parent)
        self.geometry("300x300")
        self.mainframe = ttk.Frame(self)
        self.value_hold = {"E": StringVar(), "RL": StringVar(), "RC": StringVar()}
        temp_dict = return_temp()
        self.value = value
        self.brother = brother

        self.view_label = ttk.Label(self.mainframe, text="Temporal Metrics: ")
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)
        
        self.view_label.grid()
        # TO-DO This button has to be put blow create_labels once ScrollView is implemented
        self.submit_button.grid()
        self.create_labels(temp_dict)
        self.mainframe.grid()

    def print_text(self):
        for i in self.value_hold: 
            print(self.value_hold[i])
            self.brother.controller.set_metric(i, self.value_hold[i].get())
        self.value.set(self.brother.controller.get_metric(type="TEMP"))
        self.brother.temp_score_var.set(self.brother.controller.get_temp_score())
        self.brother.check_status()

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self.value_hold[i], values=i, dict=return_temp(), val="X")


class EnvView(tk.Toplevel): 
    def __init__(self, parent, value, brother):
        super().__init__(parent)
        self.geometry("300x300")
        self.mainframe = ttk.Frame(self)
        self.value_hold = {"CR": StringVar(), "IR": StringVar(), "AR": StringVar(), "MAV": StringVar(), "MAC": StringVar(), "MPR": StringVar(), "MUI": StringVar(), "MS": StringVar(), "MC": StringVar(), "MI": StringVar(), "MA":StringVar()}
        env_dict = return_env()
        self.value = value

        self.brother=brother

        self.view_label = ttk.Label(self.mainframe, text="Environmental Score: ")
        self.submit_button = ttk.Button(self.mainframe, text="Press", command=self.print_text)
        
        self.view_label.grid()
        # TO-DO This button has to be put blow create_labels once ScrollView is implemented
        self.submit_button.grid()
        self.create_labels(env_dict)
        self.mainframe.grid()

    def print_text(self):
        for i in self.value_hold: 
            print(self.value_hold[i])
            self.brother.controller.set_metric(i, self.value_hold[i].get())
        self.value.set(self.brother.controller.get_metric(type="ENV"))
        self.brother.env_score_var.set(self.brother.controller.get_env_score())
        self.brother.check_status()

    def create_labels(self, dict_values): 
        for i in dict_values:
            metric_label = ttk.Label(self.mainframe, text=dict_values[i]["name"])
            metric_label.grid()
            MetricOptions(parent=self.mainframe, valueholder=self.value_hold[i], values=i, dict=return_env(), val="X")


class CreationView: 
    def __init__(self, parent, controller): 
        self.frame = ttk.Frame(parent)

        self.controller = controller
        self.vul_str = StringVar()
        vul_name = ttk.Label(self.frame, text="Vulnerability Name: ")
        vul_entry = ttk.Entry(self.frame, textvariable=self.vul_str)

        self.asset_str = StringVar() 
        asset_name = ttk.Label(self.frame, text="Asste Name: ")
        asset_entry = ttk.Entry(self.frame, textvariable=self.asset_str)

        self.button = ttk.Button(self.frame, text="submit", command=self.submit_form, state=DISABLED)

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
        temp_score_button = ttk.Button(self.frame, textvariable=self.temp_score_button_var, command=self.temp_top_level ,width=50)

        env_score = ttk.Label(self.frame, text="Environmental Score: ")
        self.env_score_var = DoubleVar()
        self.env_score_var.set(0.0)
        env_score_value = ttk.Label(self.frame, textvariable=self.env_score_var)
        self.env_score_button_var =  StringVar() 
        self.env_score_button_var.set("Not set yet!")
        env_score_button = ttk.Button(self.frame, textvariable=self.env_score_button_var, command=self.env_top_level, width=50)


        asset_name.grid(column=0,row=0, columnspan=2) 
        asset_entry.grid(column=0,row=1, columnspan=2)
        vul_name.grid(column=0,row=2, columnspan=2)
        vul_entry.grid(column=0,row=3, columnspan=2)
        base_score.grid(column=0,row=4)
        base_score_value.grid(column=1, row=4)
        base_score_button.grid(column=0,row=5, columnspan=2)
        temp_score.grid(column=0, row=6)
        temp_score_value.grid(column=1, row=6)
        temp_score_button.grid(column=0, row=7, columnspan=2)
        env_score.grid(column=0, row=8)
        env_score_value.grid(column=1, row=8)
        env_score_button.grid(column=0, row=9, columnspan=2)

        self.button.grid(column=0, row=10, columnspan=2)

        self.frame.grid() 

    def submit_form(self): 
        self.controller.set_vul(self.vul_str.get())
        self.controller.set_asset(self.asset_str.get())
        self.controller.print_txt()

    def base_top_level(self): 
        t1 = BaseView(self.frame, self.base_score_button_var, self)

    def temp_top_level(self): 
        t1 = TempView(self.frame, self.temp_score_button_var, self)

    def env_top_level(self): 
        t1 = EnvView(self.frame, self.env_score_button_var, self)

    def check_status(self): 
        if self.base_score_button_var.get() != "Not set yet!": 
            self.button.configure(state=NORMAL)


class MetricOptions: 
    def __init__(self, parent, valueholder, values, dict, val=None): 
        self.mainframe = ttk.Frame(parent)

        if val == None: 
            valueholder.set("")
        else: 
            valueholder.set("X")

        for i in dict[values]["options"]:
            self.option = ttk.Radiobutton(self.mainframe, text=dict[values]["options"][i]["name"], variable=valueholder, value=i)
            self.option.grid()
        self.mainframe.grid()



class GetCredentials: 
    def __init__(self, parent, controller): 
        self.frame = ttk.Frame(parent)

        self.controller = controller

        self.user_str = StringVar()
        user_name = ttk.Label(self.frame, text="Username ")
        user_entry = ttk.Entry(self.frame, textvariable=self.user_str)

        self.password_str = StringVar() 
        password_name = ttk.Label(self.frame, text="Password ")
        password_entry = ttk.Entry(self.frame, textvariable=self.password_str)

        self.button = ttk.Button(self.frame, text="submit", command=self.submit_form, state=ACTIVE)

        user_name.grid(column=0,row=2, columnspan=2)
        user_entry.grid(column=0,row=3, columnspan=2)
        password_name.grid(column=0,row=0, columnspan=2) 
        password_entry.grid(column=0,row=1, columnspan=2)
        self.button.grid(column=0, row=10, columnspan=2)

        self.frame.grid() 

    def submit_form(self): 
        self.controller.set_user(self.user_str.get())
        self.controller.set_password(self.password_str.get())
        
class create_user: 
    def __init__(self, parent, controller): 
        self.frame = ttk.Frame(parent)

        self.controller = controller

        self.user_str = StringVar()
        user_name = ttk.Label(self.frame, text="Username ")
        user_entry = ttk.Entry(self.frame, textvariable=self.user_str)

        self.password_str = StringVar() 
        password_name = ttk.Label(self.frame, text="Password ")
        password_entry = ttk.Entry(self.frame, textvariable=self.password_str)

        self.button = ttk.Button(self.frame, text="submit", command=self.submit_form, state=DISABLED)

        user_name.grid(column=0,row=2, columnspan=2)
        user_entry.grid(column=0,row=3, columnspan=2)
        password_name.grid(column=0,row=0, columnspan=2) 
        password_entry.grid(column=0,row=1, columnspan=2)
        self.button.grid(column=0, row=10, columnspan=2)

        self.frame.grid() 

    def submit_form(self): 
        self.controller.set_vul(self.vul_str.get())
        self.controller.set_asset(self.asset_str.get())
        self.controller.print_txt()

    def check_status(self): 
        if self.base_score_button_var.get() != "Not set yet!": 
            self.button.configure(state=NORMAL)

if __name__ == "__main__": 

    c = Controller()

