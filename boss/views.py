from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt
def order_list(request, shop):
    if request.method =='GET':
        order_list = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list':order_list})
    else:
        return HttpResponse(status=404)

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        shop_id = order_item.shop_id
        order_item.estimated_time = int(request.POST['estimated_time'])
        order_item.save()
        return render(request, 'boss/success.html', {'shop':shop_id})
    else:
        return HttpResponse(status=404)