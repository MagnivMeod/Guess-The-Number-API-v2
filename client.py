import requests, json

session = requests.session()

r = session.get("http://localhost:1337/api/start_game")

header = {"content-type": "application/json"}

data = {"guess": 0}

if r.json()["success"]:
    while True:
        data["guess"] = int(input("Guess the number >> "))
        r = session.post("http://localhost:1337/api/guess_the_number", data=json.dumps(data), headers=header)
        print(r.json())
        json_data = r.json()
        if json_data["status"] == "you win":
            break
else:
    print("Can't play the game")