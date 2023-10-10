create table vendor_offers
(
    id             int auto_increment
        primary key,
    classid        varchar(64)                          null,
    vendorid       int                                  null,
    affiliate_link text                                 null,
    lowest_price   float                                null,
    median_price   float                                null,
    sell_listings  int                                  null,
    updated_at     datetime default current_timestamp() null on update current_timestamp(),
    created_at     datetime default current_timestamp() null,
    constraint unique_class_and_vendor_id
        unique (classid, vendorid),
    constraint vendor_offers_ibfk_1
        foreign key (classid) references items (classid),
    constraint vendor_offers_ibfk_2
        foreign key (vendorid) references vendors (id)
);

create index vendorid
    on vendor_offers (vendorid);

