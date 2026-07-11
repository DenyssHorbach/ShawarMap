from django.contrib import admin
from .models import Point, Review, PointImages

# Register your models here.

class PointImageLine(admin.TabularInline):
    model = PointImages
    extra = 3
    fields = ['images', 'uploaded_at',]
    readonly_fields = ['uploaded_at',]

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "address",
        "phone_number",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["name", "id"]
    list_filter = ["is_active", "created_at", "updated_at"]
    list_editable = ["address", "phone_number", "is_active"]
    inlines = [PointImageLine]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'point', 'user', 'display_starts', 'created_at',]
    list_filter = ('rating', 'created_at',)
    search_fields = ('point__name', 'user__name',)

    @admin.display(description='Rating')
    def display_starts(self, obj):
        stars = "★" * obj.rating
        empty_stars = "☆" * (5 - obj.rating)
        return f"{stars}{empty_stars}"



