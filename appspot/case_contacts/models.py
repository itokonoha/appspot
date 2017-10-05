from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case
from appspot.person.models import Person

# Create your models here.
class Case_contact(models.Model):
	case_contact_id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='case_contacts')
	client = models.ForeignKey(Person, blank=False, null=False, verbose_name=_('Person'), related_name='case_contacts')

	class Meta:
		verbose_name = _('case_contact')
		verbose_name_plural = _('case_contacts')