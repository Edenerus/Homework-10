import json


def load_candidates():
    with open("candidates.json", mode='r', encoding='utf-8') as file:
        data_candidates = json.load(file)
        return data_candidates


def get_all():
    candidate_info = []
    for candidate in load_candidates():
        name_candidate = candidate["name"]
        position_candidate = candidate["position"]
        skills_candidate = candidate["skills"]
        candidate_info.append(f"Имя кандидата - {name_candidate}\nПозиция кандидата - {position_candidate}\nНавыки кандидата: {skills_candidate}\n")
    return '\n'.join(candidate_info)


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate["pk"] == int(pk):
            picture_candidate = candidate["picture"]
            name_candidate = candidate["name"]
            position_candidate = candidate["position"]
            skills_candidate = candidate["skills"]
            candidate_info = f"Имя кандидата - {name_candidate}\nПозиция кандидата - {position_candidate}\nНавыки кандидата: {skills_candidate}\n"
            return picture_candidate, candidate_info


def get_by_skill(skill):
    candidate_info = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].lower().split(', '):
            name_candidate = candidate["name"]
            position_candidate = candidate["position"]
            skills_candidate = candidate["skills"]
            candidate_info.append(f"Имя кандидата - {name_candidate}\nПозиция кандидата - {position_candidate}\nНавыки кандидата: {skills_candidate}\n")
    return '\n'.join(candidate_info)
