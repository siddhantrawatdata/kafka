

use  buy_online;
create table product_information
(
	id int not null,
    product_name varchar(500),
    category varchar(500),
    price float,
    created timestamp default current_timestamp,
    last_updated timestamp default current_timestamp on update current_timestamp,
	primary key (id)
);
