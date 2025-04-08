from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BookingHistory
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def book_vehicle(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        car_name = data.get("car_name")
        price = data.get("price")
        days = data.get("days")
        total_price = price * days
        
        # Save booking history
        BookingHistory.objects.create(
            name=user.first_name or user.username,
            email=user.email,
            phone_number=data.get("phone_number"),
            car_name=car_name,
            price=total_price,
            days=days,
        )
        return JsonResponse({"message": "Booking successful!"}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)
