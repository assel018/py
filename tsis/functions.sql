-- Function 1: Search contacts
-- Search by name, email or phone

CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    phone VARCHAR,
    phone_type VARCHAR,
    group_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
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
        ON p.id = ph.contact_id
    LEFT JOIN groups g
        ON p.group_id = g.id
    WHERE
        p.name ILIKE '%' || pattern || '%'
        OR p.email ILIKE '%' || pattern || '%'
        OR ph.phone ILIKE '%' || pattern || '%'
        OR g.name ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- Function 2: Pagination


CREATE OR REPLACE FUNCTION get_contacts_page(
    page_limit INT,
    page_offset INT
)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    phone VARCHAR,
    phone_type VARCHAR,
    group_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
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
        ON p.id = ph.contact_id
    LEFT JOIN groups g
        ON p.group_id = g.id
    ORDER BY p.id
    LIMIT page_limit
    OFFSET page_offset;
END;
$$ LANGUAGE plpgsql;