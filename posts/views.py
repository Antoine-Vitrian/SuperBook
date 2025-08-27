from django.views.generic import ListView
from .models import Post
from django.shortcuts import render

def lista_herois(request):
    postagens = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": postagens})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_herois.html"
    context_object_name = "posts"
