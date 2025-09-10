from django.views.generic import ListView
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm

def lista_posts(request):
    postagens = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": postagens})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, "posts/form_posts.html", {"form": form})
