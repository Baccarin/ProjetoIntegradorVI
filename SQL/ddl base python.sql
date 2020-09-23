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

insert into disco (nome,espaco_total)
values ('G://', 931.00);

insert into disco (nome,espaco_total)
values ('C://',111.00);

insert into disco (nome,espaco_total)
values ('E://',223.00);

select * from leitura
select * from disco;
-- -----------------------------------------------------

-- Quando que a utilização da CPU foi menor que 20% e maior que 80%?
select * from leitura where valor_livre_percentual > 20 and  valor_livre_percentual < 80;

-- Qual foi o máximo e o mínimo de memória utilizado nos últimos três dias?
-- maximo
select * from leitura where dta_leitura between STR_TO_DATE( "20/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" ) 
order by valor_livre_percentual desc limit 1;
-- minimo          
select * from leitura where dta_leitura between STR_TO_DATE( "20/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" ) 
order by valor_livre_percentual limit 1;

-- Quando a CPU obteve a frequência mínima e máxima?
-- maximo
select * from leitura
order by valor_livre_percentual desc limit 1;
-- minimo          
select * from leitura
order by valor_livre_percentual limit 1;

-- Considerando o monitoramento por 5 dias, qual a frequência média da CPU?
select id_disco,round(avg(valor_usado),2) media from leitura  where dta_leitura between STR_TO_DATE( "18/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" )
group by id_disco;

-- Ajustando Foreing key duplicada
ALTER TABLE leitura
DROP FOREIGN KEY leitura_ibfk_1;

ALTER TABLE leitura
ADD CONSTRAINT fk_discoid
FOREIGN KEY (id_disco) REFERENCES Disco(id);
