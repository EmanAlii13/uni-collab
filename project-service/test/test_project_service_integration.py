import subprocess


def test_cli_create_join_approve():
    # ----- Step 1: Create Project -----
    result_create = subprocess.run(
        [
            "python",
            "app/cli/project_cli.py",
            "create-project",
            "--title",
            "AI Project",
            "--desc",
            "ML System",
            "--leader",
            "ayat",
        ],
        capture_output=True,
        text=True,
    )
    print("CREATE OUTPUT:", result_create.stdout)

    # قراءة _id من stdout
    lines = [
        line.strip()
        for line in result_create.stdout.splitlines()
        if line.strip() and "Project created successfully" not in line
    ]
    if not lines:
        raise Exception("CLI did not return project ID")
    project_id = lines[-1]

    # ----- Step 2: Join Project -----
    result_join = subprocess.run(
        [
            "python",
            "app/cli/project_cli.py",
            "join-project",
            "--project-id",
            project_id,
            "--user-id",
            "lama",
        ],
        capture_output=True,
        text=True,
    )
    print("JOIN OUTPUT:", result_join.stdout)
    assert "Request sent" in result_join.stdout

    # ----- Step 3: Approve Request -----
    result_approve = subprocess.run(
        [
            "python",
            "app/cli/project_cli.py",
            "approve-request",
            "--project-id",
            project_id,
            "--user-id",
            "lama",
        ],
        capture_output=True,
        text=True,
    )
    print("APPROVE OUTPUT:", result_approve.stdout)
    assert "Approved" in result_approve.stdout
