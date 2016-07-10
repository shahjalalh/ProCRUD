from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import UserForm
from .models import User

# Create your views here.
def user_list(request):
    users = User.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'user_info/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_info/user_detail.html', {'user': user})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.modified_date = timezone.now()
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'user_info/user_info.html', {'form': form})

def user_info(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.modified_date = timezone.now()
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_info/user_info.html', {'form': form})
