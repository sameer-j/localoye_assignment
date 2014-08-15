from django.template import RequestContext
from django.shortcuts import render_to_response
from localoye.models import Venue,Hall

def index(request):
    context = RequestContext(request)
    details_list = Hall.objects.select_related()
    context_dict = {'details': details_list }
    return render_to_response('localoye/index.html', context_dict, context)