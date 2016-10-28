from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request, 'main.html')

def feedback(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = Comment()
        comment.name = form.data['name']
        comment.mail = form.data['mail']
        comment.text = form.data['text']
        comment.save()
        return redirect('/feedback')

    return render(request, 'feedback.html')

@staff_member_required
def feedback_admin(request):
    comments = Comment.objects.all()
    return render(request, 'feedback_admin.html', {'comments': comments})

def underdev(request):
    return render(request, 'underdev.html')

def osago(request):
    return render(request, 'osago.html')

def kasko(request):
    return render(request, 'kasko.html')

def advantages(request):
    return render(request, 'advantages.html')

def requisites(request):
    return render(request, 'requisites.html')
