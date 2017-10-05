from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.vehicles.models import Vehicle

# Create your models here.
class Case_equipment(models.Model):
	case_equipment_id = models.AutoField(primary_key=True)
	serial_number = models.CharField(verbose_name=_('Serial number'), max_length=100, blank=False, null=False)
	email_address = models.EmailField(verbose_name=_('Email address'), max_length=254, unique=True)
	password = models.CharField(verbose_name=_('Password'), max_length=100, blank=False, null=False)
	service_status = models.CharField(verbose_name=_('Service status'), max_length=100, blank=False, null=False)
	date_purchased = models.DateField(help_text=_(''), blank=False, null=False)
	price = models.FloatField(help_text=_(''), blank=False, null=False)
	comments = models.CharField(verbose_name=_('Comments'), max_length=100, blank=False, null=False)
	equipment_type = models.CharField(verbose_name=_('Equipment type'), max_length=100, blank=False, null=False)
	vehicle = models.ForeignKey(Vehicle, blank=False, null=False, verbose_name=_('Vehicle'), related_name='case_equipment')

	class Meta:
		verbose_name = _('case_equipment')
		verbose_name_plural = _('case_equipments')