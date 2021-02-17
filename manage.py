#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from researcher.data import retrieve_All
from researcher.write_data_final import write_All
from researcher.write_data_final import update_All
from django.core.management import execute_from_command_line
import logger
import datetime

# First Server Start-up - Log.txt must be zeroed out, Replace date integers with 0
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifesVitalSigns.settings')
    execute_from_command_line(sys.argv)

    SERVER_LAST_STARTED = logger.read_status('SERVER_STARTED_TIMESTAMP')
    SERVER_LAST_STARTED_STAMPS = (SERVER_LAST_STARTED.split('-'))[1].split('=')
    SERVER_LAST_STARTED_STAMPS[2] = SERVER_LAST_STARTED_STAMPS[1][1]
    SERVER_LAST_STARTED_STAMPS[1] = SERVER_LAST_STARTED_STAMPS[1][0]

    FILES_LAST_UPDATED = logger.read_status('FILES_UPDATED_TIMESTAMP')
    FILES_LAST_UPDATED_STAMPS = (FILES_LAST_UPDATED.split('-'))[1].split('=')
    FILES_LAST_UPDATED_STAMPS[2] = FILES_LAST_UPDATED_STAMPS[1][1]
    FILES_LAST_UPDATED_STAMPS[1] = FILES_LAST_UPDATED_STAMPS[1][0]

    JSON_LAST_UPDATED = logger.read_status('JSON_UPDATED_TIMESTAMP')
    JSON_LAST_UPDATED_STAMPS = (JSON_LAST_UPDATED.split('-'))[1].split('=')
    JSON_LAST_UPDATED_STAMPS[2] = JSON_LAST_UPDATED_STAMPS[1][1]
    JSON_LAST_UPDATED_STAMPS[1] = JSON_LAST_UPDATED_STAMPS[1][0]

    CURRENT_TIME = datetime.datetime.today()
    CURRENT_TIME = str(CURRENT_TIME.day) + '-' + str(CURRENT_TIME.month) + '=' + str(CURRENT_TIME.year)
    CURRENT_TIME_STAMPS = (CURRENT_TIME.split('-'))[1].split('=')
    CURRENT_TIME_STAMPS[2] = CURRENT_TIME_STAMPS[1][1]
    CURRENT_TIME_STAMPS[1] = CURRENT_TIME_STAMPS[1][0]

    FILES_UPDATED = False
    if CURRENT_TIME_STAMPS[2] > FILES_LAST_UPDATED_STAMPS[2]:
        try:
            retrieve_All()
            FILES_UPDATED = True
        except Exception:
            FILES_UPDATED = False
            print('Files failed to update.')
    
    if CURRENT_TIME_STAMPS[2] == FILES_LAST_UPDATED_STAMPS[2]:
        if CURRENT_TIME_STAMPS[1] > FILES_LAST_UPDATED_STAMPS[1]:
            try:
                retrieve_All()
                FILES_UPDATED = True
            except Exception:
                FILES_UPDATED = False
                print('Files failed to update.')

    if JSON_LAST_UPDATED == '0-0=0000':
        write_All()

    JSON_UPDATED = False
    if FILES_UPDATED:
        try:
            # Change and write new function update_All()
            update_All()
            JSON_UPDATED = True
        except Exception:
            JSON_UPDATED = False
            print('JSON failed to update.')

    if FILES_UPDATED:
        if JSON_UPDATED:
            logger.write_status(CURRENT_TIME, CURRENT_TIME, CURRENT_TIME)
        logger.write_status(CURRENT_TIME, CURRENT_TIME, JSON_LAST_UPDATED)
    else:
        logger.write_status(CURRENT_TIME, FILES_LAST_UPDATED, JSON_LAST_UPDATED)
    

if __name__ == '__main__':
    main()
