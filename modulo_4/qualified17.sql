-- questao 1
select clientes.id as cliente_id, clientes.nome as nome_cliente
from clientes
left join pedidos on clientes.id = pedidos.cliente_id
where pedidos.id is null;

-- questao 2
select cl.id as cliente_id, cl.nome as nome_cliente, 
  case when min(ped.quantidade) is null then 0
  else sum(ped.quantidade)
  end quantidade_itens_pedidos
from clientes cl
left join pedidos ped on cl.id = ped.cliente_id
group by cl.id
order by quantidade_itens_pedidos
limit 10;

-- questao 3
select f.id, f.nome, f.salario
from funcionarios as f
where f.salario > (select f.salario 
                   from funcionarios as f
                   where f.id = 30)

-- questao 4
select f.id, f.nome, f.area_atuacao, f.salario
from funcionarios as f 
where f.salario in (select min(f.salario)
                   from funcionarios as f
                   group by f.area_atuacao)

-- questao 5
select f.id, f.nome, f.area_atuacao, f.salario
from funcionarios as f 
where f.salario > (select avg(f.salario)
                   from funcionarios as f
                   group by f.area_atuacao
                   limit 1)