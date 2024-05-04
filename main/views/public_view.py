from django.shortcuts import render,redirect,get_object_or_404
from main.models import *

from django.contrib.auth.decorators import login_required
# from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

from main.forms import *

def index(request):
    context = {
        'title': "Home Page"
    }
    return render(request,'index.html', context)

def detailPost(request):
    return render(request,'posts.html',object)

def about(request):
    context = {
        'title': "About"
    }
    return render(request,'about.html', context)

def myPortfolio(request):
    dados_portfolio = Porfolio.objects.all()
    print(dados_portfolio)

    context = {
        'title': "My-Portfolio",
        'portfolio_active':"active",
        'dados_port':dados_portfolio,
    }
    return render(request,'myPortfolio.html', context)

def partnership(request):

    context = {
        'title': "Partnership"
    }
    return render(request,'partnership.html', context)

def contact(request):
    context = {
        'title': "Contact"
    }
    return render(request,'contact.html', context)

def post(request):
    objects = Post.objects.filter(status="published").all()
    post_image_urls = []
    for post in objects:
        image_url,text = extract_images_from_post_content(post.content)
        _,words20 = extract_total_words(text)
        post_image_urls.append({
            'id':post.id,
            'title':post.title,
            'image':image_url,
            'headline':words20,
            'publication_date':post.publication_date,
        })
        print('post_image_urls:',post_image_urls)
    context = {
        'title': "post",
        'post_active': "active",
        'post_image_urls':post_image_urls,
        'dados' : objects,
    }
    return render(request,'post.html', context)

from bs4 import BeautifulSoup

def extract_images_from_post_content(content):
    soup = BeautifulSoup(content,'html.parser')

    images = soup.find_all('img')

    text = soup.get_text(separator='')
    text = ''.join(text.split())

    images_urls = [img['src'] for img in images]

    return images_urls,text

def extract_total_words(text):
    words = text.split()

    words10 = ' '.join(words[:10])
    words20 = ' '.join(words[:20])

    return words10,words20
