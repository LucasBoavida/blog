from django.urls import path
from main.views import *
# form kompara ho lin. php maka include
# view ne'e kompara ho seluk maka nia menu sira


urlpatterns = [
    #admin
    path('', IndexAdmin, name='IndexAdmin'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),

    path('admin-portfolio',AdminPortfolio, name='admin-portfolio'),
    path('admin-portfolio/add',AdminPortfolioAdd, name='admin-portfolio-add'),
    path('admin-portfolio/update/<str:id>',AdminPortfolioUpdate, name='admin-portfolio-update'),
    path('admin-portfolio/delete/<str:id>',AdminPortfolioDelete, name='admin-portfolio-delete'),

    path('admin-project',AdminProject, name='admin-project'),
    path('admin-project/add',AdminProjectAdd, name='admin-project-add'),
    path('admin-project/update/<str:id>',AdminProjectUpdate, name='admin-project-update'),
    path('admin-project/delete/<str:id>',AdminProjectDelete, name='admin-project-delete'),

    path('admin-categoria',AdminCategoria, name='admin-categoria'),
    path('admin-categoria/add',AdminCategoriaAdd, name='admin-categoria-add'),
    path('admin-categoria/update/ <str:id>',AdminCategoriaUpdate, name='admin-categoria-update'),
    path('admin-categoria/delete/ <str:id>',AdminCategoriaDelete, name='admin-categoria-delete'),

    path('admin-post/', AdminPost, name='admin-post'),
	path('admin-post/add', AdminPostAdd, name='admin-post-add'),
	path('admin-post/update/<str:pk>', AdminPostUpdate, name='admin-post-update'),
	path('admin-post/delete/<str:pk>', AdminPostDelete, name='admin-post-delete'),

	path('admin-post/load-post-update-form', AdminPostLoadUpdateForm, name='load-post-update-form'),

	# path('create_post/', create_post, name='create_post'),
 
	path('user/change/password', UserPasswordChange.as_view(), name='user-change-password'),
	path('user/change/account', UserChangeAccount, name='user-change-account'),
]