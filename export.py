import json, requests as r
from colorama import Fore

w = Fore.WHITE
rd = Fore.RED
lb = Fore.LIGHTBLACK_EX
mgn = Fore.MAGENTA
with open("config.json", "r") as f:
    data = json.load(f)
token = data["token"]

def exporter():
    headers = {
        "Authorization": token,
    }
    api = "https://discord.com/api/v10/users/@me/relationships"
    resp = r.get(api, headers=headers)
    
    if resp.status_code != 200:
        print(f"{lb}[{rd}!{lb}] {w}Error while fetching friends list")
        print(f"{lb}[{rd}!{lb}] {w}", resp.status_code, resp.text)
    relats = resp.json()
    
    if not isinstance(relats, list):
        print(f"{lb}[{rd}!{lb}] {w}Unexpected resp format")
        return
    
    with open("friends.txt", "w") as f:
        for rel in relats:
            if rel.get("type") == 1:
                user = rel.get("user")
                if not user:
                    continue
                username = user.get("username")
                user_id = user.get("id")
                if username and user_id:
                    f.write(f"{username} - {user_id}\n")

    print(f"{lb}[{mgn}*{lb}] {w}Friends Exported{w}")

if __name__ == "__main__":
    exporter()
