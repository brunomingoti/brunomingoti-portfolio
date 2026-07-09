import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from content.models import (
    EducationEntry,
    ExperienceEntry,
    Institution,
    Profile,
    Project,
    Publication,
)

DEFAULT_OUTPUT = Path(settings.BASE_DIR).parent / "frontend" / "src" / "data"


def bilingual(obj, field):
    return {"pt": getattr(obj, f"{field}_pt"), "en": getattr(obj, f"{field}_en")}


def tool_list(raw):
    return [t.strip() for t in raw.split(",") if t.strip()]


class Command(BaseCommand):
    help = "Exports all content as JSON consumed by the static frontend."

    def add_arguments(self, parser):
        parser.add_argument("--out", default=str(DEFAULT_OUTPUT))

    def handle(self, *args, **options):
        out_dir = Path(options["out"])
        out_dir.mkdir(parents=True, exist_ok=True)

        profile = Profile.objects.first()
        profile_data = None
        if profile:
            profile_data = {
                "name": profile.name,
                "headline": bilingual(profile, "headline"),
                "bio": bilingual(profile, "bio"),
                "email": profile.email,
                "phone": profile.phone,
                "linkedinUrl": profile.linkedin_url,
                "githubUrl": profile.github_url,
                "scholarUrl": profile.scholar_url,
                "photoUrl": profile.photo.name and f"/media/{profile.photo.name}",
                "cvPtUrl": profile.cv_pt_file.name and f"/cv/{Path(profile.cv_pt_file.name).name}",
                "cvEnUrl": profile.cv_en_file.name and f"/cv/{Path(profile.cv_en_file.name).name}",
            }

        institutions = [
            {"slug": i.slug, "name": i.name}
            for i in Institution.objects.all()
        ]

        projects = []
        for p in Project.objects.select_related("institution").prefetch_related("images"):
            projects.append(
                {
                    "slug": p.slug,
                    "title": bilingual(p, "title"),
                    "summary": bilingual(p, "summary"),
                    "body": bilingual(p, "body"),
                    "institution": p.institution.slug,
                    "role": bilingual(p, "role"),
                    "periodStart": p.period_start,
                    "periodEnd": p.period_end,
                    "tools": tool_list(p.tools),
                    "icon": p.icon,
                    "coverImage": p.cover_image.name and f"/media/{p.cover_image.name}",
                    "repoUrl": p.repo_url,
                    "demoUrl": p.demo_url,
                    "featured": p.featured,
                    "images": [
                        {
                            "src": f"/media/{img.image.name}",
                            "caption": {"pt": img.caption_pt, "en": img.caption_en},
                        }
                        for img in p.images.all()
                    ],
                }
            )

        publications = [
            {
                "title": pub.title,
                "authors": pub.authors,
                "venue": pub.venue,
                "year": pub.year,
                "type": pub.type,
                "url": pub.url,
                "summary": bilingual(pub, "summary"),
            }
            for pub in Publication.objects.all()
        ]

        experience = [
            {
                "organization": e.organization,
                "location": e.location,
                "role": bilingual(e, "role"),
                "periodStart": e.period_start,
                "periodEnd": e.period_end,
                "context": bilingual(e, "context"),
                "highlights": {"pt": e.highlights_pt, "en": e.highlights_en},
                "tools": tool_list(e.tools),
                "recommendationLetterUrl": e.recommendation_letter.name
                and f"/media/{e.recommendation_letter.name}",
            }
            for e in ExperienceEntry.objects.all()
        ]

        education = [
            {
                "institution": ed.institution,
                "location": ed.location,
                "degree": bilingual(ed, "degree"),
                "periodStart": ed.period_start,
                "periodEnd": ed.period_end,
                "details": {"pt": ed.details_pt, "en": ed.details_en},
            }
            for ed in EducationEntry.objects.all()
        ]

        payload = {
            "profile": profile_data,
            "institutions": institutions,
            "projects": projects,
            "publications": publications,
            "experience": experience,
            "education": education,
        }

        out_file = out_dir / "content.json"
        out_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Exported content to {out_file}"))
