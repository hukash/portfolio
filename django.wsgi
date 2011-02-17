import os
import sys

path_workspace = ''
path_project = ''
sys.path.append(path_workspace)
sys.path.append(path_project)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

