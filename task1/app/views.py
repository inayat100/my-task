from django.shortcuts import render,redirect,HttpResponse
from .models import Items ,Buyer,Seller,Invoice
from .make_pdf import render_to_pdf,html_to_pdf
# Create your views here.
from rest_framework.decorators import api_view
from .serializer import Buyerseri,Sellerseri,Itemseri
from rest_framework.response import Response

@api_view(['GET','POST'])
def create_invoice_api(request):
    if request.method == 'POST':
        seller_data={
        'name' :request.data['sellarname'],
        'phone' : request.data['sellarphone'],
        'address' : request.data['sellaraddress']
        }
        buyer_data = {
            'name' :request.data['buyername'],
        'phone' : request.data['buyerphone'],
        'address' : request.data['buyeraddress']
        }
        buyer_seri = Buyerseri(data=buyer_data)
        seller_seri = Sellerseri(data=seller_data)
        if buyer_seri.is_valid() and seller_seri.is_valid():
            buyer_seri.save()
            seller_seri.save()
        buyer = Buyer.objects.last()
        seller = Seller.objects.last()
        items = Items.objects.filter(is_invoice=False)
        invoice = Invoice(buyer_id=buyer,seller_id=seller)
        invoice.save()
        total = 0.0
        for i in items:
            invoice.items_ids.add(i.id)
            total += i.price
            invoice.save()
        for item in items:
            item.is_invoice = True
            item.save()
        filename = f'{seller.name}-{buyer.name}-{buyer.id}+{seller.id}'
        pdf = html_to_pdf('pdf_invoice.html',filename,{'object':invoice,'total':round(total, 3)})
        return Response({'invoice':f'/media/{filename}.pdf'})
    objs = Items.objects.filter(is_invoice=False)
    items_objs = Itemseri(objs,many=True)
    return Response({'data':items_objs.data})



@api_view(['POST'])
def add_item_api(request):
    if request.method == 'POST':
        print('==',request.data)
        # data = float(request.data['price'])
        # request.data['price'] = data
        item_seri = Itemseri(data=request.data)
        if item_seri.is_valid():
            item_seri.save()
        objs = Items.objects.filter(is_invoice=False)
        items_objs = Itemseri(objs,many=True)
        return Response({'object':items_objs.data})




def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        obj = Items(name=name,quantity=quantity,price=float(price))
        obj.save()
        
    return redirect('/')

def create_invoice(request):
    if request.method == 'POST':
        seller_name = request.POST['sellarname']
        seller_phone = request.POST['sellarphone']
        seller_address = request.POST['sellaraddress']
        buyer_name = request.POST['buyername']
        buyer_phone = request.POST['buyerphone']
        buyer_address = request.POST['buyeraddress']
        seller = Seller(name=seller_name,phone=seller_phone,address=seller_address)
        buyer = Buyer(name=buyer_name,phone=buyer_phone,address=buyer_address)
        seller.save()
        buyer.save()
        items = Items.objects.filter(is_invoice=False)
        invoice = Invoice(buyer_id=buyer,seller_id=seller,)
        invoice.save()
        total = 0.0
        for i in items:
            invoice.items_ids.add(i.id)
            total += i.price
            invoice.save()
        for item in items:
            item.is_invoice = True
            item.save()
        pdf = render_to_pdf('pdf_invoice.html',{'object':invoice,'total':round(total, 3)})
        return HttpResponse(pdf,content_type='application/pdf')
    objs = Items.objects.filter(is_invoice=False)
    return render(request,'invoice_gen.html',{'data':objs})