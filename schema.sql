CREATE TABLE users (
    id serial PRIMARY KEY,
    firstname varchar(255),
    lastname varchar(255),
    email varchar(255) NOT NULL,
    pwdhash varchar(255)
);

CREATE TABLE items (
    id serial PRIMARY KEY,
    name varchar(255),
    details text,
    user_id int references users(id)
);
