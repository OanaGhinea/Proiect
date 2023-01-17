from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Postare, Tipuri
from .forms import FormularePostare, EditPostare
from django.urls import reverse_lazy
# reverse
# from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

# def LikeView(request, pk):
#     postare = get_object_or_404(Postare, id = request.POST.get('postare_id'))
#     postare.likes.add(request.user)
#     return HttpResponseRedirect(reverse('articole_details', args=[str(pk)])),
#
# def LikeView(request, pk):
#     post = get_object_or_404(Postare, id=request.POST.get('postare_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('articole_details', args=[str(pk)])),

class HomeView(ListView):
    model = Postare
    template_name = 'home.html'
    tip  = Tipuri.objects.all()
    ordering = ['-data_postare']

    def get_context_data(self, *args, **kwargs):
        tip_categorie = Tipuri.objects.all()
        context =super(HomeView, self).get_context_data(*args, **kwargs)
        context['tip_categorie']=tip_categorie
        return context

def TipuriView(request, tip):
    tipuri_postari = Postare.objects.filter(tipuri=tip.replace('-',' '))
    return render (request, 'tipuri.html', {'tip':tip.title().replace('-',' '), 'tipuri_postari':tipuri_postari})

class ArticoleDetailView(DetailView):
    model = Postare
    template_name = 'articole_details.html'

class AdaugaPostareView(CreateView):
    model = Postare
    form_class = FormularePostare
    template_name = 'adauga_postare.html'
    # fields = '__all__'
    # fields = ("titlu","cuprins", "autor")

class AdaugaTipuriView(CreateView):
    model = Tipuri
    # form_class = FormularePostare
    template_name = 'adauga_tipuri.html'
    fields = '__all__'


class EditarePostareView(UpdateView):
    model = Postare
    template_name = 'editare_postare.html'
    # fields = ['titlu', 'titlu_nav', 'cuprins']
    form_class = EditPostare

class StergerePostareView(DeleteView):
    model = Postare
    template_name = 'stergere_postare.html'
    success_url = reverse_lazy('home')