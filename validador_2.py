#-*- coding: utf-8 -*-
import pdb
import time
import re
import os
import pandas as pd


#--------------VALIDA A ESTRUTURA, TAMANHO DO CAMPO E OS OBRIGATORIOS --------------#
def Verif_estrut(layout,template):
	
	temp_layout, temp_template = dict(),dict()
	cont_lin = int()
	lin_error = list()
	temp_layout, temp_template = layout['obrigatoriedade'],template
	cont_lin = len(temp_template)

	for n in range(1,cont_lin + 1):
		
		if len(temp_template[cont_lin]) > len(temp_layout) :
			lin_error.append(cont_lin,'ef')
			return lin_error
		elif len(temp_template[n]) > len(temp_layout): 
			lin_error.append((n,'mm',len(temp_template[n]),len(temp_layout)))
		elif len(temp_template[n]) < len(temp_layout):
			lin_error.append((n,'mn',len(temp_template[n]),len(temp_layout)))

	if len(lin_error) == 0 :
		return True
	else:
		#print('{}{}{}{}'.format('\n','--------','Erro na estrutura','--------'))
		#[print(x) for x in lin_error ]
		return lin_error

def Verif_tam_camp(layout,template):
	temp_layout, temp_template = dict(),dict()
	temp_layout, temp_template = layout['tamanho'],template
	cont_lin = int()
	lin_error = list()
	cont_col = 1

	for l in range(1,len(temp_template) + 1 ):
		temp = temp_template[l]
		cont_col = 1
		for c in temp:
			if not(len(c) <= int(temp_layout[cont_col])):
				lin_error.append((l,cont_col,c, len(c), temp_layout[cont_col]))				
			cont_col += 1
	if len(lin_error) == 0 :
		return True
	else:
		#print('{}{}{}{}'.format('\n','--------','Erro! Excedeu tamanho do campo','--------'))
		#[print(x) for x in lin_error ]
		return lin_error

def Verif_obr(layout,template):
	temp_layout, temp_template = dict,dict
	temp_layout, temp_template = layout['obrigatoriedade'],template
	temp_layout_cab = layout['nome']
	cont_lin = int()
	lin_error = list()
	cont_col = 1

	for l in range(1,len(temp_template) + 1 ):
		temp = temp_template[l]
		cont_col = 1
		for c in temp:
			if c == '' and temp_layout[cont_col] == 'x':  #melhorar a validacao de campo vazio, com regex
				lin_error.append((l,cont_col,temp_layout_cab[cont_col]))				
			cont_col += 1
	if len(lin_error) == 0 :
		return True
	else:
		#print('{}{}{}{}'.format('\n','--------','Erro! falta dado obrigatorio','--------'))
		#[print(x) for x in lin_error ]
		return lin_error

#-----------------------------------------------------------------------------------#

#------------VERFIFICA A TIPAGEM DOS DADOS SE NUMERO OU DATA -------------#

def Test_dat(layout,template):

	temp_layout, temp_template = dict(),dict()
	padrao = None
	cont_lin = int()
	lin_error = list()
	temp_data = None
	resp_re = None
	temp_lin = None

	temp_layout, temp_template = layout['tipo'],template
	temp_layout_ob = layout['obrigatorio']
	cont_col = 1
	padrao = re.compile("(([0-3]{1}[0-9]{1})\/([0-1]{1}[0-9]{1})\/([1-2]{1}[0-9]{1}[0-9]{1}[0-9]{1}))|(([0-3]{1}[0-9]{1})\/([0-1]{1}[0-9]{1})\/([0-9]{1}[0-9]{1}))")	

	for l in range(1,len(temp_template) + 1):
		temp_lin = temp_template[l]
		cont_col = 1
		for c in temp_lin:
			if temp_layout[cont_col] == 'Data': #and not(c == ''): analisar se o campo e obrigatorio
				temp_data = str(c)
				resp_re = padrao.match(temp_data)
				if not(resp_re) :
					lin_error.append((l,cont_col,temp_data, temp_layout[cont_col],temp_layout_ob[cont_col]))
			cont_col += 1
	if len(lin_error) == 0 :
		return True
	else:
		#print('{}{}{}{}'.format('\n','--------','Erro! Data incorreta ou ausente','--------'))
		#[print(x) for x in lin_error ]
		return lin_error

def Test_num(layout,template):
	temp_layout, temp_template = dict,dict
	temp_layout, temp_template = layout['tipo'],template
	temp_layout_ob = layout['obrigatorio']
	cont_lin = int()
	temp_linha = int()
	lin_error = list()
	cont_col = 1

	for linha in range(1,len(temp_template) + 1 ):
		temp_linha = temp_template[linha]
		cont_col = 1
		for dado in temp_linha:
			if temp_layout[cont_col] == 'Numérico' :
				try:
					conv_dado = float(dado)
				except:
					lin_error.append((l,cont_col,dado,temp_layout[cont_col],temp_layout_ob[cont_col]))
			cont_col += 1
	if len(lin_error) == 0 :
		return True
	else:
		#print('{}{}{}{}'.format('\n','--------','Erro! Tipo de dado incorreto','--------'))
		#[print(x) for x in lin_error ]
		return lin_error


def Format_caminho(dado):
	pass



def Executa():
	
	os.system('cls')
	end = input( 'Informe o caminho do arquivo: ')
	df = pd.read_csv(end,encoding = 'latin1', index_col = 0, sep = ';')
	print(df)
	#temp_layout = Le_arquivo("C:\\Users\\thiago.santos\\Desktop\\HISTDEP.csv",'l')
	#conv_layout = Template(temp_layout)
	#temp_template = Le_arquivo("C:\\Users\\thiago.santos\\Documents\\Clientes\\Finch\\TEMPLATE_FINCH\\CONCLUIDO\\HISTDEP.txt",'t') #Gera dicionario com cada linha do template
	#Verif_estrut(conv_layout,temp_template)
	#Verif_obr(conv_layout,temp_template)
	#Verif_tam_camp(conv_layout,temp_template)
	#Test_num(arq3,arq4)
	#Test_dat(arq3,arq4)

	

if __name__ == '__main__' :
	Executa()