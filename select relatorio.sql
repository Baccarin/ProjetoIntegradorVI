-- Quando que a utiliza��o da CPU foi menor que 20% e maior que 80%?
select * from leitura where valor_livre_percentual > 20 and  valor_livre_percentual < 80;

-- Qual foi o m�ximo e o m�nimo de mem�ria utilizado nos �ltimos tr�s dias?
-- maximo
select * from leitura where dta_leitura between STR_TO_DATE( "20/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" ) 
order by valor_livre_percentual desc limit 1;
-- minimo          
select * from leitura where dta_leitura between STR_TO_DATE( "20/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" ) 
order by valor_livre_percentual limit 1;

-- Quando a CPU obteve a frequ�ncia m�nima e m�xima?
-- maximo
select * from leitura
order by valor_livre_percentual desc limit 1;
-- minimo          
select * from leitura
order by valor_livre_percentual limit 1;

-- Considerando o monitoramento por 5 dias, qual a frequ�ncia m�dia da CPU?
select id_disco,round(avg(valor_usado),2) from leitura  where dta_leitura between STR_TO_DATE( "18/09/2020", "%d/%m/%Y" ) AND
           STR_TO_DATE( "23/09/2020", "%d/%m/%Y" )
group by id_disco;

