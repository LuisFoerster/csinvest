create table users
(
    id         int auto_increment
        primary key,
    username   text                                 null,
    role       varchar(32)                          null,
    last_login datetime                             null,
    updated_at datetime default current_timestamp() null on update current_timestamp(),
    created_at datetime default current_timestamp() null,
    constraint username
        unique (username) using hash
);

