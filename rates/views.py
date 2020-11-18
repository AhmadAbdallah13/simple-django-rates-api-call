from django.shortcuts import render
from rates.codes import apirequests

def rates_view(request):
    context = {'error': 'no respo'}
    if(request.GET.get('latest')):
        context = apirequests.getLatestRates()
    if(request.GET.get('date')):
        context = apirequests.getRatesInYear( int(request.GET.get('yearINP')), 
                                              int(request.GET.get('monthINP')),
                                              int(request.GET.get('dayINP')))
    if(request.GET.get('symbols')):
        context = apirequests.getSpecificExchangeRates( request.GET.get('bas'), 
                                                        request.GET.get('sym'))

    return render(request, 'rates/rates_view.html', context)
