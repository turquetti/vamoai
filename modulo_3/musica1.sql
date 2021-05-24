select * from "Album" 
select * from "Artist"
select * from "Customer"
select * from "Employee"
select * from "Genre"
select * from "Invoice"
select * from "InvoiceLine"
select * from "MediaType"
select * from "Playlist"
select * from "PlaylistTrack"
select * from "Track"

-- selecione os 10 primeiros artistas da tabela 
select * from "Artist"
limit 10

-- apresente o nome dos artistas de forma paginada com 10 resultados por página
select * from "Artist"
limit 10
offset (0-0) * 10

-- mostre a quantidade de albuns que cada artista lançou e ordene-se de modo que seja possível visualizar quem lançou mais album
select artist."Name", count(album."ArtistId") as qtd_albuns
from "Album" album 
join "Artist" artist on album."ArtistId" = artist."ArtistId" 
group by artist."Name" 
order by qtd_albuns desc

-- apresente os países que possuem mais de 2 usuários (costumer)
select "Country", count("CustomerId") as contagem
from "Customer"
where contagem > 2


-- exiba a média de tempo das músicas em milisegundos

-- mostre quais são os únicos preços que uma música pode custar

-- selecione o valor maximo da conta de um usuário

-- selecione o total de musicas do genero rock

-- selecione os funcionários que são IT Manager e IT Staff

-- Selecione os funcionários que nasceram entre 1960 e 1970

-- Liste o nome dos usuários e a origem deles de modo que se a origem dele for "Brazil", o valor mostrado deve ser Brasil, caso contrário mostre Estrangeiro.

-- selecione o nome dos artistas associados com o titulo dos seus albuns
select artista."Name", album."Title"
from "Artist" artista
join "Album" album on artista."ArtistId" = album."ArtistId" 

-- selecione o nome dos artistas associados com o nome das musicas (track.name) de forma paginada com 10 resultados por página

-- selecione o nome das playlists e o total de musicas (track.name) agrupadas pelas playlists que pertencem e ordernadas pelas playlists que possuem mais músicas
select 
from "Playlist" playlist 
join 

-- exiba o nome do gênero e a média de tempo das músicas em milisegundos agrupadas por gênero
