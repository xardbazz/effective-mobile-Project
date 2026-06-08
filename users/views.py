from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from rest_framework_simplejwt.tokens import RefreshToken  # if DRF/JWT

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign default role
            default_role = Role.objects.get(name='employee')
            UserRole.objects.create(user=user, role=default_role)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # or custom backend
        if user and user.is_active:
            login(request, user)
            # JWT example:
            # refresh = RefreshToken.for_user(user)
            # return JsonResponse({'refresh': str(refresh), 'access': str(refresh.access_token)})
            return redirect('home')
        else:
            # 401 logic
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

# Profile update, soft delete similar (set is_active=False, logout)