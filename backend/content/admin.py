from django.contrib import admin

from .models import (
    EducationEntry,
    ExperienceEntry,
    Institution,
    Profile,
    Project,
    ProjectImage,
    Publication,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Profile.objects.exists()


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title_pt", "institution", "featured", "order")
    list_filter = ("institution", "featured")
    prepopulated_fields = {"slug": ("title_en",)}
    inlines = [ProjectImageInline]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "venue", "year", "type", "order")
    list_filter = ("type",)


@admin.register(ExperienceEntry)
class ExperienceEntryAdmin(admin.ModelAdmin):
    list_display = ("organization", "role_pt", "period_start", "period_end", "order")


@admin.register(EducationEntry)
class EducationEntryAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree_pt", "period_start", "period_end", "order")
