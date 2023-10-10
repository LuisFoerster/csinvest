create table assets
(
    assetid       varchar(64)                          not null
        primary key,
    classid       varchar(64)                          null,
    steamid       varchar(64)                          null,
    asset_stackid int                                  null,
    instanceid    varchar(64)                          null,
    appid         int                                  null,
    contextid     varchar(64)                          null,
    amount        int                                  null,
    updated_at    datetime default current_timestamp() null on update current_timestamp(),
    created_at    datetime default current_timestamp() null,
    constraint assets_ibfk_1
        foreign key (asset_stackid) references assetstacks (id),
    constraint assets_ibfk_2
        foreign key (classid) references items (classid),
    constraint assets_ibfk_3
        foreign key (steamid) references accounts (steamid)
);

create index asset_stackid
    on assets (asset_stackid);

create index classid
    on assets (classid);

create index steamid
    on assets (steamid);

