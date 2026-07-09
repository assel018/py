import csv
import json
import re
from datetime import datetime

from connect import get_connection
from config import MENU


# Validation

def validate_phone(phone):
    """
    Kazakhstan phone number:
    starts with 87
    contains exactly 11 digits
    """

    if re.fullmatch(r"87\d{9}", phone):
        return True

    print("\nInvalid phone number!")
    print("Phone must start with 87 and contain exactly 11 digits.\n")

    return False


def validate_email(email):

    if re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        return True

    print("\nInvalid email address.\n")
    return False


def validate_birthday(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:

        print("\nWrong birthday format.")
        print("Example: 2003-05-12\n")

        return False
    

def show_all():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            p.id,
            p.name,
            p.email,
            p.birthday,
            ph.phone,
            ph.type,
            g.name

        FROM phonebook p

        LEFT JOIN phones ph
            ON ph.contact_id=p.id

        LEFT JOIN groups g
            ON g.id=p.group_id

        ORDER BY p.id
    """)

    rows = cur.fetchall()

    if not rows:

        print("\nPhoneBook is empty.\n")

    else:

        print("\n---------------- CONTACTS ----------------")

        for row in rows:

            print(f"""
ID        : {row[0]}
Name      : {row[1]}
Email     : {row[2]}
Birthday  : {row[3]}
Phone     : {row[4]}
Type      : {row[5]}
Group     : {row[6]}
-------------------------------------------
""")

    cur.close()
    conn.close()


def insert_from_console():

    name = input("Name: ")
    
    if len(name.strip()) == 0:

      print("\nName cannot be empty.\n")
      return

    email = input("Email: ")

    if len(email.strip()) == 0:

        print("\nEmail cannot be empty.\n")
        return
    
    if not validate_email(email):
        return

    birthday = input("Birthday (YYYY-MM-DD): ")

    if not validate_birthday(birthday):
        return

    phone = input("Phone (87XXXXXXXXX): ")

    if not validate_phone(phone):
        return

    print("""
Phone type

1 Home
2 Work
3 Mobile
""")

    t = input("Choose: ")

    if t == "1":
        phone_type = "home"

    elif t == "2":
        phone_type = "work"

    else:
        phone_type = "mobile"

    print("""
    Choose group

    1. Family
    2. Friends
    3. Work
    4. Other
    """)

    g = input("Choose: ")

    if g == "1":
        group = "Family"

    elif g == "2":
        group = "Friends"

    elif g == "3":
        group = "Work"

    else:
        group = "Other"



    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM groups WHERE name=%s",
        (group,)
    )

    g = cur.fetchone()

    if g is None:

        cur.execute(
            "INSERT INTO groups(name) VALUES(%s) RETURNING id",
            (group,)
        )

        group_id = cur.fetchone()[0]

    else:

        group_id = g[0]


        cur.execute(
        """
        SELECT id
        FROM phonebook
        WHERE email=%s
        """,
        (email,)
    )

    if cur.fetchone():

        print("\nEmail already exists.\n")

        cur.close()
        conn.close()
        return
    cur.execute("""
        INSERT INTO phonebook(
            name,
            email,
            birthday,
            group_id
        )
        VALUES(%s,%s,%s,%s)
        RETURNING id
    """,
    (
        name,
        email,
        birthday,
        group_id
    ))

    contact_id = cur.fetchone()[0]

    # Check duplicate phone
    cur.execute(
                """
                SELECT id
                FROM phones
                WHERE phone=%s
                """,
                (phone,)
            )

    if cur.fetchone():

                print("\nPhone already exists.\n")

                cur.close()
                conn.close()
                return

    cur.execute("""
                INSERT INTO phones(
                    contact_id,
                    phone,
                    type
                )
                VALUES(%s,%s,%s)
            """,
            (
                contact_id,
                phone,
                phone_type
            ))

    conn.commit()

    print("\nContact added successfully.\n")

    cur.close()
    conn.close()


# Import contacts from CSV


def insert_from_csv():

    path = input("Enter CSV file path: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            name = row["name"]
            phone = row["phone"]
            email = row["email"]
            birthday = row["birthday"]
            group = row["group"]
            phone_type = row["phone_type"]

            if not validate_phone(phone):
                continue

            if not validate_email(email):
                continue

            if not validate_birthday(birthday):
                continue

            # group
            cur.execute(
                "SELECT id FROM groups WHERE name=%s",
                (group,)
            )

            g = cur.fetchone()

            if g is None:

                cur.execute(
                    """
                    INSERT INTO groups(name)
                    VALUES(%s)
                    RETURNING id
                    """,
                    (group,)
                )

                group_id = cur.fetchone()[0]

            else:

                group_id = g[0]

            # duplicate email


            cur.execute(
                """
                SELECT id
                FROM phonebook
                WHERE email=%s
                """,
                (email,)
            )

            if cur.fetchone():

                print(f"Email '{email}' already exists. Skipped.")
                continue


            # duplicate phone

            cur.execute(
                """
                SELECT id
                FROM phones
                WHERE phone=%s
                """,
                (phone,)
            )

            if cur.fetchone():

                print(f"Phone '{phone}' already exists. Skipped.")
                continue
            # contact

            cur.execute(
                """
                INSERT INTO phonebook(
                    name,
                    email,
                    birthday,
                    group_id
                )
                VALUES(%s,%s,%s,%s)
                RETURNING id
                """,
                (
                    name,
                    email,
                    birthday,
                    group_id
                )
            )

            contact_id = cur.fetchone()[0]

            # phone

            cur.execute(
                """
                INSERT INTO phones(
                    contact_id,
                    phone,
                    type
                )
                VALUES(%s,%s,%s)
                ON CONFLICT(phone)
                DO NOTHING
                """,
                (
                    contact_id,
                    phone,
                    phone_type
                )
            )

        conn.commit()

        print("\nCSV imported successfully.\n")

        cur.close()
        conn.close()


# Export contacts to JSON

def export_json():

    filename = input("JSON filename: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        SELECT

            p.name,
            p.email,
            p.birthday,
            ph.phone,
            ph.type,
            g.name

        FROM phonebook p

        LEFT JOIN phones ph
            ON p.id=ph.contact_id

        LEFT JOIN groups g
            ON g.id=p.group_id

        ORDER BY p.id

    """)

    rows = cur.fetchall()

    contacts = []

    for row in rows:

        contacts.append({

            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "phone": row[3],
            "phone_type": row[4],
            "group": row[5]

        })

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            contacts,
            file,
            indent=4
        )

    print("\nJSON exported successfully.\n")

    cur.close()
    conn.close()


# Import contacts from JSON

def import_json():

    filename = input("JSON filename: ")

    with open(filename, "r", encoding="utf-8") as file:

        contacts = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for contact in contacts:

        name = contact["name"]
        email = contact["email"]
        birthday = contact["birthday"]
        phone = contact["phone"]
        phone_type = contact["phone_type"]
        group = contact["group"]

        cur.execute(
            """
            SELECT id
            FROM phonebook
            WHERE name=%s
            """,
            (name,)
        )

        existing = cur.fetchone()

        if existing:

            print(f"\n{name} already exists.")

            action = input(
                "Skip or Overwrite? (s/o): "
            ).lower()

            if action == "s":
                continue

            elif action != "o":

                print("Wrong choice.")
                continue

            cur.execute(
                """
                DELETE FROM phonebook
                WHERE name=%s
                """,
                (name,)
            )
        # group

        cur.execute(
            """
            SELECT id
            FROM groups
            WHERE name=%s
            """,
            (group,)
        )

        g = cur.fetchone()

        if g is None:

            cur.execute(
                """
                INSERT INTO groups(name)
                VALUES(%s)
                RETURNING id
                """,
                (group,)
            )

            group_id = cur.fetchone()[0]

        else:

            group_id = g[0]

        cur.execute(
            """
            INSERT INTO phonebook(
                name,
                email,
                birthday,
                group_id
            )
            VALUES(%s,%s,%s,%s)
            RETURNING id
            """,
            (
                name,
                email,
                birthday,
                group_id
            )
        )

        contact_id = cur.fetchone()[0]

        cur.execute(
            """
            INSERT INTO phones(
                contact_id,
                phone,
                type
            )
            VALUES(%s,%s,%s)
            """,
            (
                contact_id,
                phone,
                phone_type
            )
        )

    conn.commit()

    print("\nJSON imported successfully.\n")

    cur.close()
    conn.close()


# Update Contact


def update_contact():

    name = input("Enter contact name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM phonebook
        WHERE name=%s
        """,
        (name,)
    )

    result = cur.fetchone()

    if not result:

        print("\nContact not found.\n")

        cur.close()
        conn.close()
        return

    contact_id = result[0]

    print("""
1. Update Email
2. Update Birthday
3. Update Phone
4. Update Group
""")

    choice = input("Choose: ")

    if choice == "1":

        email = input("New email: ")

        if not validate_email(email):
            cur.close()
            conn.close()
            return

        cur.execute(
            """
            UPDATE phonebook
            SET email=%s
            WHERE id=%s
            """,
            (email, contact_id)
        )

    elif choice == "2":

        birthday = input("Birthday (YYYY-MM-DD): ")

        if not validate_birthday(birthday):
            cur.close()
            conn.close()
            return

        cur.execute(
            """
            UPDATE phonebook
            SET birthday=%s
            WHERE id=%s
            """,
            (birthday, contact_id)
        )

    elif choice == "3":

        phone = input("New phone: ")

        if not validate_phone(phone):
            cur.close()
            conn.close()
            return

        cur.execute(
            """
            UPDATE phones
            SET phone=%s
            WHERE contact_id=%s
            """,
            (phone, contact_id)
        )

    elif choice == "4":

        group = input("New group: ")

        cur.execute(
            """
            SELECT id
            FROM groups
            WHERE name=%s
            """,
            (group,)
        )

        row = cur.fetchone()

        if row:

            group_id = row[0]

        else:

            cur.execute(
                """
                INSERT INTO groups(name)
                VALUES(%s)
                RETURNING id
                """,
                (group,)
            )

            group_id = cur.fetchone()[0]

        cur.execute(
            """
            UPDATE phonebook
            SET group_id=%s
            WHERE id=%s
            """,
            (group_id, contact_id)
        )

    else:

        print("Wrong choice.")

        cur.close()
        conn.close()
        return

    conn.commit()

    print("\nContact updated successfully.\n")

    cur.close()
    conn.close()


# Search Contact

def search_contact():

    pattern = input("Enter name, phone or email: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM search_contacts(%s)",
        (pattern,)
    )

    rows = cur.fetchall()

    if not rows:

        print("\nNothing found.\n")

    else:

        print("\n------------- RESULTS -------------")

        for row in rows:

            print(f"""
ID        : {row[0]}
Name      : {row[1]}
Email     : {row[2]}
Birthday  : {row[3]}
Phone     : {row[4]}
Type      : {row[5]}
Group     : {row[6]}
------------------------------------
""")

    cur.close()
    conn.close()



# Filter by Group

def filter_by_group():

    group = input("Enter group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            p.id,
            p.name,
            p.email,
            p.birthday,
            ph.phone,
            ph.type,
            g.name

        FROM phonebook p

        LEFT JOIN phones ph
            ON p.id=ph.contact_id

        LEFT JOIN groups g
            ON p.group_id=g.id

        WHERE g.name=%s

        ORDER BY p.id
        """,
        (group,)
    )

    rows = cur.fetchall()

    if not rows:

        print("\nNo contacts found.\n")

    else:

        for row in rows:

            print(f"""
ID        : {row[0]}
Name      : {row[1]}
Email     : {row[2]}
Birthday  : {row[3]}
Phone     : {row[4]}
Type      : {row[5]}
Group     : {row[6]}
------------------------------------
""")

    cur.close()
    conn.close()


# ==========================================
# Sort Contacts
# ==========================================

def sort_contacts():

    print("""
Sort by

1 Name
2 Birthday
3 Date Added
""")

    choice = input("Choose: ")

    if choice == "1":
        order = "name"

    elif choice == "2":
        order = "birthday"

    else:
        order = "created_at"

    conn = get_connection()
    cur = conn.cursor()

    query = f"""
        SELECT
            p.id,
            p.name,
            p.email,
            p.birthday,
            ph.phone,
            ph.type,
            g.name

        FROM phonebook p

        LEFT JOIN phones ph
            ON p.id=ph.contact_id

        LEFT JOIN groups g
            ON p.group_id=g.id

        ORDER BY p.{order}
    """

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:

        print(f"""
ID        : {row[0]}
Name      : {row[1]}
Email     : {row[2]}
Birthday  : {row[3]}
Phone     : {row[4]}
Type      : {row[5]}
Group     : {row[6]}
------------------------------------
""")

    cur.close()
    conn.close()



# ==========================================
# Pagination
# ==========================================

def pagination():

    limit = 5
    offset = 0

    while True:

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM get_contacts_page(%s,%s)",
            (limit, offset)
        )

        rows = cur.fetchall()

        print("\n=========== PAGE ===========")

        if not rows:
            print("No contacts.")

        else:

            for row in rows:

                print(f"""
ID        : {row[0]}
Name      : {row[1]}
Email     : {row[2]}
Birthday  : {row[3]}
Phone     : {row[4]}
Type      : {row[5]}
Group     : {row[6]}
------------------------------------
""")

        cur.close()
        conn.close()

        print("""
n - next page
p - previous page
q - quit
""")

        choice = input("Choose: ").lower()

        if choice == "n":

            offset += limit

        elif choice == "p":

            offset = max(0, offset - limit)

        elif choice == "q":

            break

        else:

            print("Wrong choice.")


# Add Phone

def add_phone():

    name = input("Contact name: ")

    phone = input("Phone: ")

    if not validate_phone(phone):
        return

    print("""
Phone type

1 Home
2 Work
3 Mobile
""")

    t = input("Choose: ")

    if t == "1":
        phone_type = "home"

    elif t == "2":
        phone_type = "work"

    else:
        phone_type = "mobile"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL add_phone(%s,%s,%s)",
        (
            name,
            phone,
            phone_type
        )
    )

    conn.commit()

    print("\nPhone added successfully.\n")

    cur.close()
    conn.close()


# Move Contact to Group
def move_contact():

    name = input("Contact name: ")

    group = input("New group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL move_to_group(%s,%s)",
        (
            name,
            group
        )
    )

    conn.commit()

    print("\nGroup updated.\n")

    cur.close()
    conn.close()



# Delete Contact


def delete_contact():

    value = input("Enter contact name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL delete_contact(%s)",
        (value,)
    )

    conn.commit()

    print("\nContact deleted.\n")

    cur.close()
    conn.close()


# ==========================================
# Main
# ==========================================

def main():

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

            search_contact()

        elif choice == "8":

            pagination()

        elif choice == "9":

            filter_by_group()

        elif choice == "10":

            sort_contacts()

        elif choice == "11":

            export_json()

        elif choice == "12":

            import_json()

        elif choice == "13":

            add_phone()

        elif choice == "14":

            move_contact()

        elif choice == "15":

            print("\nGoodbye!\n")
            break

        else:

            print("Invalid option.")


    if __name__ == "__main__":
          main()