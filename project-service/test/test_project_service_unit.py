from app.services.project_service import (
    approve_request,
    create_project,
    join_project,
    load_projects,
)


def test_create_project():
    project = create_project("Test Project", "Description", "leader1")
    assert project["title"] == "Test Project"
    assert project["leader"] == "leader1"
    assert "members" in project
    assert project["members"] == ["leader1"]


def test_join_project():
    project = create_project("Join Test", "Desc", "leader2")
    success, msg = join_project(project["_id"], "user1")
    projects = load_projects()
    project = next(p for p in projects if p["_id"] == project["_id"])
    assert success
    assert msg == "Request sent"
    assert "user1" in project["requests"]


def test_approve_request():
    project = create_project("Test Approve", "Desc", "leader3")
    join_project(project["_id"], "user2")
    success, msg = approve_request(project["_id"], "user2")
    projects = load_projects()
    project = next(p for p in projects if p["_id"] == project["_id"])
    assert success
    assert msg == "Approved"
    assert "user2" in project["members"]
