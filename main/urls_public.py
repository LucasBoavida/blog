from django.urls import path
from main.views import *

urlpatterns = [
    # path (urls, view, file name)
    path('', index, name='home'),
    path('post-detail/', detailPost, name='detailPost'),
    path('about/', about, name='konaba'),
    path('my-portfolio/', myPortfolio, name='myportfolio'),
    path('partnership/', partnership, name='partnership'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
]