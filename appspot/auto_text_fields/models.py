from django.utils.translation import ugettext_lazy as _
from django.db import models
from appspot.auto_texts.models import Auto_text

# Create your models here.
class Auto_text_field(models.Model):
	auto_text_field_id = models.AutoField(primary_key=True)
	parent_auto_text_field = models.ForeignKey(Auto_text, blank=False, null=False, verbose_name=_('Auto_text'), related_name='fields')
	field_name = models.CharField(verbose_name=_('Text'), max_length=100, blank=False, null=False)

	class Meta:
		verbose_name = _('auto_text_field')
		verbose_name_plural = _('auto_text_fields')