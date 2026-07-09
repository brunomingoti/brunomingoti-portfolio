import shutil
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

FRONTEND_DIR = Path(settings.BASE_DIR).parent / "frontend"


class Command(BaseCommand):
    help = (
        "One-shot publish: exports content.json and copies any uploaded media "
        "(project images, profile photo, CVs) into the frontend's public/ folder."
    )

    def handle(self, *args, **options):
        call_command("export_content")

        media_root = Path(settings.MEDIA_ROOT)

        cv_src = media_root / "cv"
        if cv_src.exists():
            cv_dst = FRONTEND_DIR / "public" / "cv"
            cv_dst.mkdir(parents=True, exist_ok=True)
            for f in cv_src.iterdir():
                shutil.copy2(f, cv_dst / f.name)

        for sub in ["projects", "profile"]:
            src = media_root / sub
            if not src.exists():
                continue
            dst = FRONTEND_DIR / "public" / "media" / sub
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

        self.stdout.write(self.style.SUCCESS("Frontend content and media are up to date."))
