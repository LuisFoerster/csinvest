create table accounts
(
    steamid      varchar(64)                          not null
        primary key,
    personame    text                                 null,
    avatar       text                                 null,
    avatarmedium text                                 null,
    avatarfull   text                                 null,
    updated_at   datetime default current_timestamp() null on update current_timestamp(),
    created_at   datetime default current_timestamp() null
);

