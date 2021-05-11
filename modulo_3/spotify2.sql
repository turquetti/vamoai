create table plano(
	assinatura varchar(10) not null unique
);

alter table album add column ano varchar(4);

drop table playlist;