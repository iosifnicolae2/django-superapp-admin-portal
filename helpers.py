from typing import Optional

from django.contrib.admin import helpers
from django.contrib.admin.utils import lookup_field
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ForeignKey
from django.forms import ModelChoiceField
from django.http import HttpRequest
from unfold.admin import UnfoldAdminReadonlyField

# Keep exporting these classes for backwards compatibility
from .admin import SuperAppModelAdmin
from .db_fields import ChainedForeignKey
from .models import SuperAppBaseModel as BaseModel
from .widgets import ChainedAdminSelect

__all__ = ['SuperAppModelAdmin', 'BaseModel']


class SuperAppAdminReadonlyField(UnfoldAdminReadonlyField):
    def is_custom_html_field(self) -> bool:
        field, obj, model_admin = (
            self.field["field"],
            self.form.instance,
            self.model_admin,
        )

        try:
            f, attr, config = lookup_field(field, obj, model_admin)
        except (AttributeError, ValueError, ObjectDoesNotExist):
            return False

        return hasattr(attr, 'custom_html_field') and attr.custom_html_field == True


helpers.AdminReadonlyField = SuperAppAdminReadonlyField


class ChainedForeignKeyAdmin:
    def formfield_for_foreignkey(
            self, db_field: ForeignKey, request: HttpRequest, **kwargs
    ) -> Optional[ModelChoiceField]:
        db = kwargs.get("using")

        if isinstance(db_field, ChainedForeignKey):
            kwargs["widget"] = ChainedAdminSelect(
                db_field, self.admin_site, using=db
            )
            pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
