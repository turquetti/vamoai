CREATE TABLE tb_cliente (
	id_cliente SERIAL NOT NULL,
	nome varchar(50) NULL,
	email varchar(50) NULL,
	endereco varchar(200) NULL,
    PRIMARY KEY (id_cliente)
);

CREATE TABLE tb_pizza(
	id_pizza SERIAL NOT NULL,
    nome varchar(100) NULL,
    descricao varchar(200) NULL,
    categoria varchar(50) NULL,
    preco float8 NULL,
	PRIMARY KEY (id_pizza)
);

CREATE TABLE tb_pedido(
	id_pedido SERIAL NOT NULL,
    id_cliente int NOT NULL,
    observacao varchar(500) NULL,
    tipo_entrega varchar(20) NOT NULL,
    preco float8 NULL,
    data_pedido timestamp NULL,
	PRIMARY KEY (id_pedido),
    CONSTRAINT tb_pedido_fk_id_cliente FOREIGN KEY (id_cliente) REFERENCES tb_cliente (id_cliente)
);

CREATE TABLE tb_pedido_pizza(
	id_pedido int NOT NULL,
	id_pizza int NOT NULL,
	quantidade varchar(10) DEFAULT NULL,
    CONSTRAINT tb_pedido_pizza_fk_id_pedido FOREIGN KEY (id_pedido) REFERENCES tb_pedido (id_pedido),
    CONSTRAINT tb_pedido_pizza_fk_id_pizza FOREIGN KEY (id_pizza) REFERENCES tb_pizza (id_pizza)
);

INSERT INTO tb_cliente (nome,email,endereco) VALUES
	 ('Francisco Jose','franc@xpto.com','av. Beltrano, numero 32, apt. 13, Centro'),
	 ('Antonio Luiz','ant_luz@fb.com','rua das Flores, quadra B, numero 2, Liberdade'),
	 ('Belchior Lopez','blopez@fb.com','rua Projetada, numero 2, Lagos'),
	 ('Maria Jose','jmaria21@xpto.com','av. Embaixador Luiz, numero 3, Centro'),
	 ('Jose de Ribamar','joseribas@yes.com','av. Beira mar, numero 33, Lagoa Amarela'),
	 ('Maria Fernanda','mary100@fb.com','av. Rocha, numero 5, Rio Vermelho'),
	 ('Michael Rey','mrey@xpto.com','rua das Flores, quadra C, numero 12, Liberdade'),
	 ('Lara Goncalves','lg@yes.com','av. Embaixador Luiz, numero 13, Centro'),
	 ('Julia da Silva','juju_s@fb.com','av. beira mar, numero 25, Lagoa Amarela'),
	 ('Raimundo Nonato','rai7@xpto.com','av. Rocha, numero 12, Rio Vermelho'),
	 ('Enzo Gabriel','gabriel_enzo@fb.com','av. Olimpica, numero 10, apt. 102, Centro'),
	 ('Valentina Rangel','val_rangel@xpto.com','rua 4, quadra B, numero 3, Montes Altos');

INSERT INTO tb_pizza (nome,descricao,categoria,preco) VALUES
     ('BACON COM CATUPIRY', 'Molho de tomate, queijo mozarela, fatias de bacon e Catupiry', 'Tradicionais', 55.0),
     ('CALABRESA COM CATUPIRY', 'Molho de tomate, queijo mozarela, calabresa fatiada Cerati, Catupiry, cebola e orégano', 'Tradicionais', 50.0),
     ('MARGUERITA ESPECIAL', 'Molho de tomate, queijo mozarela, tomate confit, queijo parmesão ralado na hora e manjericão', 'Tradicionais', 45.0),
     ('PORTUGUESA', 'Molho de tomate, queijo mozarela, presunto, ovo, cebola, azeitona preta e orégano', 'Tradicionais', 50.0),
     ('CAPRESE', 'Molho de tomate, queijo mozarela, mozarela de búfala, molho pesto, tomate cereja e manjericão', 'Especiais', 60.0),
     ('PALETA SUÍNA DEFUMADA COM GELEIA DE PIMENTA', 'Molho de tomate, queijo mozarela, paleta suína defumada e geleia de pimenta', 'Especiais', 60.0),
     ('PEPPERONI AO PESTO', 'Molho de tomate, queijo mozarela, pepperoni, e molho pesto', 'Especiais', 55.0),
     ('QUATRO QUEIJOS', 'Molho de tomate, queijos gorgonzola, provolone, mozarela e parmesão ralado na hora', 'Especiais', 60.0),
     ('ROMEU E JULIETA', 'Queijo mozarela, pedaços de goiabada e queijo parmesão ralado na hora', 'Especiais', 40.0),
     ('TOMATE SECO COM RÚCULA', 'Molho de tomate, queijo mozarela, mozarela de búfala, tomate seco, rúcula e parmesão ralado na hora', 'Especiais', 60.0),
     ('BACON ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, fatias de bacon', 'Zero Lactose', 55.0),
     ('CALABRESA ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, calabresa fatiada Cerati, Catupiry, cebola e orégano', 'Zero Lactose', 55.0),
     ('MARGUERITA ESPECIAL ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, tomate confit e manjericão', 'Zero Lactose', 55.0),
     ('PORTUGUESA ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, presunto, ovo, cebola, azeitona preta e orégano', 'Zero Lactose', 55.0),
     ('PALETA SUÍNA DEFUMADA COM GELEIA DE PIMENTA ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, paleta suína defumada e geleia de pimenta', 'Zero Lactose', 60.0),
     ('PEPPERONI AO PESTO ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, pepperoni, e molho pesto', 'Zero Lactose', 55.0),
     ('ROMEU E JULIETA ZERO LACTOSE', 'Queijo mozarela zero lactose e pedaços de goiabada', 'Zero Lactose', 40.0),
     ('TOMATE SECO COM RÚCULA ZERO LACTOSE', 'Molho de tomate, queijo mozarela zero lactose, tomate seco e rúcula', 'Zero Lactose', 55.0);

INSERT INTO tb_pedido (id_cliente,observacao,tipo_entrega,preco,data_pedido) VALUES
	 (1,NULL,'Delivery',55.00,'2021-04-17 19:12:23'),
	 (2,NULL,'Delivery',120.00,'2021-04-17 19:17:20'),
	 (3,'Sem molho pesto.','Delivery',55.00,'2021-04-17 20:51:17'),
	 (1,NULL,'Delivery',60.00,'2021-04-18 18:02:03'),
	 (4,NULL,'Delivery',57.50,'2021-04-18 18:12:35'),
	 (5,'Sem cebola.','Retirada no balcão',90.00,'2021-04-18 18:35:12'),
	 (3,NULL,'Delivery',55.00,'2021-04-18 18:47:44'),
	 (2,NULL,'Delivery',55.00,'2021-04-18 19:21:07'),
	 (6,NULL,'Delivery',60.00,'2021-04-18 19:24:10'),
	 (7,NULL,'Delivery',155.00,'2021-04-18 19:32:55'),
	 (1,NULL,'Delivery',320.00,'2021-04-18 19:57:00'),
	 (8,NULL,'Delivery',110.00,'2021-04-18 20:01:45'),
	 (9,NULL,'Delivery',55.00,'2021-04-18 20:12:13'),
	 (2,NULL,'Delivery',55.00,'2021-04-18 20:18:09'),
	 (5,NULL,'Retirada no balcão',60.00,'2021-04-18 20:30:08'),
	 (6,NULL,'Delivery',95.00,'2021-04-18 20:47:56'),
	 (4,NULL,'Delivery',57.50,'2021-04-18 21:07:09'),
	 (9,NULL,'Retirada no balcão',107.50,'2021-04-20 18:17:23'),
	 (10,NULL,'Delivery',260.00,'2021-04-20 18:50:35'),
	 (11,NULL,'Delivery',45.00,'2021-04-20 19:20:46'),
	 (6,NULL,'Delivery',57.50,'2021-04-20 20:47:19'),
	 (12,NULL,'Retirada no balcão',100.00,'2021-04-20 21:15:02'),
	 (1,NULL,'Delivery',100.00,'2021-04-20 22:30:44'),
	 (12,NULL,'Retirada no balcão',50.00,'2021-04-21 19:41:00'),
	 (3,NULL,'Delivery',60.00,'2021-04-21 20:22:59'),
	 (4,NULL,'Delivery',95.00,'2021-04-22 20:05:13'),
	 (11,NULL,'Delivery',57.50,'2021-04-22 21:37:41'),
	 (5,NULL,'Delivery',215.00,'2021-04-23 19:02:33'),
	 (9,NULL,'Delivery',60.00,'2021-04-23 19:55:56'),
	 (1,NULL,'Delivery',47.50,'2021-04-23 20:47:42');

INSERT INTO tb_pedido_pizza (id_pedido,id_pizza,quantidade) VALUES
	 (1,11,'Inteira'),
	 (2,5,'Meia'),
	 (2,6,'Meia'),
	 (2,8,'Meia'),
	 (2,10,'Meia'),
	 (3,1,'Meia'),
	 (3,7,'Meia'),
	 (4,10,'Inteira'),
	 (5,7,'Meia'),
	 (5,8,'Meia'),
	 (6,9,'Inteira'),
	 (6,2,'Meia'),
	 (6,4,'Meia'),
	 (7,16,'Inteira'),
	 (8,12,'Inteira'),
	 (9,5,'Meia'),
	 (9,6,'Meia'),
	 (10,1,'Meia'),
	 (10,2,'Meia'),
	 (10,4,'Meia'),
	 (10,7,'Meia'),
	 (10,9,'Meia'),
	 (10,10,'Meia'),
	 (11,1,'Inteira'),
	 (11,2,'Inteira'),
	 (11,3,'Inteira'),
	 (11,4,'Inteira'),
	 (11,5,'Inteira'),
	 (11,6,'Inteira'),
	 (12,6,'Meia'),
	 (12,2,'Meia'),
	 (13,1,'Inteira'),
	 (14,13,'Meia'),
	 (14,14,'Meia'),
	 (15,5,'Inteira'),
	 (16,3,'Inteira'),
	 (16,4,'Inteira'),
	 (17,15,'Meia'),
	 (17,16,'Meia'),
	 (18,4,'Meia'),
	 (18,7,'Meia'),
	 (18,1,'Inteira'),
	 (19,1,'Inteira'),
	 (19,2,'Inteira'),
	 (19,4,'Inteira'),
	 (19,3,'Inteira'),
	 (19,5,'Inteira'),
	 (20,3,'Inteira'),
	 (21,1,'Meia'),
	 (21,5,'Meia'),
	 (22,1,'Meia'),
	 (22,3,'Meia'),
	 (22,2,'Meia'),
	 (22,4,'Meia'),
	 (23,10,'Inteira'),
	 (23,9,'Inteira'),
	 (24,2,'Inteira'),
	 (24,4,'Inteira'),
	 (25,15,'Inteira'),
	 (26,11,'Meia'),
	 (26,12,'Meia'),
	 (26,9,'Inteira'),
	 (27,7,'Meia'),
	 (27,8,'Meia'),
	 (28,1,'Inteira'),
	 (28,3,'Inteira'),
	 (28,5,'Inteira'),
	 (28,9,'Inteira'),
	 (29,5,'Meia'),
	 (29,6,'Meia'),
	 (30,3,'Meia'),
	 (30,4,'Meia');
	 

select nome from tb_cliente;

select nome from tb_pizza;

select nome from tb_pizza
where categoria = 'Zero Lactose';

select nome from tb_pizza
where categoria <> 'Zero Lactose';


select * from tb_pedido 
where data_pedido >= '2021-04-21 00:00:00' AND data_pedido <= '2021-04-21 23:59:59';

select * from tb_pedido
where preco > 100;

select * from tb_pedido 
where id_cliente = 11 and (data_pedido >= '2021-04-22 00:00:00' AND data_pedido <= '2022-04-22 23:59:59');

--selecionar todos os clientes que moram nas ruas das flores
select * from tb_cliente
where endereco like '%rua das Flores%';

--selecionar os emails de todos os clientes que possuem Maria no nome
select * from tb_cliente
where email like '%maria%';

--selecionar as pizzas que possuem bacon
-- SELECT * FROM tb_pizza WHERE LOWER(nome) LIKE '%bacon%';
select * from tb_pizza
where nome like '%BACON%';

--selecionar as pizzas que possuem a letra 'a' como segundo caractere no seu nome
select * from tb_pizza
where nome like '_A%';

--selecionar o nome dos clientes que fizeram pedidos com valores de 45, 95 e 120
select nome,preco from tb_cliente as c join tb_pedido as p on preco in (45,95,120);


--selecionar o nome dos clientes em ordem alfabetica
select * from tb_cliente order by nome asc;

--seleciona as diferentes formas de entrega realizadas no dia 22/04
select distinct tipo_entrega,id_pedido,id_cliente 
from tb_pedido
where data_pedido between '2021-04-22 00:00:00' and '2021-04-22 23:59:59';

-- selecionar os nomes dos clientes que realizaram mais de 2 pedidos

-- retornar a quantidade de pedidos de cada pizza

-- retornar a quantidade de pedidos de cada categoria de pizza

-- retornar a soma dos preços dos pedidos agrupados pelo nome da pizza

-- retornar a soma dos preços dos pedidos agrupados pelo nome da pizza, filtrando pelas pizzas de categoria "Zero Lactose"
