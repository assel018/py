-- Procedure 1
-- Insert or Update Contact

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_email VARCHAR,
    p_birthday DATE
)
LANGUAGE plpgsql
AS $$
BEGIN

    IF EXISTS(
        SELECT 1
        FROM phonebook
        WHERE name = p_name
    ) THEN

        UPDATE phonebook
        SET
            email = p_email,
            birthday = p_birthday
        WHERE name = p_name;

    ELSE

        INSERT INTO phonebook(
            name,
            email,
            birthday
        )
        VALUES(
            p_name,
            p_email,
            p_birthday
        );

    END IF;

END;
$$;




-- Procedure 2
-- Add phone number


CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    c_id INT;
BEGIN

    SELECT id
    INTO c_id
    FROM phonebook
    WHERE name = p_contact_name;

    INSERT INTO phones(
        contact_id,
        phone,
        type
    )
    VALUES(
        c_id,
        p_phone,
        p_type
    );

END;
$$;




-- Procedure 3
-- Move contact to another group
-- Creates group if it doesn't exist


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE

    g_id INT;

BEGIN

    SELECT id
    INTO g_id
    FROM groups
    WHERE name = p_group_name;

    IF g_id IS NULL THEN

        INSERT INTO groups(name)
        VALUES(p_group_name);

        SELECT id
        INTO g_id
        FROM groups
        WHERE name = p_group_name;

    END IF;

    UPDATE phonebook
    SET group_id = g_id
    WHERE name = p_contact_name;

END;
$$;




-- Procedure 4
-- Delete contact


CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM phonebook
    WHERE name = p_value;

END;
$$;