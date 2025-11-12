from django.shortcuts import render, redirect
from .models import LottoTicket
from django.contrib.auth.models import User

def home(request):
    tickets = LottoTicket.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tickets': tickets})

def buy_ticket(request):
    user, _ = User.objects.get_or_create(username='guest')  # 임시 사용자
    if request.method == 'POST':
        mode = request.POST.get('mode')
        if mode == 'auto':
            numbers = LottoTicket.generate_auto_numbers()
        else:
            numbers = request.POST.get('numbers')
        LottoTicket.objects.create(user=user, numbers=numbers)
        return redirect('home')
    return render(request, 'buy.html')

