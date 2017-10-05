from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Case_video(models.Model):
	case_video_id = models.AutoField(primary_key=True)
	media_id = models.IntegerField(verbose_name=_('Media ID'), unique=False, blank=False, null=False)
	update_id = models.IntegerField(verbose_name=_('Update ID'), unique=False, blank=False, null=False)
	url = models.CharField(verbose_name=_('Url'), max_length=100, blank=False, null=False)
	file_name = models.CharField(verbose_name=_('File name'), max_length=100, blank=False, null=False)
	media_pin = models.IntegerField(verbose_name=_('Media pin'), unique=False, blank=False, null=False)

	class Meta:
		verbose_name = _('case_video')
		verbose_name_plural = _('case_videos')