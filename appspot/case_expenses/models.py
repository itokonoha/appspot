from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.investigative_cases.models import Investigative_case
from appspot.users.models import User

# Create your models here.
class Case_expense(models.Model):
	case_expense_id = models.AutoField(primary_key=True)
	investigative_case = models.ForeignKey(Investigative_case, blank=False, null=False, verbose_name=_('Investigative case'), related_name='expenses')
	#investigator_id = models.IntegerField(verbose_name=_('Investigator ID'), unique=False, blank=False, null=False)
	expense_date = models.DateField(help_text=_(''), blank=False, null=False)
	description = models.CharField(verbose_name=_('Description'), max_length=100, blank=False, null=False)
	amount = models.FloatField(verbose_name=_('Amount'), unique=False, blank=False, null=False)
	total = models.FloatField(verbose_name=_('Total'), unique=False, blank=False, null=False)
	investigator = models.ForeignKey(User, blank=False, null=False, verbose_name=_('User'), related_name='expenses')

	class Meta:
		verbose_name = _('case_expense')
		verbose_name_plural = _('case_expenses')