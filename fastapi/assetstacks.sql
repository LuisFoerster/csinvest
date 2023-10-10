create table assetstacks
(
    id           int auto_increment
        primary key,
    classid      varchar(64)                          null,
    steamid      varchar(64)                          null,
    buyin        float                                null,
    virtual      tinyint(1)                           null,
    virtual_size int                                  null,
    updated_at   datetime default current_timestamp() null on update current_timestamp(),
    created_at   datetime default current_timestamp() null,
    constraint assetstacks_ibfk_1
        foreign key (classid) references items (classid),
    constraint assetstacks_ibfk_2
        foreign key (steamid) references accounts (steamid)
);

create index classid
    on assetstacks (classid);

create index steamid
    on assetstacks (steamid);

