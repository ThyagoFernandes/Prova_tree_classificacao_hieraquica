from csv import reader
from contextlib import redirect_stdout
from collections import namedtuple
from treelib import Tree, Node #pip3 install treelib

Entrada = namedtuple("Entrada", "cod_geral area_geral cod_especifica area_especifica cod_detalhada area_detalhada codigo rotulo")
with open("dataset.csv", encoding="utf-8") as csvfile:
  with open("tree.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        arv = Tree()
        cod_geral_area_geral = ""
        cod_especifica_area_especifica = ""
        cod_detalhada_area_detalha = ""
        cod_rotulo = ""
        csvfile.readline()
        for line in reader(csvfile, delimiter=";"):
            entrada = Entrada(*line)

            if cod_geral_area_geral != "{} {}".format(entrada.cod_geral,entrada.area_geral):
                if(arv.all_nodes() != []):
                     arv.show()            
                arv = Tree()
                cod_geral_area_geral = "{} {}".format(entrada.cod_geral,entrada.area_geral)
                arv.create_node(cod_geral_area_geral,"ch+"+cod_geral_area_geral)
                
            if cod_especifica_area_especifica  != "{} {}".format(entrada.cod_especifica ,entrada.area_especifica):
                arv.create_node("{} {}".format(entrada.cod_especifica ,entrada.area_especifica),"{} {}".format(entrada.cod_especifica ,entrada.area_especifica),parent="ch+"+cod_geral_area_geral)
                cod_especifica_area_especifica = "{} {}".format(entrada.cod_especifica ,entrada.area_especifica)
            if  cod_detalhada_area_detalha != "{} {}".format(entrada.cod_detalhada ,entrada.area_detalhada):
                arv.create_node("{} {}".format(entrada.cod_detalhada ,entrada.area_detalhada),"{} {}".format(entrada.cod_detalhada ,entrada.area_detalhada),parent=cod_especifica_area_especifica)
                cod_detalhada_area_detalha = "{} {}".format(entrada.cod_detalhada ,entrada.area_detalhada)
            arv.create_node("{} {}".format(entrada.codigo ,entrada.rotulo),"{} {}".format(entrada.codigo ,entrada.rotulo),parent=cod_detalhada_area_detalha)
