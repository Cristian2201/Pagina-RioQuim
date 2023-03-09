from django.urls import path
from AppCoder import views
from AppCoder.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [                 # El nombre/ es lo que se muestra en la pagina.... http://127.0.0.1:8000/AppCoder/nosotros/
    path("", inicio, name="Inicio"),
    path('busqueda/', busqueda, name="Busqueda"),
    path("resultados/",resultadoBusqueda),
    path('ProductosLeer/', productos, name="Productos"),
    path('tienda/', tienda, name="Tienda"), 
    path('nosotros/', nosotros, name="Nosotros"),  # El name nos permite movernos entre pestañas en la pagina
    path("loginUser/", inicioSesion, name="Login"),
    path("registrarse/",registroUsuario , name="SingUp"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("agregar/",agregarAvatar, name="Avatar"),
    

    #Crear formularios con html
    path('crearUsuario/', crearUsuario, name="FormularioRegistro"),
    
    #busqueda de productos
    #path("buscarProducto/",buscarProducto, name="BusquedaProductos"),
    path("resultados/",resultadoBusqueda),

    #CRUD de productos
    path('leerProducto/',leerProducto, name="ProductoVeer"),
    path('crearProducto/',crearProducto, name="ProductoCreado"),
    path("eliminarProducto/<id>/",eliminarProducto, name="ProductoEliminar"),
    path("editarProducto/<id>/",editarProducto, name="ProductoEditar"),


    #CRUD de Productos usando Clases

    path('productos/list/',ListaProducto.as_view(), name="ProductosLeer"),
    path('productos/<int:pk>/',DetalleProducto.as_view(), name="ProductosDetalle"),
    path('productos/crear/',CrearProducto.as_view(), name="ProductosCrear"),
    path('productos/editar/<int:pk>',ActualizarProducto.as_view(), name="ProductosEditar"),
    path('productos/borrar/<int:pk>',BorrarProducto.as_view(), name="ProductosBorrar"),

]

