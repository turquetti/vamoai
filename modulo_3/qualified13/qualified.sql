create table cliente(
id int primary key,
nome varchar(50) not null,
sobrenome varchar(50) not null,
email varchar(50) not null,
data_cadastro varchar(50) not null
);

create table venda(
id int primary key,
cliente_id integer,
data_venda varchar(50) not null,
foreign key (cliente_id) references cliente(id)
);

create table produto(
id int primary key,
nome varchar(50) not null,
preco decimal(10,2) not null
);

create table produto_venda(
id int primary key,
venda_id integer,
produto_id integer not null,
quantidade integer not null,
foreign key (venda_id) references venda(id),
foreign key (produto_id) references produto(id)
);

COPY cliente (id, nome, sobrenome, email, data_cadastro)
FROM '/home/cliente.csv'
DELIMITER ','
CSV header

COPY produto (id, nome, preco)
FROM '/home/produto.csv'
DELIMITER ','
CSV header

COPY venda (id, cliente_id, data_venda)
FROM '/home/venda.csv'
DELIMITER ','
CSV header

COPY produto_venda (id, venda_id, produto_id, quantidade)
FROM '/home/produto_venda.csv'
DELIMITER ','
CSV header

select * from cliente limit 10;

select nome, sobrenome, email from cliente limit 20;

select nome, preco from produto limit 15;

select * from venda limit 10;

select venda_id, produto_id, quantidade from produto_venda limit 10;

select * from produto 
where preco > 15 
limit 10;

select * from produto_venda
where quantidade > 10 and quantidade < 20
limit 10;