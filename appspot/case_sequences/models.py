from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Case_sequence(models.Model):
	case_sequence_id = models.AutoField(primary_key=True)
	case_year = models.IntegerField(verbose_name=_('Case year'), unique=False, blank=False, null=False)
	case_sequence_number = models.IntegerField(verbose_name=_('Sequence number'), unique=False, blank=False, null=False)
	case_number = models.CharField(verbose_name=_('Number'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('case_sequence')
		verbose_name_plural = _('case_sequences')