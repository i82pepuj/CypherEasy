from django import forms
from models import ClaveMochila, ClaveRSA

class CifradoCesar(forms.Form):
    k = forms.IntegerField(label="Valor k", required = True)
    texto = forms.CharField(label="Texto a cifrar", required = True)

class DescifradoCesar(forms.Form):
    k = forms.IntegerField(label="Valor k", required = True)
    texto = forms.CharField(label="Texto a descifrar", required = True)

class CifradoAfin(forms.Form):
    a = forms.IntegerField(label="Valor a", required = True)
    d = forms.IntegerField(label="Valor d", required = True)
    texto = forms.CharField(label="Texto a cifrar", required = True)

class DescifradoAfin(forms.Form):
    a = forms.IntegerField(label="Valor a", required = True)
    d = forms.IntegerField(label="Valor d", required = True)
    texto = forms.CharField(label="Texto a descifrar", required = True)

class CifradoMochila(forms.Form):
    def __init__ (self, user, *args, **kwargs):
        forms.Form.__init__ (self, *args, **kwargs)
        self.fields['clave'] = forms.ChoiceField(label="Clave", choices=[(str(o), str(o)) for o in ClaveMochila.objects.filter(user=user)])
        self.fields['texto'] = forms.CharField(label="Texto a cifrar", required=True)

class DescifradoMochila(forms.Form):
    def __init__ (self, user, *args, **kwargs):
        forms.Form.__init__ (self, *args, **kwargs)
        self.fields['clave'] = forms.ChoiceField(label="Clave", choices=[(str(o), str(o)) for o in ClaveMochila.objects.filter(user=user)])
        self.fields['texto'] = forms.CharField(label="Texto a descifrar", required=True)

class GenerarMochila(forms.Form):
    nombre = forms.CharField(label="Nombre de la clave", required = True)

class IntroducirClaveMochila(forms.Form):
    nombre = forms.CharField(label="Nombre identificativo de la clave", required = True)
    mochila = forms.CharField(label="Clave mochila", required = True)
    publica = forms.CharField(label="Clave publica", required = True)
    m = forms.IntegerField(label="Valor m")
    w = forms.IntegerField(label="Valor w")

class CifradoRSA(forms.Form):
    def __init__ (self, user, *args, **kwargs):
        forms.Form.__init__ (self, *args, **kwargs)
        self.fields['clave'] = forms.ChoiceField(label="Clave", choices=[(str(o), str(o)) for o in ClaveRSA.objects.filter(user=user)])
        self.fields['texto'] = forms.CharField(label="Texto a cifrar", required=True)

class DescifradoRSA(forms.Form):
    def __init__ (self, user, *args, **kwargs):
        forms.Form.__init__ (self, *args, **kwargs)
        self.fields['clave'] = forms.ChoiceField(label="Clave", choices=[(str(o), str(o)) for o in ClaveRSA.objects.filter(user=user)])
        self.fields['texto'] = forms.CharField(label="Texto a descifrar", required=True)

class GenerarRSA(forms.Form):
    nombre = forms.CharField(label="Nombre de la clave", required = True)

class IntroducirClaveRSA(forms.Form):
    nombre = forms.CharField(label="Nombre identificativo de la clave", required = True)
    n = forms.IntegerField(label="Valor n")
    e = forms.IntegerField(label="Valor e")
    d = forms.IntegerField(label="Valor d")

class Correo(forms.Form):
    def __init__ (self, user, *args, **kwargs):
        forms.Form.__init__ (self, *args, **kwargs)
        self.fields['clave'] = forms.ChoiceField(label="Clave", choices=[(str(o), str(o)) for o in ClaveRSA.objects.filter(user=user)])
        self.fields['nombre'] = forms.CharField(required = True)
        self.fields['remitente'] = forms.EmailField(required = True)
        self.fields['direccion'] = forms.EmailField(required = True)
        self.fields['asunto'] = forms.CharField(required = True)
        self.fields['mensaje'] = forms.CharField(required = True)
