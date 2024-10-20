from django.shortcuts import render,redirect
from users.forms import RegisterUserForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
	if request.method=="POST":
		form=RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Пользователь {username} зарегистрирован!')
			return redirect('index')
	else:
		form=RegisterUserForm()

	context={
		'form':form,
	}
	return render(request,"users/register.html",context)
