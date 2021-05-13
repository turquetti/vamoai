--questao 1
SELECT * from users
where age >= 18;

--questao 2
delete from travelers
where country = 'Canada' or country = 'Mexico' or country = 'USA';

select * from travelers
-- outra solução
select * from travelers
where country not in ('Canada', 'Mexico', 'USA');


--questao 3
INSERT INTO participants (name, 
                          age, 
                          attending) 
       VALUES('Gabriela', 
              26, 
              'TRUE');

SELECT * FROM participants;

--questao 4
SELECT 
       MAX(idade) as maior_idade,
       MIN(idade) as menor_idade
FROM alunos;

-- questao 5
SELECT * 
FROM suspeitos
WHERE nome LIKE 'João%';