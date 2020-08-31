create table disco (
	id int unique auto_increment primary key,
	nome varchar(100) not null,
	espaco_total float not null
);

create table leitura(
	id int unique auto_increment primary key,
	id_disco int not null,
	valor_usado float not null,
	valor_livre float not null,
	valor_livre_percentual float not null,
	swap_percentual float not null,
	ram_livre float not null,
	ram_livre_percentual float not null,
	dta_leitura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (id_disco) REFERENCES disco(id)
);

insert into leitura (id_disco,valor_usado,valor_livre,valor_livre_percentual,swap_percentual,ram_livre,ram_livre_percentual)
values (%s,%s,%s,%s,%s,%s,%s);

insert into disco (nome,espaco_total)
values ('G://', 931.00);

insert into disco (nome,espaco_total)
values ('C://',111.00);

insert into disco (nome,espaco_total)
values ('E://',223.00);


select * from leitura
select * from disco;