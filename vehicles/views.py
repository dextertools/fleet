
# Create your views here.
from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect, Http404
#from django.urls import reverse
from django.views import generic

from .models import VehMaster
#from .models import *

class IndexView(generic.ListView):
    template_name = 'vehicles/index.html'
    context_object_name = 'registeted_veh_list'

    def get_queryset(self):
        """Return the last five registered vehicles."""
        return VehMaster.objects.order_by('-Veh_Reg_No')[:5]

def detail(request, vehmaster_Veh_Reg_No):
    vehmaster = get_object_or_404(VehMaster, Veh_Reg_No=vehmaster_Veh_Reg_No)
    return render(request, 'vehicles/detail.html', {'vehmaster': vehmaster})

def vehs_list(request):
    vehs = VehMaster.Objects.all()
    return render(request,
                  'vehicles/list.html',
                  {'vehs': vehs})

'''
def veh_detail(request, Veh_Reg_No):
vehs = get_object_or_404(VehMaster, Veh_Reg_No=vehs,
status='published',
publish__year=year,
publish__month=month,
publish__day=day)
return render(request,
'blog/post/detail.html',
{'post': post})

'vehicles/post/list.html',
def detail(request, vehmaster_Veh_Reg_No):
    vehmaster = get_object_or_404(VehMaster, Veh_Reg_No=vehmaster_Veh_Reg_No)
    return render(request, 'vehicles/detail.html', {'vehmaster': vehmaster})


def detail(request, vehmaster_id):
    vehmaster = get_object_or_404(VehMaster, id=vehmaster_Veh_Reg_No)
    return render(request, 'vehicles/detail.html', {'vehmaster': vehmaster})
'''
