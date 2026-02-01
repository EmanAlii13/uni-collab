import json
import os
import uuid

PROJECTS_FILE = "app/data/projects.json"


def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)


def save_projects(projects):
    with open(PROJECTS_FILE, "w") as f:
        json.dump(projects, f, indent=2)


def create_project(title, desc, leader):
    projects = load_projects()
    project = {
        "_id": str(uuid.uuid4()),
        "title": title,
        "desc": desc,
        "leader": leader,
        "members": [leader],  # Leader becomes a member automatically
        "requests": [],
    }
    projects.append(project)
    save_projects(projects)
    print("Project created successfully")
    print(project["_id"])
    return project


def join_project(project_id, user_id):
    projects = load_projects()
    for project in projects:
        if project["_id"] == project_id:
            if user_id in project["members"] or user_id in project["requests"]:
                return False, "Already joined or requested"
            project["requests"].append(user_id)
            save_projects(projects)
            return True, "Request sent"
    return False, "Project not found"


def approve_request(project_id, user_id):
    projects = load_projects()
    for project in projects:
        if project["_id"] == project_id:
            if user_id in project["requests"]:
                project["requests"].remove(user_id)
                project["members"].append(user_id)
                save_projects(projects)
                return True, "Approved"
            return False, "Request not found"
    return False, "Project not found"
