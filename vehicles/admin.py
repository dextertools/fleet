
from django.contrib import admin

# Register your models here.
from .models import VehMaster, VehWorkOrder
from django.forms import TextInput, Textarea, ModelForm
from django.forms.models import inlineformset_factory
from django.db import models

class VehWorkOrderInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'23'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':25})},
    }    
    model = VehWorkOrder
    extra = 1

class VehMasterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20', 'padding-left':'10px'})},
    }
    
    list_display = ('Veh_Reg_No', 'Veh_Make', 'Veh_Model', 'Veh_Year', 'Veh_Status',
                    'Veh_Seats', 'Veh_Horsepower',
                    'Veh_Fuel_Type', 'Veh_Pur_date', 'Veh_Pur_price',
                    )
    fields = [('Veh_Reg_No', 'Veh_Make', 'Veh_Model', 'Veh_Status', 'Veh_Year'),
              ('Veh_Engine_No', 'Veh_Chassis_No', 'Veh_Seats', 'Veh_Fuel_Type',
               'Veh_Horsepower', 'Veh_Colour'),
              ('Veh_Sale_price', 'Veh_Pur_price', 'Veh_Sale_date', 'Veh_Pur_date')
              ]
    inlines = [VehWorkOrderInline]


admin.site.register(VehMaster, VehMasterAdmin)
