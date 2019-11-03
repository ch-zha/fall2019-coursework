-- #1
create index vendor_zip_code_index
	on vendors (vendor_zip_code);

-- #2
drop table if exists members_committees;
drop table if exists members;
drop table if exists committees;
create table members
(
    member_id	int		primary key 	auto_increment,
    first_name	varchar(50),
    last_name	varchar(50),
    address		varchar(50),
    city		varchar(50),
    state		varchar(50),
    phone		int	
);

create table committees
(
	committee_id	int		primary key		auto_increment,
    committee_name	varchar(50)
);

create table members_committees
(
	member_id		int	not null,
    committee_id	int	not null,
    constraint members_committees_fk_member
		foreign key (member_id)
        references members (member_id),
	constraint members_committees_fk_committee
		foreign key (committee_id)
        references committees (committee_id)
);

-- #3
insert members values
	(default, 'John', 'Smith', '123 Street St', 'CA', '123-456-7890'),
    (default, 'Jane', 'Doe', '456 Way Way', 'CA', '234-567-8901');

insert committees values
	(default, 'Committee A'),
    (default, 'Committee B');

insert members_committees values
	(1, 2),
    (2, 1),
    (2, 2);

-- #4
alter table members
	add annual_dues		decimal(5, 2)	default 52.50,
    add payment_date	date;

-- #5
alter table committees
	modify committee_name varchar(50) unique;

insert committees values
	(default, 'Committee B');

select * from committees;