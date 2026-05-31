"""
ASGI config for e_waste_recycling project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps', 'authentication'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps', 'core'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps', 'rewards'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps', 'setup_data'))

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_waste_recycling.settings')

application = get_asgi_application()
