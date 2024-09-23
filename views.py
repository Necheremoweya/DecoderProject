from django.shortcuts import render

# Credef decode_message(request)def    decoded_message = None
def decode_message(request):
    decoded_message = None
    if request.method == 'POST':
        encoded_message = request.POST.get('encoded_message')
        decoded_message = encoded_message[::-1]  # Simple decoding by reversing the string
    
    return render(request, 'decoderapp/decode_message.html', {'decoded_message': decoded_message}) 