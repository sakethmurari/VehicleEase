from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.
from registerpage.models import Register
from cartpage.models import vehicle
from historypage.models import BookingHistory
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Register.objects.get(email=email)
            if password == user.password:
                request.session['user_id'] = user.id
                return redirect('welcome')
            
            else:
                return HttpResponse("Invalid password.")
        except Register.DoesNotExist:
            return HttpResponse("User does not exist.")
    return render(request, 'login.html')


def welcome(request):
    vehicles = vehicle.objects.filter(book=False)
    user_id = request.session.get('user_id')
    if user_id:
        user = Register.objects.get(id=user_id)
        return render(request, 'welcome.html', {'user':user,'vehicles':vehicles,})
    return redirect('login')

def logout(request):
    request.session.flush()
    return redirect('home')


def book_vehicle(request):
    print(request)
    if request.method == 'POST':
        id = request.POST.get('id')
        email = request.POST.get('email')
        type = request.POST.get('type')
        name = request.POST.get('vehicle_name')
        price = int(request.POST.get('price'))
        days = int(request.POST.get('days'))
        car_number = request.POST.get('car_number')
        # print(id)
        # print(email)
        # print(type)
        # print(name)
        actual_price = price
        price = price*days
        # print(price)
        # print(days)
        try:
            BookingHistory.objects.create(email=email,type=type,car_name=name,price=price,days=days,actual_price=actual_price,car_number=car_number)
            obj = vehicle.objects.get(id=id)
            obj.book = True
            obj.save()
            return redirect('welcome')
        except:
            return HttpResponse(f"Booking not successful ")



def history(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  
    try:
        user = Register.objects.get(id=user_id)
        email = user.email
        historys = BookingHistory.objects.filter(email=email)
        return render(request, 'history.html', {'historys': historys})
    except Register.DoesNotExist:
        return HttpResponse("User not found.")
    except BookingHistory.DoesNotExist:
        return HttpResponse("No booking history found.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")



def profile(request):
    user_id = request.session.get('user_id')
    user = Register.objects.get(id=user_id)
    return render(request,'profile.html',{'user':user})


# def update_profile(request,id):
#     user = Register.objects.get(id=id) # Get the currently logged-in user
#     if request.method == 'POST':
#         # Update user profile with form data
#         user.username = request.POST.get('username')
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         user.age = request.POST.get('age')
#         user.profession = request.POST.get('profession')
#         user.phone = request.POST.get('phone')
#         user.location = request.POST.get('location')
#         user.landmark = request.POST.get('landmark')
#         user.save()  # Save the updated profile
#         # Redirect to the profile page
#         return redirect('profile')  # You can change 'profile' to the name of your profile view
#     return render(request, 'update_profile.html', {'user': user})

def update_profile(request, id):
    user = Register.objects.get(id=id)  # Get the currently logged-in user
    if request.method == 'POST':
        # Get form data
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')
        new_age = request.POST.get('age')
        new_profession = request.POST.get('profession')
        new_phone = request.POST.get('phone')
        new_location = request.POST.get('location')
        new_landmark = request.POST.get('landmark')

        # # Check if the email is unique
        # if Register.objects.filter(email=new_email).exclude(id=user.id).exists():
        #     return HttpResponse('This email is already in use by another account.')

        # # Check if the phone number is unique
        # if Register.objects.filter(phone=new_phone).exclude(id=user.id).exists():
        #     return HttpResponse('This phone number is already in use by another account.')

        # Update user profile with validated data
        user.username = new_username
        user.email = new_email
        user.password = new_password  # Ensure hashing is applied for passwords
        user.age = new_age
        user.profession = new_profession
        user.phone = new_phone
        user.location = new_location
        user.landmark = new_landmark
        user.save()  # Save the updated profile

        # Redirect to the profile page
        return redirect('profile')  # You can change 'profile' to the name of your profile view

    return render(request, 'update_profile.html', {'user': user})


# Update View
def history_update(request, id):
    booking = BookingHistory.objects.get(id = id)
    # print("your booking item",booking)
    actual_price = booking.actual_price
    # print(actual_price)
    if request.method == 'POST':
        booking.car_name = request.POST.get('car_name', booking.car_name)
        booking.type = request.POST.get('type', booking.type)
        booking.days = request.POST.get('days', booking.days)
        # print(actual_price)
        cost = int(booking.days)*actual_price

        booking.price = cost
        booking.save()
        return redirect('history')  
    return render(request, 'history_update.html', {'booking': booking})

# Delete View
def history_remove(request, id):
    try:
        # Retrieve the booking history and associated vehicle
        booking = BookingHistory.objects.get(id=id)
        bandi = vehicle.objects.get(car_number=booking.car_number)

        # Update the vehicle status and save
        bandi.book = False
        bandi.save()

        # Delete the booking history
        booking.delete()

        return redirect('welcome')  # Redirect to the history page
    except BookingHistory.DoesNotExist:
        return HttpResponse("Booking history not found.")
    except vehicle.DoesNotExist:
        return HttpResponse("Vehicle not found.")
    except Exception as e:
        return HttpResponse(f"Sorry, unable to delete: {e}")
