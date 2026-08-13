from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm
from .models import Profile
from posts.forms import PostForm
from posts.models import Post


def register_view(request):
    """Página de Cadastro"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso! Bem-vindo ao Socialize.")
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'profiles/register.html', {'form': form})


@login_required
def home_view(request):
    """Página Inicial interna (Feed + Criar Post)"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            messages.success(request, "Seu post foi publicado com sucesso!")
            return redirect('home')
    else:
        form = PostForm()

    # Traz os posts e já carrega os relacionamentos de Profile e User
    posts = Post.objects.select_related('author', 'author__user').all().order_by('-created_at')

    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, 'profiles/home.html', context)


@login_required
def delete_account_view(request):
    """Exclusão da conta do usuário"""
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.info(request, "Sua conta foi excluída com sucesso.")
        return redirect('login')

    return render(request, 'profiles/delete_confirm.html')


@login_required
def follow_toggle_view(request, profile_id):
    """Permite seguir ou deixar de seguir outro perfil"""
    target_profile = get_object_or_404(Profile, id=profile_id)
    my_profile = request.user.profile

    if my_profile != target_profile:
        if target_profile in my_profile.following.all():
            my_profile.following.remove(target_profile)
            messages.info(request, f"Você deixou de seguir {target_profile.user.username}.")
        else:
            my_profile.following.add(target_profile)
            messages.success(request, f"Agora você está seguindo {target_profile.user.username}!")

    next_url = request.META.get('HTTP_REFERER')
    if next_url:
        return redirect(next_url)
    return redirect('profile_detail', username=target_profile.user.username)


@login_required
def profile_detail_view(request, username):
    """Exibe a página de perfil de um usuário específico"""
    profile_user = get_object_or_404(User, username=username)
    profile = profile_user.profile
    posts = profile.posts.all().order_by('-created_at')

    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'profiles/profile_detail.html', context)


@login_required
def edit_profile_view(request):
    """Edição da foto e biografia do usuário logado"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})