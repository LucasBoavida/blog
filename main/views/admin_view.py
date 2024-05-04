from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from main.models import *

from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

from main.forms import *

@login_required
def IndexAdmin(request):
    return render(request, 'adminpage/index.html')

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('IndexAdmin')
		else:
			messages.error(request,'Username ou Password la loos! Favor Prense fali!')
	context = {
		"title":"Pajina Login",
	}
	return render(request,'auth/login.html',context)

@login_required
def logoutPage(request):
	logout(request)
	return render(request,'auth/logout.html')

from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
class UserPasswordChange(PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('user-change-password')
    def get_success_url(self):
        messages.success(self.request,'Password troka ho successu')
        return super().get_success_url()
    def get_context_data(self, **kwargs): 
        return super().get_context_data(**kwargs)
        

@login_required
def AdminPortfolio(request):
    objects = Porfolio.objects.all()
    context = {
        'objects': objects
    }
    return render(request,'adminpage/portfolio.html',context)

@login_required
def AdminPortfolioAdd(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Rai Dadus Portfolio ho sucessu!')
            return redirect('admin-portfolio')
    else:
        form = PortfolioForm()
    context = {
        'title':"Formulario Rejistu Portfolio",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminPortfolioUpdate(request,id):
    dataportfolio = Porfolio.objects.get(id=id)
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=dataportfolio)
        if form.is_valid():
            form.save()
            messages.success(request,'update Dadus Portfolio ho sucessu!')
            return redirect('admin-portfolio')
    else:
        form = PortfolioForm(instance=dataportfolio)
    context = {
        'title':"Formulario Update Portfolio",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminPortfolioDelete(request,id):
    dataportfolio = Porfolio.objects.get(id=id)
    dataportfolio.delete()
    messages.error(request,f'delete Dadus Portfolio {dataportfolio.titulu} ho sucessu!')
    return redirect('admin-portfolio')

@login_required
def AdminProject(request):
    objects = Project.objects.all()
    context = {
        'title':'lista project',
        'objects': objects
    }
    return render(request,'adminpage/project.html',context)

@login_required
def AdminProjectAdd(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Rai Dadus Project ho sucessu!')
            return redirect('admin-project')
    else:
        form = ProjectForm()
    context = {
        'title':"Formulario Rejistu Project",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminProjectUpdate(request,id):
    # dataproject = Project.objects.get(id=id)
    data = get_object_or_404(Project,id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'update Dadus Project ho sucessu!')
            return redirect('admin-project')
    else:
        form = ProjectForm(instance=data)
    context = {
        'title':"Formulario Update Project",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminProjectDelete(request,id):
    dataproject = Project.objects.get(id=id)
    dataproject.delete()
    messages.error(request,f'delete Dadus Project ho sucessu!')
    return redirect('admin-project')

@login_required
def AdminCategoria(request):
    objects = Categoria.objects.all()
    context = {
         'objects': objects
    }
    return render(request,'adminpage/categoria.html',context)

@login_required
def AdminCategoriaAdd(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Rai Dadus Categoria ho sucessu!')
            return redirect('admin-categoria')
    else:
        form = CategoriaForm()
    context = {
        'title':"Formulario Rejistu Categoria",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminCategoriaUpdate(request,id):
    datacategoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST,instance=datacategoria)
        if form.is_valid():
            form.save()
            messages.success(request,'update Dadus Categoria ho sucessu!')
            return redirect('admin-categoria')
    else:
        form = CategoriaForm(instance=datacategoria)
    context = {
        'title':"Formulario Update Categoria",
        'form' : form,
    }
    return render(request, 'adminpage/add_portfolio.html',context)

@login_required
def AdminCategoriaDelete(request,id):
    datacategoria = Categoria.objects.get(id=id)
    datacategoria.delete()
    messages.error(request,'delete Dadus categoria ho sucessu!')
    return redirect('admin-categoria')

@login_required
def AdminPost(request):
	objects = Post.objects.all()
	context = {
		'objects':objects,
		'title':"Lista Publikasaun",
		'page':"lista_post",
	}
	return render(request,'adminpage/posts.html',context)

@login_required
def AdminPostAdd(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			form.save_m2m()
			messages.success(request,'Dadus Post Rejistadu ho Susesu!')
			return redirect('admin-post')
	else:
		form = PostForm()
	context = {
		'title':"Formulario Rejistu Publikasaun",
		'form':form,
		'page':"form_post",
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPostUpdate(request,pk):
	objects = get_object_or_404(Post,id=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance=objects)
		if form.is_valid():
			post = form.save(commit=False)
			# post.author = request.user
			post.save()
			form.save_m2m()
			messages.success(request,'Dadus Post Atualizadu ho Susesu!')
			return redirect('admin-post')
	else:
		form = PostForm(instance=objects)
	context = {
		'title':"Formulario Atualiza Publikasaun",
		'form':form,
		'page':"form_post",
	}
	return render(request,'adminpage/add_portfolio.html',context)

@login_required
def AdminPostDelete(request,pk):
	objects = get_object_or_404(Post,id=pk)
	objects.delete()
	messages.error(request,f'Dados Publikasaun {objects.title} hamoos ona ho susesu!')
	return redirect('admin-post')

@login_required
def AdminPostLoadUpdateForm(request):
	if request.method == 'GET':
		object_id = request.GET.get('objectID')
		objects = get_object_or_404(Post,id=object_id)
		form = PostForm(instance=objects)
	context = {
		'form':form,
		'objects':objects,
	}
	return render(request,'adminpage/posts_load_form.html',context)

@login_required
def UserChangeAccount(request):
    loginUser = get_object_or_404(User,id=request.user.id)
    if request.method == 'POST':
        form = UserAccountForm(request.POST,instance=loginUser)
        if form.is_valid():
            form.save()
            messages.success(request,f'Username atualiza ho sucessu')
            return redirect('user-change-account')
    else:
        form = UserAccountForm(instance=loginUser)

    context = {
        'form':form,
        'title': "altera username",
    }
    return render(request,'adminpage/add_portfolio.html',context)

