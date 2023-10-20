from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templatesProductos/index.html')

def electronica(request):
    data={
        "titulo":"Electrónica",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"PlayStation",
    }
    return render(request,'templatesProductos/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"Pelota",
        'producto2':"Figura de Acción",
        'producto3':"Juego de Mesa",
    }
    return render(request,'templatesProductos/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Polera",
        'producto2':"Chaqueta",
        'producto3':"Zapatilla",
    }
    return render(request,'templatesProductos/productos.html',data)