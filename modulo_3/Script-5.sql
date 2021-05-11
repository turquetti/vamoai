alter table album alter column id type varchar(25);

insert into album (id, titulo) values ('59CVVonQciTIUJH5zr7hia','The Perfect Element, Pt. I (Anniversary Mix 2020)')

insert into album (id, titulo) values ('2n4ir58xq66WvWHFjzsYXU','The Perfect Element, Pt. 1 (Anniversary Mix 2020)')

delete from album 
where id = '59CVVonQciTIUJH5zr7hia'

delete from album
where id = '2n4ir58xq66WvWHFjzsYXU'

COPY album (id, titulo)
FROM '/home/albums.csv'
DELIMITER ','
CSV header


-- select * from album where titulo = 'PANTHER'
select * from album

update album set titulo = 'OASIS' where titulo = 'PANTHER'

update album set titulo = 'Sextou' where titulo = 'Sexta'