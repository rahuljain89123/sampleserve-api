
from wtforms_alchemy import ModelForm
from wtforms.validators import Email, regexp
from sampleserve.models import (
    Site,
    SiteData,
    Client,
    Upload,
    Schedule,
    ScheduleWellTests,
    Contact,
)


class SiteDataForm(ModelForm):
    class Meta:
        model = SiteData
