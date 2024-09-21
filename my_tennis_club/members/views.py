from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import pytz
from .models import Result

def my_view(request):
    current_time_utc = timezone.now()
    
    wat_timezone = pytz.timezone('Africa/Lagos')
    current_time_wat = current_time_utc.astimezone(wat_timezone)

    context = {
        'current_time': current_time_wat,
        'current_timezone': wat_timezone,
    }

    return render(request, 'result.html', context)

def result_page(request):
    results = None
    if request.method == "POST":
        name = request.POST.get("name")
        first_name, last_name = name.split() if ' ' in name else (name, '')
        results = Result.objects.filter(first_name=first_name, last_name=last_name)

    context = {
        'results': results,
        'current_time': timezone.now(),
        'current_timezone': pytz.timezone('Africa/Lagos'),
    }
    
    return render(request, 'result.html', context)

def members(request):
    return render(request, 'index.html')

def ai_page(request):
    return render(request, 'ai.html')

def blockchain_page(request):
    return render(request, 'blockchain.html')

def bi_page(request):
    return render(request, 'bi.html')

def cybersecurity_page(request):
    return render(request, 'cybersecurity.html')

def dataanalytics_page(request):
    return render(request, 'dataanalytics.html')

def softwareengineering_page(request):
    return render(request, 'softwareengineering.html')