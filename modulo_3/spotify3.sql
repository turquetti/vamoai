copy 
(
select id, titulo from albums.csv
)
to '/Users/gabrielaturquetti/Documents/vamoai/modulo_3/albums.csv'
delimiter ';'
csv header