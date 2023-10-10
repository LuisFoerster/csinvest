create table items
(
    classid          varchar(64)                          not null
        primary key,
    appid            int                                  null,
    market_hash_name text                                 null,
    name             text                                 null,
    item_nameid      varchar(64)                          null,
    icon_url         text                                 null,
    background_color varchar(64)                          null,
    name_color       varchar(64)                          null,
    type             text                                 null,
    updated_at       datetime default current_timestamp() null on update current_timestamp(),
    created_at       datetime default current_timestamp() null
);

