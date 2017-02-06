#!-/usr/bin/python3

fich = open('/etc/passwd','r')
lineas = fich.readlines()

diccionario = {}

for linea in lineas:
	login = linea.split(":")[0]
	shell = linea.split(":")[-1][:-1]
	diccionario[login] = [shell]
	
try:
	
	print ('root:', diccionario['root'])
	print ('diccionario:', diccionario['imaginario'])
	
except:
	
	print ("usuario no encontrado")
	
fich.close()
