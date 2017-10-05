from django.utils.translation import ugettext_lazy as _
from django.db import models

class Auto_text(models.Model):
	auto_text_id = models.AutoField(primary_key=True)
	label = models.CharField(verbose_name=_('Label'), max_length=100, blank=False, null=False)
	atext = models.CharField(verbose_name=_('Text'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('auto_text')
		verbose_name_plural = _('auto_texts')