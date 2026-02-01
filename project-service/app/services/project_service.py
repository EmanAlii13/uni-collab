import os

class ProjectService:
    def __init__(self, storage=None):
        """
        storage: إما مسار ملف (str/Path) أو كائن storage يدعم load() و save()
        """
        if storage is None:
            from .storage import JSONStorage
            storage_path = os.path.join(os.path.dirname(__file__), "../data.json")
            self.storage = JSONStorage(storage_path)
        elif isinstance(storage, str) or isinstance(storage, os.PathLike):
            from .storage import JSONStorage
            self.storage = JSONStorage(storage)
        else:
            # نفترض أنه كائن storage جاهز
            self.storage = storage

        # تحميل البيانات
        try:
            self.data = self.storage.load()
        except FileNotFoundError:
            self.data = {"projects": {}}

        # التأكد من وجود projects
        if "projects" not in self.data or not isinstance(self.data["projects"], dict):
            self.data["projects"] = {}

    def save_data(self):
        self.storage.save(self.data)

    def create_project(self, title, desc, leader):
        project_id = str(len(self.data["projects"]) + 1)
        self.data["projects"][project_id] = {
            "title": title,
            "desc": desc,
            "leader": leader,
            "members": []
        }
        self.save_data()
        return project_id

    def join_project(self, project_id, member):
        if project_id in self.data["projects"]:
            self.data["projects"][project_id]["members"].append(member)
            self.save_data()
            return True
        return False
