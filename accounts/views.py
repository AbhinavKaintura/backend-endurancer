from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.http import JsonResponse
import json




# ====================
# User views
# ====================

@csrf_exempt
def get_user(request):
    """
        Retrieve user information.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    data = json.loads(request.body)
    user_name = data.get('username')

    if not user_name:
        return JsonResponse({'error': 'Username is required.'}, status=400)

    try: 
        user = User.objects.filter(username=user_name).first()
        if not user:
            return JsonResponse({'error': 'User not found.'}, status=404)

        user_data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_of_birth': user.date_of_birth,
            'is_active': user.is_active,
        }
        return JsonResponse(user_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

@csrf_exempt
def new_user(request):
    """
        Create a new user.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
    data = json.loads(request.body)
    username = data.get('username')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    date_of_birth = data.get('date_of_birth')
    is_active = data.get('is_active')

    if not all([username, email, first_name, last_name, date_of_birth, is_active]):
        return JsonResponse({'error': 'All fields are required.'}, status=400)

    try:
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            is_active=is_active
        )
        return JsonResponse({'message': 'User created successfully.', 'user_id': user.id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    
@csrf_exempt
def delete_user(request):
    """
        Delete a user.
    """
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    data = json.loads(request.body)
    user_name = data.get('username')

    if not user_name:
        return JsonResponse({'error': 'Username is required.'}, status=400)

    try:
        user = User.objects.filter(username=user_name).first()
        if not user:
            return JsonResponse({'error': 'User not found.'}, status=404)

        user.delete()
        return JsonResponse({'message': 'User deleted successfully.'}, status=204)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    
@csrf_exempt
def get_all_user(request):
    """
        Retrieve all users.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    try:
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_of_birth': user.date_of_birth,
                'is_active': user.is_active,
            })
        return JsonResponse(user_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
