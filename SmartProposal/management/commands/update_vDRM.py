import os
from django.core.management.base import BaseCommand
from SmartProposal.utils import update_drm_from_csv

class Command(BaseCommand):
    help = 'Update DRM data from CSV file every 20 minutes'

    def handle(self, *args, **kwargs):
        file_path = "C:test/my_file_path"
        update_drm_from_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Successfully updated DRM data'))