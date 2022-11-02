import json

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
print(type(person))

person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)