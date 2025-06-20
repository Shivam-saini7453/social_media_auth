from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# # ------------------ SIGN UP ------------------ #
# def signup_view(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 != password2:
#             messages.error(request, "❌ Passwords do not match.")
#             return redirect('signup')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, f"❌ Username '{username}' is already taken.")
#             return redirect('signup')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, f"❌ Email '{email}' is already registered.")
#             return redirect('signup')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1,
#             first_name=first_name,
#             last_name=last_name
#         )

#         # Explicitly set the backend if using multiple backends
#         user.backend = 'django.contrib.auth.backends.ModelBackend'
#         login(request, user)

#         return redirect('signin')

#     return render(request, 'signup.html')

# # ------------------ SIGN IN ------------------ #
# def signin_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # ✅ uses the URL name

#         else:
#             messages.error(request, "❌ Invalid username or password.")
#             return redirect('signin')

#     return render(request, 'signin.html')

# # ------------------ SIGN OUT ------------------ #
# def signout_view(request):
#     logout(request)
#     return redirect('signin')

# # ------------------ DASHBOARD ------------------ #

# from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

