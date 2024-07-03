import json
def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        return json.load(file)

def get_by_id(id):
    for i in load_candidates():
        if i['id'] == id:
            return i
        
def get_by_name(name):
    a = []
    for i in load_candidates():
        if name in i['name']:
            a.append(i) 
    return a


def get_by_skill(skill_name):
    a = []
    for i in load_candidates():
        if skill_name in i['skills']:
            a.append(i)
    return a
