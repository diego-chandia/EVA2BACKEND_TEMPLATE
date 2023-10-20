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
     }
     return render(request,'templatesApp2/datos.html', datos)