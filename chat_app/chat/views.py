from django.http import JsonResponse
from .models import Message

def handle_message(request):
    sender = request.POST.get('sender')
    receiver = request.POST.get('receiver')
    content = request.POST.get('content')

    # Process the message and generate a response using the AI model
    response = generate_response(content)

    # Save the conversation to the database
    message = Message(sender=sender, receiver=receiver, content=content)
    message.save()

    return JsonResponse({'response': response})