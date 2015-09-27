from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from profiles.models import Profiles
# Create your views here.
class ProfilesForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['idnum', 'name', 'age', 'school', 'course', 'year']

def profiles_list(request, template_name='profiles/profiles_list.html'):
    profiles = Profiles.objects.all()
    data = {}
    data['object_list'] = profiles
    return render(request, template_name, data)

def profiles_create(request, template_name='profiles/profiles_form.html'):
    form = ProfilesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profiles_list')
    return render(request, template_name, {'form':form})

def profiles_update(request, pk, template_name='profiles/profiles_form.html'):
    profiles = get_object_or_404(Profiles, pk=pk)
    form = ProfilesForm(request.POST or None, instance=profiles)
    if form.is_valid():
        form.save()
        return redirect('profiles_list')
    return render(request, template_name, {'form':form})

def profiles_delete(request, pk, template_name='profiles/profiles_confirm_delete.html'):
    profiles = get_object_or_404(Profiles, pk=pk)    
    if request.method=='POST':
        profiles.delete()
        return redirect('profiles_list')
    return render(request, template_name, {'object':profiles})