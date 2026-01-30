from app.db import projects_collection

def create_project(title, description, leader_id):
    project = {
        "title": title,
        "description": description,
        "leader_id": leader_id,
        "team_ids": [leader_id],
        "join_requests": []
    }

    projects_collection.insert_one(project)
    return project


def request_join(project, user_id):
    if user_id in project["team_ids"]:
        return "Already in team"

    if len(project["team_ids"]) >= 3:
        return "Team is full"

    project["join_requests"].append(user_id)
    return "Request sent"

def approve_request(project, user_id):
    if user_id in project["join_requests"]:
        project["join_requests"].remove(user_id)
        project["team_ids"].append(user_id)
        return "Approved"
    return "No such request"

def reject_request(project, user_id):
    if user_id in project["join_requests"]:
        project["join_requests"].remove(user_id)
        return "Rejected"
    return "No such request"
