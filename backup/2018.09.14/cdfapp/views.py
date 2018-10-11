from django.shortcuts import render, redirect
from .forms import ContactoForm

def home(request):
    return render(request, 'home.html', {})

def contacto(request):
	
#	if request.method == "POST":
#		raise Exception("Metodo: " + request.method)
#		form = ContactoForm(request.POST)
#		if form.is_valid():
#			Contacto = form.save(commit=True)
 				
#		return redirect('home')
	if request.method == "POST":
		raise Exception("Metodo POST: " + request.method)
#		form = ContactoForm(request.POST)
#		if form.is_valid():
#			Contacto = form.save(commit=True)
#			raise Exception("Is valild: ")
#		else:
#			raise Exception("Is NOT valild: ")
#		raise Exception("Metodo: " + request.method)
	else:
		form = ContactoForm()
#		raise Exception("Metodo Otro: " + request.method)
			
	return render(request, 'contacto.html', {'form': form})
	