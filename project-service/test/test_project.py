from app.services.project_service import create_project, request_join

def test_join_request():
    project = create_project("Test", "Desc", "leader")
    result = request_join(project, "user2")
    assert result == "Request sent"
