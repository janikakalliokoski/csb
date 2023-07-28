create table users (
    id integer primary key autoincrement,
    email text,
    username text unique,
    password text,
    admin boolean
);
