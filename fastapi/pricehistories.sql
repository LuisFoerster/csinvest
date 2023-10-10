create table pricehistories
(
    id         int auto_increment
        primary key,
    classid    varchar(64)                          null,
    vendorid   int                                  null,
    time_stamp datetime                             null,
    volume     int                                  null,
    price      float                                null,
    updated_at datetime default current_timestamp() null on update current_timestamp(),
    created_at datetime default current_timestamp() null,
    constraint unique_class_and_vendor_id_and_time_stamp
        unique (classid, vendorid, time_stamp),
    constraint pricehistories_ibfk_1
        foreign key (classid) references items (classid),
    constraint pricehistories_ibfk_2
        foreign key (vendorid) references vendors (id)
);

create index vendorid
    on pricehistories (vendorid);

