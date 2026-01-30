import sys
import os

# نضيف مسار root المشروع لبايثون
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from app.db import projects_collection
from app.services.project_service import (
    create_project,
    request_join,
    approve_request,
    reject_request
)


# Example CLI usage
project = create_project("Cloud Project", "Project from CLI", "ayat")
print("Project created")
result = request_join(project, "user2")
print(result)
result = approve_request(project, "user2")
print(result)

