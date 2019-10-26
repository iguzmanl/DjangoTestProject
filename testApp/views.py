from django.shortcuts import render
# Create your views here.
from testApp.models import Visitor
from django.http import HttpResponse

import datetime


def homePageView(request):
    return render(request,'base.html')

def pageCountView(request):
	# context = {'visitors': [[1,1],[2,2]] }
	print(Visitor.objects.all())

	print("new visitor!")
	dt  = datetime.datetime.now()
	new_visitor = Visitor(visit_date=dt.date(), visit_time=dt.time())
	new_visitor.save()

	query_list = list(Visitor.objects.values_list('id', 'visit_date', 'visit_time'))


	context = {'visitors': query_list}
	return render(request, 'counts.html', context)
	# return HttpResponse('hello!')