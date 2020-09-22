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
select id_disco,round(avg(valor_usado),2) from leitura  where dta_leitura between STR_TO_DATE( "18/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" )
group by id_disco;

