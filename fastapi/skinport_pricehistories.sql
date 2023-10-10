create table skinport_pricehistories
(
    id         int auto_increment
        primary key,
    classid    varchar(64)                          null,
    avg_price  float                                null,
    volume     int                                  null,
    updated_at datetime default current_timestamp() null on update current_timestamp(),
    created_at datetime default current_timestamp() null,
    constraint skinport_pricehistories_ibfk_1
        foreign key (classid) references items (classid)
);

create index classid
    on skinport_pricehistories (classid);

