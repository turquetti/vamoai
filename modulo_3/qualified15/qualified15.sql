-- questao 1
select idade, count(idade) as total_de_pessoas
from pessoas
group by idade
having count(idade) >= 10

--questao 2

--questao 3
select pes.id, pes.nome, count(b.id) as quantidade_brinquedos
from pessoas pes
join brinquedos b on pes.id = b.pessoas_id
group by pes.id

--questao 4
select case
    when pessoas.idade >= 18 then 'Maior de Idade'
    else 'Menor de Idade' end grupo_idade,
    count(pessoas.id) as quantidade_pessoas
from pessoas 
group by grupo_idade
order by quantidade_pessoas desc

--questao 5
select pes.id, pes.nome, sum(ped.quantidade) as total_itens
from pessoas pes
join pedidos ped on pes.id = ped.pessoas_id
group by pes.id
order by total_itens desc
limit 10
