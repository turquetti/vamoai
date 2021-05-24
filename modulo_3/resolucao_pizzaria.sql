-- selecionar todos os clientes da pizzaria
select nome from tb_cliente;

-- selecionar todas as pizzas da pizzaria
select nome from tb_pizza;

-- selecionar as pizzas da categoria Zero Lactose
select nome from tb_pizza
where categoria = 'Zero Lactose';

-- selecionar todas as pizzas que não são da catergoria Zero Lactose
select nome from tb_pizza
where categoria <> 'Zero Lactose';

-- selecionar todos os pedidos feitos no dia 21/04
select * from tb_pedido 
where data_pedido >= '2021-04-21 00:00:00' AND data_pedido <= '2021-04-21 23:59:59';

-- selecionar todos os ids dos clientes que realizaram pedidos acima de 100 reais
select * from tb_pedido
where preco > 100;

-- selecionar todos os sabores de pizzas pedidas por Enzo Gabriel no dia 22/04/2021
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

-- selecionar o nome do cliente que fez o pedido mais caro
select c.nome, max(p.preco) as preco_pedido
from tb_cliente c 
join tb_pedido p on c.id_cliente = p.id_cliente
group by c.nome

select tb_cliente.nome, tb_pedido.preco
from tb_cliente, tb_pedido
order by tb_pedido.preco desc 
limit 1

-- selecionar o nome dos clientes de todos os pedidos realizados ordenados pelo preço do pedido

-- selecionar a pizza mais cara da categoria "Tradicionais"  que possui "a" como segundo caractere

-- selecionar a soma de todos os pedidos realizados
select sum(preco) as soma_pedidos from tb_pedido;

-- retornar o valor do pedido mais caro
select max(preco) as pedido_max from tb_pedido;

-- retornar o preço médio das pizzas
select avg(preco) as preco_medio_pizzas from tb_pizza;

-- selecione o preço médio por categoria de pizza
select categoria, cast(avg(preco) as numeric(15,2)) as preco_medio_pizzas 
from tb_pizza
group by 1
order by 2;

-- selecione o preço total agrupando-os por tipo de entrega
select tipo_entrega, sum(preco)
from tb_pedido
group by 1
order by 2;

-- selecionar o número de pedidos que cada cliente realizou na pizzaria
-- em ordem crescente

--select *
--from tb_pedido
--where id_cliente = (select count(id_cliente) from tb_cliente);

select c.nome, count(p.id_cliente) as qtd_pedidos
from tb_cliente c 
join tb_pedido p on c.id_cliente = p.id_cliente
group by c.nome
order by 2;

-- selecionar o nome dos clientes que realizam mais de dois pedidos
select c.nome, count(p.id_cliente) as qtd_pedidos
from tb_cliente c 
join tb_pedido p on c.id_cliente = p.id_cliente
group by c.nome having count(p.id_cliente) > 2;

-- selecionar a quantidade de pedidos de cada pizza
select pz.nome, count(pp.id_pizza) as qtd_pizza
from tb_pizza pz
join tb_pedido_pizza pp on pz.id_pizza = pp.id_pizza 
group by pz.nome;

-- retornar a quantidade de pedido de cada categoria de pizza
select pz.categoria, count(pp.id_pizza) as qtd_categoria_pizza
from tb_pizza pz
join tb_pedido_pizza pp on pz.id_pizza = pp.id_pizza 
group by pz.categoria;

-- retornar a soma dos preços dos pedidos agrupados pelo nome da pizza
select pz.nome, sum(p.preco) 
from tb_pizza pz
join tb_pedido_pizza pp on pz.id_pizza = pp.id_pizza
join tb_pedido p on pp.id_pedido = p.id_pedido 
group by pz.nome;

-- retornar a soma dos preços dos pedidos agrupados pelo nome da pizza fil
-- trando pela categoria de "Zero Lactose"
select pz.nome, sum(p.preco) 
from tb_pizza pz
join tb_pedido_pizza pp on pz.id_pizza = pp.id_pizza
join tb_pedido p on pp.id_pedido = p.id_pedido
where pz.categoria = 'Zero Lactose'
group by pz.nome;

-- selecionar o nome dos clientes e o preço dos pedidos com o tipo de entrega Delivery
select * from tb_cliente
join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente 

-- selecionar o nome dos clientes e o nome das pizzas pedidas por eles.

-- selecionar o nome dos clientes e o nome das pizzas pedidas por eles filtrando pelas pizzas que são Zero Lactose

-- Selecionar o total de preço dos pedidos, agrupando pelos nomes dos clientes e ordenando pelos que mais gastaram.
select c.nome, sum(preco) as valor_total_pedidos
from tb_cliente c
join tb_pedido as p on c.id_cliente = p.id_cliente
group by c.nome 
order by valor_total_pedidos desc;
