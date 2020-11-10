import Leitura as leitura

def maiorUsoRam(self):
    return "select * from leitura order by ram_livre_percentual limit 1"

def menorUsoRam(self):
    return "select * from leitura order by ram_livre_percentual desc limit 1"

def bt_Leitura_Tela(self):
    leitura.bt_iniciarLeitura()