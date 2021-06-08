
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

    def get_option(self, options): 
        answer = ""
        for i in options:
            print((i + ": " + options[i]))

        answer = input()
        return answer
    
    def get_credentials(self):
        user_input = []
        user_input.append(input("username: "))
        user_input.append(input("password: "))

        return user_input

    def create_user(self):
        user_input = []
        print('Create a new user')
        user_input.append(input("username: "))
        user_input.append(input("password: "))

        return user_input