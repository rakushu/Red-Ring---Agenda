from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .forms import ContactAddForm, ContactAddModelForm
# from django.contrib.auth import User

# Create your views here.
from .models import Contacto

def contact_list_page(request):
    qs = Contacto.objects.filter(owner=request.user)
    template_name = 'contact_list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)

def contact_create_page(request):
    form = ContactAddModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        # Contacto.objects.create(**form.cleaned_data)
        # form = ContactAddForm()
        return redirect('/contactos')
    context = {
            "form": form
        }
    return render(request, 'contact_create.html', context)

def contact_detail_page(request, contact_id):
    obj = Contacto.objects.get(id=contact_id)
    template_name = 'contact_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def contact_update_page(request, contact_id):
    obj = Contacto.objects.get(id=contact_id)
    form = ContactAddModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/contactos')
    template_name = 'contact_update.html'
    context = {"form": form, "title": f"Actualiza {obj.id}"}
    return render(request, template_name, context)

def contact_delete_page(request, contact_id):
    obj = Contacto.objects.get(id=contact_id)
    template_name = 'contact_delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/contactos')
    context = {"object": obj}
    return render(request, template_name, context)

# class contact_list_by_user(ListView):
#     model = Contacto
#     template_name = "contact_list.html"
#     context = "all_contacts_by_user"

#     def get_queryset(self):
#         return Contacto.objects.filter(owner=self.request.user)