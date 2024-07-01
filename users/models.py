from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from services.custom_exceptions import InvalidRequest


class CustomUser(AbstractUser):
    is_using_prepaid = models.BooleanField(
        verbose_name=_("Is Using Prepaid"),
        blank=False,
        null=True,
        default=False,
        help_text=_(
            "denotes whether this user is using prepaid balance or payment gateway to pay utility bill"
        ),
        error_messages={
            'blank': _("is_using_prepaid value must be provided")
        }
    )

    def activate_account(self):
        if self.is_active:
            raise InvalidRequest(
                detail=_('this user is already active')
            )
        self.is_active = True
        self.save()

    def deactivate_account(self):
        if self.is_active is False:
            raise InvalidRequest(
                detail=_('this user is already deactivated')
            )
        self.is_active = False
        self.save()

    def set_is_using_prepaid_true(self):
        if self.is_using_prepaid:
            raise InvalidRequest(
                detail=_('this user is already using prepaid')
            )
        self.is_using_prepaid = True
        self.save()

    def set_is_using_prepaid_false(self):
        if self.is_using_prepaid is False:
            raise InvalidRequest(
                detail=_('this user is not using prepaid')
            )
        self.is_using_prepaid = False
        self.save()
