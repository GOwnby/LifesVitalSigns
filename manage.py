#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from researcher.write_data_final import write_All
from researcher.data import retrieve_All
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifesVitalSigns.settings')
    execute_from_command_line(sys.argv)

    retrieve_All()
    write_All()

if __name__ == '__main__':
    main()
