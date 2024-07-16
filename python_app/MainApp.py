from Database import Database
import sys


def main():

    database = Database()
    database.create_table()  # Ensure the table exists

    if len(sys.argv) < 2:
        print("Usage: python MainApp.py <operation> [<first_name> <last_name>]")
        print("Supported operations: ADD; DELETE; GET")
        sys.exit(1)

    operation = sys.argv[1].upper()

    if operation == "ADD" and len(sys.argv) == 4:
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        database.add_name(first_name, last_name)
        print(f"Added {first_name} {last_name} to the database.")
    elif operation == "DELETE" and len(sys.argv) == 4:
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        database.delete_name(first_name, last_name)
        print(f"Deleted {first_name} {last_name} from the database.")
    elif operation == "GET":
        names = database.get_names()
        for first_name, last_name in names:
            print(f"{first_name} {last_name}")
    else:
        print("Invalid operation or arguments.")
        print("Usage:")
        print("  python main.py ADD <first_name> <last_name>")
        print("  python main.py DELETE <first_name> <last_name>")
        print("  python main.py GET")
        sys.exit(1)


if __name__ == "__main__":
    main()
