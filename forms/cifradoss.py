# -*- coding: utf-8 -*-
#!/usr/bin/env python
import funciones
from fractions import *
import random
from funciones import *
class Cesar:
	def __init__(self):
		self.k = 3
		self.texto = ""
		self.abc = funciones.abecedario()

	def setK(self,k):
		self.k=k

	def setTexto(self,texto):
		self.texto = texto

	def cifrar(self):
		mensaje = funciones.letranumero(self.texto)
		cifrado = []
		for i in mensaje:
			aux = i
			cifrado.append((aux+self.k)%len(self.abc))
		textocifrado = funciones.numeroLetra(cifrado)
		return textocifrado

	def descifrar(self):
		mensaje = funciones.letranumero(self.texto)
		cifrado = []
		for i in mensaje:
			aux = i
			cifrado.append((aux-self.k)%len(self.abc))
		textocifrado = funciones.numeroLetra(cifrado)
		return textocifrado

class Afin:
	def __init__(self):
		self.a = 14
		self.d= 7
		self.texto = ""
		self.abc=funciones.abecedario()

	def setA(self,a):
		self.a = a

	def setD(self,d):
		self.d = d

	def setTexto(self,texto):
		self.texto = texto

	def cifrar(self):
		tam = len (self.abc)
		mcd = gcd(self.a, tam)
		if mcd == 1:
			texto = funciones.letranumero(self.texto)
			cifrado = []
			for i in texto:
				aux = i
				cifrado.append((self.a*aux+self.d)%tam)
			textocifrado = funciones.numeroLetra(cifrado)
			return textocifrado

	def descifrar(self):
		tam = len (self.abc)
		mcd, u, v = funciones.egcd(tam, self.a);
		if mcd == 1:
			texto = funciones.letranumero(self.texto)
			v = v%tam
			des = []
			for i in texto:
				aux = i
				des.append((v*(aux-self.d)%tam))
			textodes = funciones.numeroLetra(des)
			return textodes



class Mochila:
	def __init__(self):
		self.mochila = [12,64,109,254,455] #privada
		self.m = 986 #privada
		self.w = 503 #publica
		self.public = [120,640,597,568,113] #publica
		self.texto = ""
		self.abc=funciones.abecedario()

	def setMochila(self,mochila):
		self.mochila = mochila

	def setM(self,m):
		self.m = m

	def setW(self,w):
		self.w = w

	def setPublic(self,public):
		self.public = public

	def setTexto(self,texto):
		self.texto = texto

	def setClaves(self,mochila,m,w,public):
		self.setM(m)
		self.setW(w)
		mochila = funciones.cadenaLista(mochila)
		self.setMochila(mochila)
		public = funciones.cadenaLista(public)
		self.setPublic(public)



	def cifrar(self):
		texto = funciones.numeroBinario(self.texto)
		tam = len(self.public)
		if (len(texto) % tam) !=0:
			i = 0
			while i<=(len(texto) % tam):
				texto = texto + '0'
				i = i+1

		i = 0
		j = 0
		suma = 0
		textocifrado = ''
		aux = []
		while i<len(texto):
			if j == tam:
				j = 0
				suma = 0
			if texto[i]=='1':
				suma = suma+self.public[j]
			if j == tam-1:
				suma = suma%self.m
				aux.append(suma)
			i = i+1
			j = j+1

		i = 0
		while i < len(aux):
			aux[i]=str(aux[i])
			textocifrado += aux[i]
			textocifrado += ','
			i = i+1
		textocifrado = textocifrado[0:len(textocifrado)-1]
		textocifrado = funciones.cadenaLista(textocifrado)
		return textocifrado

	def descifrar(self):
		texto = self.texto
		inv = funciones.modinv(self.w,self.m)
		i = 0
		while i < len(texto):
			texto[i] = (texto[i]*inv)%self.m
			i = i+1

		numeros = self.descifraNumero(texto,self.mochila)
		numeros = funciones.binarioNumero(numeros)
		descifrado = funciones.numeroLetra(numeros)

		return descifrado

	def generarClave(self):
	    tam = 5
	    aleatorio = random.randrange(1,100)
	    mochila = [aleatorio]
	    suma = aleatorio
	    for i in range(tam-1):
	        suma = suma+mochila[i]
	        numero = suma + random.randrange(1,100)
	        mochila.append(numero)

	    m = mochila[tam-1]*2 + random.randrange(1,200)
	    w = funciones.generarPrimos(1)
	    b = []
	    for i in range(tam):
	        numero = (w*mochila[i])%m
	        b.append(numero)

		self.setM(m)
		self.setW(w)
		self.setPublic(b)
	    self.setMochila(mochila)

	def descifraNumero (self,texto, mochila):
	    #funcion para conseguir la cadena de binarios al descifrar
	    """

	    """
	    i = 0
	    numero=''
	    while i < len(texto):
	        j=len(mochila)-1
	        aux=''
	        res = texto[i]
	        while j >=0:
	            if mochila[j] <= res:
	                res = res-mochila[j]
	                aux = '1'+aux
	            else:
	                aux = '0'+aux
	            j=j-1
	        numero = numero+aux
	        i=i+1
	    return numero


class RSA:
	def __init__(self):
		self.n = 1711 #privada y publica
		self.e = 961 #publica
		self.d = 921 #privada
		self.texto = ""

	def setN(self,n):
		self.n = n

	def setE(self,e):
		self.e = e

	def setD(self,d):
		self.d = d

	def setTexto(self,texto):
		self.texto = texto

	def cifrar(self,e,n,texto):
		blo = funciones.prepa_num_cifrar(n,texto)
		cifrado = []
		for i in blo:
			cifrado.append(funciones.potencia(i,e,n))

		return cifrado

	def descifrar(self,d,n,cifrado):
		descifro = []
		for i in cifrado:
			descifro.append(funciones.potencia(i,d,n))
		descifrado = funciones.num_letra(n,descifro)
		return descifrado

	def generarFirma(self, texto):
		n = self.n
		M = funciones.hash(self.texto, n)
		S = funciones.potencia(M,self.d,n)
		return S

	def generarClave(self):
		p = funciones.generarPrimos(2)
		q = funciones.generarPrimos(2)
		while p == q:
			q = funciones.generarPrimos(2)

		n = p*q
		phi = (p-1)*(q-1)
		e = random.randrange(50,phi-1)
		[gcd,u,v] = funciones.egcd(phi,e)

		while True:
			e = random.randrange(1,phi-1)
			[gcd,u,v] = funciones.egcd(phi,e)
			if gcd == 1:
				break

		d = funciones.modinv(e,phi)
		self.setN(n)
		self.setD(d)
		self.setE(e)




if __name__ == "__main__":
	"""asd = RSA()
	#asd.generarClave()
	asd.setN(3869)
	asd.setE(1489)
	asd.setD(1393)
	asd.setTexto('hola')
	r = asd.cifrar(asd.e, asd.n, asd.texto)
	print r
	d = asd.descifrar(asd.d, asd.n, r)
	print d"""
	asd = Mochila()
	asd.setTexto('hola')
	r = asd.cifrar()
	print r
	asd.setTexto(cadenaLista('292, 819, 335, 0'))
	d = asd.descifrar()
	print d
