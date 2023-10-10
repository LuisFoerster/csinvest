create table vendors
(
    id         int auto_increment
        primary key,
    name       text                                 null,
    provision  float                                null,
    icon_url   text                                 null,
    updated_at datetime default current_timestamp() null on update current_timestamp(),
    created_at datetime default current_timestamp() null
);

