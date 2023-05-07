"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

while True:
    try:
        state_code = input("Enter short state: ").upper()
        name = CODE_TO_NAME[state_code]
        print(f"{state_code} is {name}")
    except KeyError:
        print("Invalid short state")
    except KeyboardInterrupt:
        print("Exit")
        break
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")
