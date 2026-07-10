import os
import shutil
import stat
import time
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

FRONTEND_DIR = Path(settings.BASE_DIR).parent / "frontend"


def _force_writable(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass


def sync_dir(src: Path, dst: Path, stdout=None):
    """One-way sync src -> dst: copy/overwrite files from src, remove files in dst
    that no longer exist in src. Tolerant of transient Windows/OneDrive file locks
    (retries briefly, skips a stubborn file instead of failing the whole command)."""
    dst.mkdir(parents=True, exist_ok=True)
    src_names = {f.name for f in src.iterdir()} if src.exists() else set()

    for existing in list(dst.iterdir()):
        if existing.name in src_names:
            continue
        try:
            if existing.is_dir():
                shutil.rmtree(existing, onerror=_force_writable)
            else:
                os.chmod(existing, stat.S_IWRITE)
                existing.unlink()
        except PermissionError as e:
            if stdout:
                stdout.write(f"  (couldn't remove stale {existing.name}, still locked: {e})")

    if not src.exists():
        return

    for f in src.iterdir():
        if not f.is_file():
            continue
        for attempt in range(3):
            try:
                shutil.copy2(f, dst / f.name)
                break
            except PermissionError as e:
                if attempt == 2 and stdout:
                    stdout.write(f"  (couldn't copy {f.name}, still locked: {e})")
                else:
                    time.sleep(0.5)


class Command(BaseCommand):
    help = (
        "One-shot publish: exports content.json and copies any uploaded media "
        "(project images, profile photo, CVs, recommendation letters) into the "
        "frontend's public/ folder."
    )

    def handle(self, *args, **options):
        call_command("export_content")

        media_root = Path(settings.MEDIA_ROOT)

        sync_dir(media_root / "cv", FRONTEND_DIR / "public" / "cv", self.stdout)

        for sub in ["projects", "profile", "recommendations"]:
            sync_dir(media_root / sub, FRONTEND_DIR / "public" / "media" / sub, self.stdout)

        self.stdout.write(self.style.SUCCESS("Frontend content and media are up to date."))
