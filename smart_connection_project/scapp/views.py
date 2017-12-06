from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from scapp.models import Posts

# Create your views here.

def index(request):
    entries1 = Posts.objects.all()[:10]
    content = {
        'first_name' : 'Juan',
        'last_name' : 'Eljach',
        'company_name' : 'Komatsu',
        'company_field' : 'Mineria',
        'country' : 'Colombia',
        'company_descr' : 'Esta empresa fabrica equipos para mineria.'
    }
    return render_to_response('index.html', {'Posts' : entries1}) #, {'Company' : entries2})


