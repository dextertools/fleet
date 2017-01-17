
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.

COLOR_CHOICES = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('grey', 'Grey'),
    ('white', 'White'),
    ('black', 'Black'),
    ('silver', 'Silver'),
    ('green', 'Green'),
)

class VehMaster(models.Model):
    Veh_Reg_No = models.CharField("Registration No", max_length=8, primary_key=True)
    Veh_Make = models.CharField("Vehicle's Make", max_length=15)
    Veh_Model = models.CharField("Vehicle's Model", max_length=15)
    Veh_Year = models.IntegerField("Year Manufactured", blank=True, null=True)
    Veh_Pur_date = models.DateField('Purchase Date', blank=True, null=True)
    Veh_Pur_price = models.IntegerField('Purchase Price', blank=True, null=True)
    Veh_Sale_date = models.DateField('Sales Date', blank=True, null=True)
    Veh_Sale_price = models.IntegerField('Sales Price', blank=True, null=True)
    Veh_Seats = models.IntegerField('No of Seats', blank=True, null=True)
    Veh_Horsepower = models.IntegerField('Power CC', blank=True, null=True)
    Veh_Colour = models.CharField('Colour',max_length=20, blank=True, null=True, choices=COLOR_CHOICES)
    Veh_Fuel_Type = models.CharField('Fuel Type', max_length=10, blank=True, null=True)
    Veh_Engine_No = models.CharField('Engine No', max_length=20, blank=True, null=True)
    Veh_Chassis_No = models.CharField('Chassis No', max_length=20, blank=True, null=True)
    Veh_Status = models.CharField('Status', max_length=10)

    def __str__(self):
        return self.Veh_Reg_No


class VehWorkOrder(models.Model):

    Work_Order_No  = models.CharField(max_length=25, primary_key=True, blank=False, null=False)
    Work_Reg_No = models.ForeignKey(VehMaster, verbose_name='Registration No', on_delete=models.CASCADE)
    Work_Type  = models.CharField("Tyep of Work", max_length=25)
    Work_Invoice_Ref  = models.CharField("Work Invoice No", max_length=25)
    Work_Odometer = models.IntegerField("Odometer Reading", blank=True, null=True)
    Work_Man_Name = models.CharField("Expert's Name", max_length=25, blank=True, null=True)
    Work_Details = models.CharField(max_length=200)
    Work_Date = models.DateField('Work Order Date', blank=True, null=True)
    Work_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Work_Remaks = models.CharField("Remarks", max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.Work_Reg_No)


class VehTyres(models.Model):

    Tyre_Reg_No = models.ForeignKey(VehMaster, verbose_name='Registration No', on_delete=models.CASCADE)
    Tyre_Tracking  = models.CharField("Tyre No", max_length=25)
    Tyre_Date  = models.DateField("Tyre Date")
    Tyre_Shop  = models.CharField("Tyre Shop", max_length=30)
    Inv_Customer_Contact = models.CharField("Contact No", max_length=15, blank=True, null=True)
    Tyre_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Tyre_OSF = models.IntegerField("OSF", blank=True, null=True)
    Tyre_NSF = models.IntegerField("NSF", blank=True, null=True)
    Tyre_OSR = models.IntegerField("OSR", blank=True, null=True)
    Tyre_NSR = models.IntegerField("NSR", blank=True, null=True)

    def __str__(self):
        return str(self.Tyre_Reg_No)

#----------------- MOEL FORMS ---------------
    
class VehMasterForm(ModelForm):
    class Meta:
        model = VehMaster
        fields = ['Veh_Reg_No', 'Veh_Make', 'Veh_Model', 'Veh_Pur_date', 'Veh_Pur_price']

