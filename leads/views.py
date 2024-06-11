from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import LeadForm, LeadModelForm
from .models import Agent, Lead


class LandingPageView(TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, "leads/lead_list.html", context)


class DetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }

    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


def lead_create(request):

    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form": form
    }

    return render(request, "leads/lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "lead": lead,
        "form": form
    }

    return render(request, "leads/lead_update.html", context)


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# * alternative method for updating a lead
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()

#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age

#             lead.save()

#             return redirect("/leads")

#     context = {
#         "lead": lead,
#         "form": form
#     }

#     return render(request, "leads/lead_update.html", context)

# * alternative method for creating a lead
# def lead_create(request):

#     form = LeadForm()

#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             # for now take the first agent
#             agent = Agent.objects.first()

#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )

#             return redirect("/leads")

#     context = {
#         "form": form
#     }

#     return render(request, "leads/lead_create.html", context)
