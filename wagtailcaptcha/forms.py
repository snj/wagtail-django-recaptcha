from __future__ import absolute_import, unicode_literals

try:
    from django_captcha.fields import ReCaptchaField  # >= 4.0
except ImportError:
    from captcha.fields import ReCaptchaField  # < 4.0
from wagtail.contrib.forms.forms import FormBuilder


class WagtailCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = "wagtailcaptcha"

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super(WagtailCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label="")

        return fields


def remove_captcha_field(form):
    if form.is_valid():
        form.fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
        form.cleaned_data.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
