from django.utils.translation import ugettext_lazy as _
from django.db import models

STATUS = (
	('NEW', _('New')),
	('OPEN', _('Open')),
	('PENDING_REPORT', _('Pending Report')),
	('REPORT_COMPLETE', _('Report Complete')),
	('CLOSED', _('Closed')),
	('PENDING', _('Pending')),
	('INVOICED', _('Invoiced')),
	('RUSH_JOB', _('Rush Job')),
)

class Case_status(models.Model):
	case_status_id = models.AutoField(primary_key=True)
	case_status = models.CharField(verbose_name=_('Case status'), max_length=100, blank=False, null=False, choices=STATUS)

	class Meta:
		verbose_name = _('case_status')
		verbose_name_plural = _('case_status')