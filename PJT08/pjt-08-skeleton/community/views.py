from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_safe,
    require_POST,
    require_http_methods,
)
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        parent_comment_id = request.POST.get('parent_comment_id')  # 부모 댓글의 ID를 POST 요청해서 가져오기
        parent_comment = None  # 초기값: 부모 댓글을 선택하지 않는 경우
        if parent_comment_id:  # 부모 댓글의 ID가 존재하는 경우
            parent_comment = get_object_or_404(Comment, pk=parent_comment_id)  # 해당 ID를 가진 부모 댓글 가져오기

        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.parent_comment = parent_comment  # 대댓글의 부모 댓글 설정
        comment_form.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)



# @login_required  # 로그인 했을 때만 좋아요 가능
# def like(request):
#     review_id = request.POST.get('review_id')   # POST 요청에서 'review_id' 가져오기
#     review = get_object_or_404(Review, pk=review_id)  # 'review_id'에 해당하는 리뷰 가져오기


#     if request.user in review.like_users.all():  # 사용자가 이미 해당 리뷰를 좋아요한 경우
#         review.like_users.remove(request.user)  # 사용자의 좋아요를 취소하고 
#         liked = False  # liked 변수를 False로 설정

#     else:  # 사용자가 해당 리뷰를 좋아요하지 않은 경우
#         review.like_users.add(request.user)  # 사용자의 좋아요를 추가하고 
#         liked = True  # liked 변수를 True로 설정


#     return JsonResponse({'liked': liked, 'like_count': review.like_users.count()})  # JavaScript로 비동기 요청을 처리하기 위해 JSON 응답을 반환


@login_required
@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True
        context = {
            'is_liked' : is_liked,
            'likes_count' : review.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')