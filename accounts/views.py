from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({"msg": "User created successfully"})