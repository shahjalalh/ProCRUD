from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import UserForm

# Create your views here.
def user_info(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.modified_date = timezone.now()
            user.save()
            return redirect('user_info')
    else:
        form = UserForm()
    return render(request, 'user_info/user_info.html', {'form': form})
