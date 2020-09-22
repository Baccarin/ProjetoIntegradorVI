
create table leitura(
	id int auto_increment primary key,
	id_disco int,
	valor_usado int,
	valor_livre int,
	valor_livre_percentual int,
	swap_percentual int,
	ram_livre int,
	ram_livre_percentual int,
	foreign key (id_disco) references disco (id),
);

create table disco (
	id int unique auto_increment primary key,
	nome varchar(100) not null,
	espaco_total float not null
);