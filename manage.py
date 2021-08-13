#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management import execute_from_command_line
import logger

# First Server Start-up - Log.txt must be zeroed out, Replace date integers with 0 "00-00=0000"
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifesVitalSigns.settings')
    execute_from_command_line(sys.argv)

    logger.write_status('00-00=0000', '00-00=0000', '00-00=0000')
    logger.run()    


if __name__ == '__main__':
    main()