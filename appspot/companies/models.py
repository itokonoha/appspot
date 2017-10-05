from django.utils.translation import ugettext_lazy as _
from django.db import models
from localflavor.us.models import USZipCodeField

# Create your models here.
class Company(models.Model):
	company_id = models.AutoField(primary_key=True)
	company_name = models.CharField(verbose_name=_('Prefix'), max_length=100, blank=False)
	company_address = USZipCodeField(max_length=9, help_text=_(''), blank=False, null=False)
	
	class Meta:
		verbose_name = _('company')
		verbose_name_plural = _('companies')