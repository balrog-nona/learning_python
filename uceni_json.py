import json

json_retezec = """
    {
        "jméno": "Nona",
        "mesto": "Praha",
        "věk": 31,
        "jazyky": ["cestina", "anglictina", "python"]
    }
"""

data = json.loads(json_retezec)  # nacte json retezec a premeni na dict
print(data)
print(type(data))
print(data["mesto"])  # pristup jako k beznemu dict
nove_data = json.dumps(data)  # zakoduje dict do json stringu
print(nove_data)
print(type(nove_data))

print(json.dumps(data, ensure_ascii=False, indent=2))  # kodovani do json stringu, aby to bylo citelne pro lidi
dalsi_data = json.dumps(data)
print(type(dalsi_data))  # je to opravdu string
