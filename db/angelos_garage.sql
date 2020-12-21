DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    website VARCHAR(255)
);

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE, -- if a manufacturer is deleted, all related cars will be removed too.
    manufacturer VARCHAR(255),
    model VARCHAR(255),
    engine_size VARCHAR(255),
    colour VARCHAR(255),
    mileage INT,
    year INT,
    purchase_cost INT,
    selling_price INT,
    profit INT
);