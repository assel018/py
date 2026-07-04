import csv
from connect import get_connection
from config import MENU


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    if not rows:
        print("PhoneBook is empty.")
    else:
        print("\n----- CONTACTS -----")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    cur.close()
    conn.close()


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO phonebook(name, phone)
        VALUES (%s, %s)
        """,
        (name, phone)
    )

    conn.commit()

    print("Contact added successfully.")

    cur.close()
    conn.close()


def insert_from_csv():
    path = input("Enter CSV file path: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
    next(reader)

    for row in reader:
        print(row)   # ← добавь эту строку

        cur.execute(
            """
            INSERT INTO phonebook(name, phone)
            VALUES (%s, %s)
            ON CONFLICT(phone) DO NOTHING
            """,
            (row[0], row[1])
        )

    conn.commit()

    print("CSV imported successfully.")

    cur.close()
    conn.close()


def update_contact():
    print("1. Update name")
    print("2. Update phone")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        old_name = input("Current name: ")
        new_name = input("New name: ")

        cur.execute(
            """
            UPDATE phonebook
            SET name=%s
            WHERE name=%s
            """,
            (new_name, old_name)
        )

    elif choice == "2":
        old_phone = input("Current phone: ")
        new_phone = input("New phone: ")

        cur.execute(
            """
            UPDATE phonebook
            SET phone=%s
            WHERE phone=%s
            """,
            (new_phone, old_phone)
        )

    else:
        print("Wrong choice.")
        cur.close()
        conn.close()
        return

    conn.commit()

    print("Contact updated.")

    cur.close()
    conn.close()


def search_contact():
    print("1. Search by name")
    print("2. Search by phone prefix")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")

        cur.execute(
            """
            SELECT * FROM phonebook
            WHERE name ILIKE %s
            """,
            ("%" + name + "%",)
        )

    elif choice == "2":
        prefix = input("Phone prefix: ")

        cur.execute(
            """
            SELECT * FROM phonebook
            WHERE phone LIKE %s
            """,
            (prefix + "%",)
        )

    else:
        print("Wrong choice.")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()

    if not rows:
        print("Nothing found.")
    else:
        print("\nResults:")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    cur.close()
    conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")

        cur.execute(
            """
            DELETE FROM phonebook
            WHERE name=%s
            """,
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")

        cur.execute(
            """
            DELETE FROM phonebook
            WHERE phone=%s
            """,
            (phone,)
        )

    else:
        print("Wrong choice.")
        cur.close()
        conn.close()
        return

    conn.commit()

    print("Contact deleted.")

    cur.close()
    conn.close()


def main():
    create_table()

    while True:
        print(MENU)

        choice = input("Choose option: ")

        if choice == "1":
            show_all()

        elif choice == "2":
            insert_from_console()

        elif choice == "3":
            insert_from_csv()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            search_contact()

        elif choice == "6":
            delete_contact()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()