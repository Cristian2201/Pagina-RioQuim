from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Login 
def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html",{"aviso":f"Bienvenido {user}"})
        else:
            return render (request, "AppCoder/inicio.html", {"aviso":"DATOS INCORRECTOS."})
    else:
        form = AuthenticationForm() 
    return render (request, "AppCoder/loginUser.html", {"formulario": form})


def registroUsuario(request):
    
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render (request, "AppCoder/inicio.html", {"aviso": "Felicitaciones lo has creado con exito."})
            
    else:
        
        form = UsuarioRegistro()
    
    return render (request, "AppCoder/registrarse.html", {"formulario":form})

# Vistas/Pestañas 

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def tienda(request):

    return render(request,'AppCoder/tienda.html') # Returna el mensaje Esta es la vista.....

def busqueda(request):

    return render(request,'AppCoder/busqueda.html')

def productos(request):

    return render(request,'AppCoder/leerProducto.html') # Retorna el mensaje Esta es la vista.....

def nosotros(request):

    return render(request,'AppCoder/nosotros.html') # Retorna el mensaje Esta es la vista.....



#Funcion para dar de alta el usuario
def crearUsuario(request):

    if request.method == "POST":
        
        nuevo = CrearUsuario(request.POST)

        if nuevo.is_valid():
            
            info = nuevo.cleaned_data

            usuarios = Registro(nombre=info["nombre"],apellido=info["apellido"],correo=info["correo"])

            usuarios.save()

            return render(request, "AppCoder/inicio.html")
    else:
    
        nuevo = CrearUsuario()
    
    return render(request, "AppCoder/crearUsuario.html", {"form1":nuevo})


#Funcion para buscar un producto

def buscarProducto(request): 

    return render(request, "AppCoder/busqueda.html")

def resultadoBusqueda(request):

    if request.GET ["elemento"]:
        elemento = request.GET["elemento"] 
        productos=Productos.objects.filter(elemento__icontains = elemento)    
        return render(request, "AppCoder/resultados.html",{"productos":productos,"busqueda":elemento,})
          
    else:
        respuesta = "No enviaste datos, vuelve al boton busqueda!!!"
    
    return HttpResponse (respuesta)
    



#CRUD de productos

def leerProducto(request): #Leer los producto en la base

    productos = Productos.objects.all()

    contexto = {"inventario":productos}
    
    return render(request,"AppCoder/leerProducto.html", contexto)


def crearProducto(request): #Crear los producto en la base

    if request.method == "POST":

        formulario1 =  CrearProducto(request.POST) #Importa de forms.py la class CrearProducto
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            elementos = Productos(elemento=info["elemento"], precio=info["precio"])        
        
            elementos.save()

            return render(request, "AppCoder/inicio.html")

    else:
        formulario1 = CrearProducto()

    return render(request, "AppCoder/crearProducto.html", {"form1":formulario1}) 


def eliminarProducto (request,id): #Elimina los productos de la base

    producto = Productos.objects.get(elemento=id)
    producto.delete()

    productos = Productos.objects.all()

    contexto = {"inventario":productos}

    return render (request, "AppCoder/leerProducto.html", contexto)


def editarProducto(request, elemento):

    producto = Productos.objects.get(elemento=elemento)

    if request.method == "POST":

        formulario1 =  CrearProducto(request.POST) #Importa de forms.py la class CrearProducto
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            producto.elemento = info["elemento"]    
            producto.precio = info["precio"]

            producto.save()

            return render(request, "AppCoder/inicio.html")

    else:
        formulario1 = CrearProducto(initial={"producto":producto.elemento,"precio":producto.precio})

    return render(request, "AppCoder/editarProducto.html", {"form1":formulario1, "producto":elemento}) 

#CRUD para subir imagenes
@login_required
def agregarAvatar(request):
    if request.method=="POST":
        
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario = usuarioActual, imagen = form.cleaned_data["imagen"])

            avatar.save()

            return render (request, "AppCoder/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render (request, "AppCoder/agregarAvatar.html", {"formulario":form})


#CRUD basadas en clases

class ListaProducto(LoginRequiredMixin, ListView):#Se genera en el html productos_list y productos_detail

    model = Productos  

class DetalleProducto(LoginRequiredMixin,DetailView):#Se genera en el html productos_list y productos_detail

    model = Productos

class CrearProducto(LoginRequiredMixin,CreateView):#Se genera en curso_form sirve para crear y actualizar productos

    model = Productos
    success_url= "/AppCoder/productos/list"
    fields = ["elemento","precio"]

class ActualizarProducto(LoginRequiredMixin,UpdateView):

    model = Productos
    success_url= "/AppCoder/productos/list"
    fields = ["elemento","precio"]

class BorrarProducto(LoginRequiredMixin,DeleteView):

    model = Productos
    success_url= "/AppCoder/productos/list"


