
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from comments.forms import ComentarioForm

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, 'posts/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })
