#!/usr/bin/env python
import os
import sys

try:
    import project.local_config
except ImportError:
    sys.stderr.write("Error: Can not import file  'local_config.py' ")
    sys.exit(1)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
