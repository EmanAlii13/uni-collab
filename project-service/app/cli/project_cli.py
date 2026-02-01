import argparse

from app.services.project_service import approve_request, create_project, join_project


def main():
    parser = argparse.ArgumentParser(description="Project CLI")
    subparsers = parser.add_subparsers(dest="command")

    # ----- Create project -----
    create_parser = subparsers.add_parser("create-project")
    create_parser.add_argument("--title", required=True)
    create_parser.add_argument("--desc", required=True)
    create_parser.add_argument("--leader", required=True)

    # ----- Join project -----
    join_parser = subparsers.add_parser("join-project")
    join_parser.add_argument("--project-id", required=True)
    join_parser.add_argument("--user-id", required=True)

    # ----- Approve request -----
    approve_parser = subparsers.add_parser("approve-request")
    approve_parser.add_argument("--project-id", required=True)
    approve_parser.add_argument("--user-id", required=True)

    args = parser.parse_args()

    if args.command == "create-project":
        create_project(args.title, args.desc, args.leader)
    elif args.command == "join-project":
        success, msg = join_project(args.project_id, args.user_id)
        print(msg)
    elif args.command == "approve-request":
        success, msg = approve_request(args.project_id, args.user_id)
        print(msg)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
