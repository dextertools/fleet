
from django.contrib import admin

# Register your models here.
from .models import VehMaster, VehWorkOrder, VehTyres
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

#-------------------------------------------------------------------

class VehTyresAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    }
    list_display = ('Tyre_Reg_No', 'Tyre_Price', 'Tyre_Date')
    fieldsets = [
        (None,                  {'fields': ['Tyre_Reg_No', ('Tyre_Price','Tyre_Date'), ('Tyre_Shop', 'Tyre_Tracking') ]}),
        ('Tyres Replaced',      {'fields': [('Tyre_OSF', 'Tyre_NSF', 'Tyre_OSR', 'Tyre_NSR') ]}),

        ]

'''
class VehTyresInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'23'})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':25})},
    }    
    model = VehTyres
    extra = 1

class VehMasterTyres(admin.ModelAdmin):
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
    inlines = [VehTyresInline]    
'''

admin.site.register(VehMaster, VehMasterAdmin)
admin.site.register(VehTyres, VehTyresAdmin)
#admin.site.register(VehMaster, VehMasterTyres)
