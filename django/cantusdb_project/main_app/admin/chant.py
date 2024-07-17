from django.contrib import admin

from main_app.admin.base_admin import EXCLUDE, READ_ONLY, BaseModelAdmin
from main_app.forms import AdminChantForm
from main_app.models import Chant


@admin.register(Chant)
class ChantAdmin(BaseModelAdmin):

    @admin.display(description="Source Siglum")
    def get_source_siglum(self, obj):
        if obj.source:
            return obj.source.siglum

    list_display = (
        "incipit",
        "get_source_siglum",
        "genre",
    )
    search_fields = (
        "title",
        "incipit",
        "cantus_id",
        "id",
    )

    readonly_fields = READ_ONLY + ("incipit",)

    list_filter = (
        "genre",
        "office",
    )
    exclude = EXCLUDE + (
        "col1",
        "col2",
        "col3",
        "next_chant",
        "s_sequence",
        "is_last_chant_in_feast",
        "visible_status",
        "date",
        "volpiano_notes",
        "volpiano_intervals",
        "title",
        "differentiae_database",
    )
    form = AdminChantForm
    raw_id_fields = (
        "source",
        "feast",
    )
    ordering = ("source__siglum",)