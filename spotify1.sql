create table usuario(
	id SERIAL primary key,
	email varchar(100) not null unique,
	username varchar(100) not null unique,
	senha varchar(30) not null
);

create table playlist(
	id SERIAL primary key,
	nome varchar(100) not null
);

create table historico(
	id SERIAL primary key,
	data_hora date not null
);

create table musica(
	id SERIAL primary key,
	nome varchar(100) not null
);

create table album(
	id SERIAL primary key,
	titulo varchar(100) not null
);

create table artista(
	id SERIAL primary key,
	nome varchar(100) not null
);

create table genero(
	id serial primary key,
	nome varchar(100) not null unique
);


