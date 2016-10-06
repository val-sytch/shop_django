#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_django.settings")
    # DJANGO_PROJ_MODE could be 'prod'-for production config or anything else for development config
    os.environ['DJANGO_PROJ_MODE'] = 'dev'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
