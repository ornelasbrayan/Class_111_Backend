--Create status table
CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(256)
);

--Create task table
CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    status_id INTEGER,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY(status_id) REFERENCES status(id)
);

--populatw status table
INSERT INTO status (name) VALUES ("to do");
INSERT INTO status (name) VALUES ("in progress");
INSERT INTO status (name) VALUES ("done");


--add dummy data to task:
INSERT INTO task(
    summary,
    description,
    status_id
) VALUES (
    "Do the laundry",
    "Put clothes in the washing machine",
    1
);
INSERT INTO task(
    summary,
    description,
    status_id
) VALUES (
    "Buy groceries",
    "Go to the grocery store and buy stuff",
    1
);
INSERT INTO task(
    summary,
    description,
    status_id
) VALUES (
    "Walk the dog",
    "Walk Fido out for a stroll",
    1
);