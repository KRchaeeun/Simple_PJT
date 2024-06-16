from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    User = get_user_model()
    # person : 상대방, request.user : 로그인 상태의 유저
    person = User.objects.get(pk=user_pk)
    # 로그인 상태의 유저(자기 자신)이 아닌 경우에만 팔로우 가능
    if person != request.user:
        # 팔로우가 되어있으면 언팔로우
        if request.user in person.followers.all():
            person.followers.remove(request.user)
            is_followed = False
        # 언팔로우 상태인 경우 팔로우
        else:
            person.followers.add(request.user)
            is_followed = True
        # JSON형식으로 넘길 데이터
        # if_followed : 팔로우, 언팔로우 여부
        # followings_count : 팔로잉 인원 수
        # followers_count : 팔로우 인원 수
        context = {
            'is_followed' : is_followed,
            'followings_count': person.followings.count(),
            'followers_count': person.followers.count(),
        }
        return JsonResponse(context)
    # return redirect('accounts:profile', person.username)
