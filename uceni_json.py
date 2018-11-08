import json

json_retezec = """
    {
        "jméno": "Nona",
        "mesto": "Praha",
        "věk": 31,
        "jazyky": ["cestina", "anglictina", "python"]
    }
"""

data = json.loads(json_retezec)
print(data)
print(data["mesto"])
print(json.dumps(data))

print(json.dumps(data, ensure_ascii=False, indent=2))
