from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case
from localflavor.us.models import USZipCodeField

# Create your models here.
class Assignment(models.Model):
	assignment_id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative_case'), related_name='assignment')
	assignment_date = models.DateField(help_text=_(''))
	#begin_time = 
	#end_time = 
	start_address = USZipCodeField(max_length=9, help_text=_(''), blank=False, null=False)
	investigator_id = models.IntegerField(verbose_name=_('Investigator ID'), unique=False, blank=False, null=False)
	record_owner = models.CharField(verbose_name=_('Record owner'), max_length=100, blank=False, null=False)
	record_creation_date = models.DateField(help_text=_(''))

	class Meta:
		verbose_name = _('assignment')
		verbose_name_plural = _('assignments')
