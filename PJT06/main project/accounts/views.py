from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from movies.models import Movie
from django.contrib.auth.decorators import login_required

# Create your views here.


# 로그인
@require_http_methods(['GET', 'POST'])
def login(request):
  if request.user.is_authenticated:
    return redirect('movies:index')

  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect(request.GET.get('next') or 'movies:index')
  else:
    form = AuthenticationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/login.html', context)


# 로그아웃
@login_required
def logout(request):
  if request.user.is_authenticated:
    auth_logout(request)
    return redirect('movies:index')


# 회원가입
@require_http_methods(['GET', 'POST'])
def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('movies:index')
  else:
    form = CustomUserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)

    
# 회원 정보 수정
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('movies:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context ={
    'form': form,
  }
  return render(request, 'accounts/update.html', context)


# 회원 정보 삭제
@login_required
@require_POST
def delete(request):
  request.user.delete()
  auth_logout(request)
  return redirect('movies:index')


# 비밀번호 변경
@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      return redirect('posts:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/change_password.html', context)

# 프로필 생성
@login_required
def profile(request, username):
  person = get_object_or_404(get_user_model(), username=username)
  
  movies = person.movie_user.all()
  
  context = {
    'person': person,
    'movies': movies,
    'username': username,
  }
  return render(request, 'accounts/profile.html', context)


# 팔로잉
@login_required
@require_POST
def follow(request, user_pk):
  if request.user.is_authenticated:
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person.followers.filter(pk=request.user.pk).exists():
      person.followers.remove(request.user)
    else:
      person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
  return redirect('accounts:login')


# 팔로워 리스트
@login_required
def follower_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followers = user.followers.all()
    return render(request, 'accounts/follower_list.html', {'followers': followers, 'person': user})


# 팔로윙 리스트
@login_required
def following_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followings = user.followings.all()
    return render(request, 'accounts/following_list.html', {'followings': followings, 'person': user})


# 좋아요 누른 영화 목록
@login_required
def like_movies_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    movies = Movie.objects.all()
    like_movies = user.like_movies.all()
    return render(request, 'accounts/like_movies_list.html', {'like_movies': like_movies, 'movies': movies, 'person': user})