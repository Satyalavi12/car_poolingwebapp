from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Userdetails
from .forms import UserdetailsForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Userdetails,MyModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def base(request):
    return render(request,'base.html')
@login_required
def create_userdetails(request):
    user_id = request.user.id
    print(user_id)
    if request.method == 'POST':
        form = UserdetailsForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data['distance']
            distance_per_km = 5  # Assuming a fixed price of $5 per km
            price = distance * distance_per_km
            form.instance.distance_per_km = distance_per_km  # Set the distance_per_km value
            form.instance.price = price
            form.save()
            return redirect('app:display_price', price=price)
    else:
        form = UserdetailsForm()
    return render(request, 'userdetails/create_userdetails.html', {'form': form})
def display_price(request, price):
    price_float = float(price)
    return render(request, 'userdetails/displayprice.html', {'price': price_float})

def userdetails_list(request):
    userdetails = Userdetails.objects.all()
    print(userdetails)
    return render(request, 'userdetails/userdetails_list.html', {'userdetails': userdetails})

def accept(request, userdetail_id):
    userdetail = Userdetails.objects.get(pk=userdetail_id)
    send_mail(
        'Carpool Request Accepted',
        'Your carpool request has been accepted.',
        'your_email@example.com',  # Replace with your email
        [userdetail.email],
        fail_silently=False,
    )
    # Add your logic to handle accepting the request
    return redirect('app:userdetails_list')

def reject(request, userdetail_id):
    userdetail = Userdetails.objects.get(pk=userdetail_id)
    send_mail(
        'Carpool Request Rejected',
        'Your carpool request has been rejected.',
        'your_email@example.com',  # Replace with your email
        [userdetail.email],
        fail_silently=False,
    )
    # Add your logic to handle rejecting the request
    return redirect('app:userdetails_list')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('app:userdetails_list')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')  # Redirect to login page after successful registration
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def dashboard_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        riders = Userdetails.objects.all()  # Assuming Userdetails is your rider model
        return render(request, 'dashboard.html', {'riders': riders})
    else:
        return redirect('app:login')

def index(request):
    return render(request, 'riderhome.html')


def logout_view(request):
    logout(request)
    return redirect('app:index')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def sos(request):
    send_mail(
        'Emergency Alert',
        'I am in a Problem.',
        'your_email@example.com',  # Replace with your email
        ['kranthikumarkantamneni@gmail.com'],  # Enclosed email address within quotes
        fail_silently=False,
    )
    # Add your logic to handle rejecting the request
    return HttpResponse("No worries police is on the way")


from django.shortcuts import render, redirect
from .forms import URLForm

def save_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:success_url')  # Redirect to a success page
    else:
        form = URLForm()
    return render(request, 'userdetails/url_form.html', {'form': form})

from django.shortcuts import render
from .models import Trip
def h(request):
    trips = Trip.objects.all()
    return render(request, 'userdetails/homepage.html',{'trips': trips})

from django.shortcuts import render
from .models import MyModel

def index(request):
    my_model_instance = MyModel.objects.first()  # Assuming you have only one instance
    image_url = my_model_instance.image.url if my_model_instance else None
    return render(request, 'index.html', {'image_url': image_url})

def success_url(request):
    return render(request, 'userdetails/success_url.html')

def pay(request):
    return render(request, 'userdetails/payment.html')


from django.shortcuts import render, redirect
from .models import Trip

def trip_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start = request.POST.get('start')
        via = request.POST.get('via')
        destination = request.POST.get('destination')
        start_date = request.POST.get('startdate')
        start_time = request.POST.get('starttime')
        
        # Now you can use these variables to create a new Trip instance or do whatever you want with the data.
        trip = Trip.objects.create(
            name=name,
            start=start,
            via=via,
            destination=destination,
            start_date=start_date,
            start_time=start_time
        )
        return redirect('app:trip_success')
    else:
        return render(request, 'trip_form.html')

def trip_success(request):
    return render(request, 'trip_success.html')


