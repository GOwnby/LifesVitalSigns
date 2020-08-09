#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from researcher.write_data_final import write_CO2
from researcher.write_data_final import write_NO2
from researcher.write_data_final import write_CH4
from researcher.write_data_final import write_CFC11
from researcher.write_data_final import write_CFC12
from researcher.write_data_final import write_Temperature

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifesVitalSigns.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    write_CO2()
    write_NO2()
    write_CH4()
    write_CFC11()
    write_CFC12()
    write_Temperature()


if __name__ == '__main__':
    main()
