from django.db import models


class Profile(models.Model):
    """Singleton holding the hero/about content and contact links."""

    name = models.CharField(max_length=120, default="Bruno Mingoti")
    headline_pt = models.CharField(max_length=200)
    headline_en = models.CharField(max_length=200)
    bio_pt = models.TextField()
    bio_en = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    scholar_url = models.URLField(blank=True)
    photo = models.ImageField(upload_to="profile/", blank=True)
    cv_pt_file = models.FileField(upload_to="cv/", blank=True)
    cv_en_file = models.FileField(upload_to="cv/", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class Institution(models.Model):
    """Filter tag for the projects gallery: WZL, CERTI, UFSC, Invest Jr., etc."""

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    slug = models.SlugField(unique=True)
    title_pt = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    summary_pt = models.CharField(max_length=280, help_text="Short teaser shown on the gallery card")
    summary_en = models.CharField(max_length=280)
    body_pt = models.TextField(help_text="Full case study, markdown supported")
    body_en = models.TextField()
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT, related_name="projects")
    role_pt = models.CharField(max_length=200, blank=True)
    role_en = models.CharField(max_length=200, blank=True)
    period_start = models.CharField(max_length=20, blank=True, help_text="e.g. 2024-08")
    period_end = models.CharField(max_length=20, blank=True, help_text="e.g. 2025-12 or 'presente'")
    tools = models.CharField(max_length=300, blank=True, help_text="Comma-separated: Python, OpenCV, ...")
    icon = models.CharField(max_length=60, default="ti-code", help_text="Tabler icon name, e.g. ti-cpu")
    cover_image = models.ImageField(upload_to="projects/", blank=True)
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-period_start"]

    def __str__(self):
        return self.title_pt


class ProjectImage(models.Model):
    """Extra before/after or gallery images for a case study."""

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/gallery/")
    caption_pt = models.CharField(max_length=200, blank=True)
    caption_en = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.slug} #{self.pk}"


class Publication(models.Model):
    TYPE_CHOICES = [
        ("paper", "Paper / conference"),
        ("thesis", "Thesis / TCC"),
        ("report", "Technical report"),
    ]

    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300, blank=True)
    venue = models.CharField(max_length=200, help_text="e.g. SIBGRAPI 2025")
    year = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="paper")
    url = models.URLField(blank=True, help_text="Zenodo / DOI / repository link")
    summary_pt = models.TextField(blank=True)
    summary_en = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-year"]

    def __str__(self):
        return self.title


class ExperienceEntry(models.Model):
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=120, blank=True)
    role_pt = models.CharField(max_length=200)
    role_en = models.CharField(max_length=200)
    period_start = models.CharField(max_length=20)
    period_end = models.CharField(max_length=20, help_text="e.g. 'presente' / 'present'")
    context_pt = models.CharField(max_length=300, blank=True)
    context_en = models.CharField(max_length=300, blank=True)
    highlights_pt = models.JSONField(default=list, help_text="List of bullet strings")
    highlights_en = models.JSONField(default=list)
    tools = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Experience entries"

    def __str__(self):
        return f"{self.organization} ({self.period_start} - {self.period_end})"


class EducationEntry(models.Model):
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=120, blank=True)
    degree_pt = models.CharField(max_length=200)
    degree_en = models.CharField(max_length=200)
    period_start = models.CharField(max_length=20)
    period_end = models.CharField(max_length=20)
    details_pt = models.JSONField(default=list)
    details_en = models.JSONField(default=list)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Education entries"

    def __str__(self):
        return f"{self.institution} ({self.period_start} - {self.period_end})"
