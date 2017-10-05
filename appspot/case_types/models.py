from django.utils.translation import ugettext_lazy as _
from django.db import models

class Case_type(models.Model):
	case_type_id = models.AutoField(primary_key=True)
	case_type = models.CharField(verbose_name=_('Case status'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('case_type')
		verbose_name_plural = _('case_types')