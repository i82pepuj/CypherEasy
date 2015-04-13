from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from cifrados import *
from funciones import *
from form import *
from models import *
from django.core.mail import send_mail

def cifrar_Cesar(request):
    if request.method == 'POST':
        form = CifradoCesar(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Cesar()
            clase.setK(form['k'])
            clase.setTexto(form['texto'])
            textoCifrado = clase.cifrar()

            return render_to_response('resultadoCesar.html', locals())

    else:
        form = CifradoCesar()

    return render(request, 'cifrarCesar.html', {'form': form})

def descifrar_Cesar(request):
    if request.method == 'POST':
        form = DescifradoCesar(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Cesar()
            clase.setK(form['k'])
            clase.setTexto(form['texto'])
            textoDescifrado = clase.descifrar()

            return render_to_response('resultadoCesar2.html', locals())

    else:
        form = DescifradoCesar()

    return render(request, 'descifrarCesar.html', {'form': form})


def cifrar_Afin(request):
    if request.method == 'POST':
        form = CifradoAfin(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Afin()
            clase.setA(form['a'])
            clase.setD(form['d'])
            clase.setTexto(form['texto'])
            textoCifrado = clase.cifrar()


            return render_to_response('resultadoAfin.html', locals())

    else:
        form = CifradoAfin()

    return render(request, 'cifrarAfin.html', {'form': form})


def descifrar_Afin(request):
    if request.method == 'POST':
        form = DescifradoAfin(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Afin()
            clase.setA(form['a'])
            clase.setD(form['d'])
            clase.setTexto(form['texto'])
            textoDescifrado = clase.descifrar()

            return render_to_response('resultadoAfin2.html', locals())

    else:
        form = DescifradoAfin()

    return render(request, 'descifrarAfin.html', {'form': form})


def cifrar_Mochila(request):
    user = request.user
    if request.method == 'POST':
        form = CifradoMochila(user, request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Mochila()
            clave = ClaveMochila.objects.filter(nombre=form['clave'])[0]
            clase.setMochila(cadenaLista(clave.mochila))
            clase.setPublic(cadenaLista(clave.publica))
            clase.setM(clave.m)
            clase.setW(clave.w)
            clase.setTexto(form['texto'])

            textoCifrado = clase.cifrar()

            return render_to_response('resultadoMochila.html', locals())

    else:
        form = CifradoMochila(user)

    return render(request, 'cifrarMochila.html', {'form': form})


def descifrar_Mochila(request):
    user = request.user
    if request.method == 'POST':
        form = DescifradoMochila(user, request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = Mochila()
            clave = ClaveMochila.objects.filter(nombre=form['clave'])[0]
            clase.setMochila(cadenaLista(clave.mochila))
            clase.setPublic(cadenaLista(clave.publica))
            clase.setM(clave.m)
            clase.setW(clave.w)
            clase.setTexto(cadenaLista(form['texto']))

            textoDescifrado = clase.descifrar()

            return render_to_response('resultadoMochila2.html', locals())

    else:
        form = DescifradoMochila(user)

    return render(request, 'descifrarMochila.html', {'form': form})


def generar_Clave_Mochila(request):
    user = request.user
    if request.method == 'POST':
        form = GenerarMochila(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            clase = Mochila()
            clase.generarClave()

            clave = ClaveMochila()
            clave.nombre = form['nombre']
            clave.user = user
            clave.mochila = listacadena(clase.mochila)
            clave.publica = listacadena(clase.public)
            clave.m = clase.m
            clave.w = clase.w
            clave.save()

            return HttpResponseRedirect('/cifrarmochila/')

    return HttpResponseRedirect('/')

def introducir_Clave_Mochila(request):
    user = request.user
    if request.method == 'POST':
        form = IntroducirClaveMochila(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            clave = ClaveMochila()
            clave.nombre = form['nombre']
            clave.user = user
            clave.mochila = form['mochila']
            clave.publica = form['publica']
            clave.m = form['m']
            clave.w = form['w']
            clave.save()


            return HttpResponseRedirect('/cifrarmochila/')

    return HttpResponseRedirect('/')


def cifrar_RSA(request):
    user = request.user
    if request.method == 'POST':
        form = CifradoRSA(user, request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = RSA()
            clave = ClaveRSA.objects.filter(nombre=form['clave'])[0]
            clase.setN(clave.n)
            clase.setE(clave.e)
            clase.setD(clave.d)
            clase.setTexto(form['texto'])

            textoCifrado = clase.cifrar(clase.e, clase.n, clase.texto)

            return render_to_response('resultadoRSA.html', locals())

    else:
        form = CifradoRSA(user)

    return render(request, 'cifrarRSA.html', {'form': form})


def descifrar_RSA(request):
    user = request.user

    if request.method == 'POST':
        form = DescifradoRSA(user, request.POST)
        if form.is_valid():

            form = form.cleaned_data

            clase = RSA()
            clave = ClaveRSA.objects.filter(nombre=form['clave'])[0]
            clase.setN(clave.n)
            clase.setE(clave.e)
            clase.setD(clave.d)
            clase.setTexto(cadenaLista(form['texto']))


            textoDescifrado = clase.descifrar(clase.d, clase.n, clase.texto)

            print textoDescifrado

            return render_to_response('resultadoRSA2.html', locals())

    else:
        form = DescifradoRSA(user)

    return render(request, 'descifrarRSA.html', {'form': form})


def generar_Clave_RSA(request):
    user = request.user
    if request.method == 'POST':
        form = GenerarRSA(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            clase = RSA()
            clase.generarClave()

            #adaptar clave a cadena y guardar en base de datos
            clave = ClaveRSA()
            clave.nombre = form['nombre']
            clave.user = user
            clave.n = clase.n
            clave.e = clase.e
            clave.d = clase.d
            clave.save()

            return HttpResponseRedirect('/cifrarrsa/')

    return HttpResponseRedirect('/')


def introducir_Clave_RSA(request):
    user = request.user
    if request.method == 'POST':
        form = IntroducirClaveRSA(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            clave = ClaveRSA()
            clave.nombre = form['nombre']
            clave.user = user
            clave.n = form['n']
            clave.e = form['e']
            clave.d = form['d']
            clave.save()


            return HttpResponseRedirect('/cifrarrsa/')

    return HttpResponseRedirect('/')


def correoFirma(request):
    user = request.user.id
    if request.method == 'POST':
        form = Correo(user, request.POST)
        if form.is_valid():
            form = form.cleaned_data

            clase = RSA()
            clave = ClaveRSA.objects.filter(nombre=form['clave'])[0]
            clase.setN(clave.n)
            clase.setE(clave.e)
            clase.setD(clave.d)
            clase.setTexto(form['mensaje'])

            firma = clase.generarFirma('mensaje')
            firma = str(firma)

            print form['mensaje'] + firma

            send_mail(form['asunto'], form['mensaje'] + firma, form['remitente'], [form['direccion']], fail_silently=False)

            return HttpResponseRedirect('/enviarcorreo/')

    else:
        form = Correo(user)

    return render(request, 'enviarCorreo.html', {'form': form})
