from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templatesProductos/index.html')
 
def datos(request):
     datos = {
        "nombre":"Cosme",
        "apellido":"Fulanito",
        "edad": 36,
        "hobbies":["Cerveza","Rosquillas","Dormir"],
        "direccion":"Calle Falsa 123",
        "ciudad":"Springfield",
        "imagen":"imagenes/cfulanito.png",
        "url0":"/index2",
        "url1": "/datos",
        "url2": "/datos2",
        "url3": "/datos3",
     }
     return render(request,'templatesApp2/datos.html', datos)

def datos2(request):
     datos2 = {
        "nombre":"Homero",
        "apellido":"Simpson",
        "edad": 36,
        "hobbies":["Cerveza","Rosquillas","Dormir"],
        "direccion":"Av Evergreen Terrace 742",
        "ciudad":"Springfield",
        "imagen":"imagenes/homer.png",
        "url0":"/index2",
        "url1": "/datos",
        "url2": "/datos2",
        "url3": "/datos3",
     }
     return render(request,'templatesApp2/datos2.html', datos2)

def datos3(request):
     datos3 = {
        "nombre":"Maggie",
        "apellido":"Simpson",
        "edad": "???",
        "hobbies":["Su Chupón"],
        "direccion":"Av Evergreen Terrace 742",
        "ciudad":"Springfield",
        "imagen":"imagenes/maggie.png",
        "url0":"/index2",
        "url1": "/datos",
        "url2": "/datos2",
        "url3": "/datos3",
     }
     return render(request,'templatesApp2/datos3.html', datos3)