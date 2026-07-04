-- Procedure 1: Insert or Update Contact
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE name = p_name
    ) THEN

        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;

    ELSE

        INSERT INTO phonebook(name, phone)
        VALUES(p_name, p_phone);

    END IF;
END;
$$;


-- Procedure 2: Insert many contacts with phone validation
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names VARCHAR[],
    phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN

    FOR i IN 1..array_length(names,1)
    LOOP

        IF phones[i] ~ '^[0-9]{11}$' THEN

            CALL upsert_contact(names[i], phones[i]);

        ELSE

            RAISE NOTICE
            'Invalid phone: % (%)',
            names[i],
            phones[i];

        END IF;

    END LOOP;

END;
$$;


-- Procedure 3: Delete contact
CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM phonebook
    WHERE name = p_value
       OR phone = p_value;

END;
$$;