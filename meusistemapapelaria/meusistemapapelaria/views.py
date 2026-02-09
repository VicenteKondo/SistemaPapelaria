from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Pagina inicial

def pagina_inicial(request) :
    return render(request, 'meusistemapapelaria/pagina_inicial.html')