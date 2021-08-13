from researcher.data import retrieve_All
from researcher.write_data_final import write_All
from researcher.write_data_final import update_All
import datetime

def write_status(SERVER_STARTED_TIMESTAMP, FILES_UPDATED_TIMESTAMP, JSON_UPDATED_TIMESTAMP):
    log = open('Log.txt', 'w')
    log.write(SERVER_STARTED_TIMESTAMP + ',' + FILES_UPDATED_TIMESTAMP + ',' + JSON_UPDATED_TIMESTAMP)
    log.close()


def read_status(TYPE_TIMESTAMP):
    log = open('Log.txt', 'r')
    STAMPS = log.read().split(',')
    log.close()
    if TYPE_TIMESTAMP == 'SERVER_STARTED_TIMESTAMP':
        return STAMPS[0]
    if TYPE_TIMESTAMP == 'FILES_UPDATED_TIMESTAMP':
        return STAMPS[1]
    if TYPE_TIMESTAMP == 'JSON_UPDATED_TIMESTAMP':
        return STAMPS[2]
    return 'Error No Log Status Found'

def run():
    SERVER_LAST_STARTED = read_status('SERVER_STARTED_TIMESTAMP')
    SERVER_LAST_STARTED_STAMPS = SERVER_LAST_STARTED.split('-')
    SERVER_LAST_STARTED_STAMPS2 = SERVER_LAST_STARTED_STAMPS[1].split('=')
    SERVER_LAST_STARTED_STAMPS[1] = SERVER_LAST_STARTED_STAMPS2[0]
    SERVER_LAST_STARTED_STAMPS.append(SERVER_LAST_STARTED_STAMPS2[1])

    FILES_LAST_UPDATED = read_status('FILES_UPDATED_TIMESTAMP')
    FILES_LAST_UPDATED_STAMPS = FILES_LAST_UPDATED.split('-')
    FILES_LAST_UPDATED_STAMPS2 = FILES_LAST_UPDATED_STAMPS[1].split('=')
    FILES_LAST_UPDATED_STAMPS[1] = FILES_LAST_UPDATED_STAMPS2[0]
    FILES_LAST_UPDATED_STAMPS.append(FILES_LAST_UPDATED_STAMPS2[1])

    JSON_LAST_UPDATED = read_status('JSON_UPDATED_TIMESTAMP')
    JSON_LAST_UPDATED_STAMPS = JSON_LAST_UPDATED.split('-')
    JSON_LAST_UPDATED_STAMPS2 = JSON_LAST_UPDATED_STAMPS[1].split('=')
    JSON_LAST_UPDATED_STAMPS[1] = JSON_LAST_UPDATED_STAMPS2[0]
    JSON_LAST_UPDATED_STAMPS.append(JSON_LAST_UPDATED_STAMPS2[1])

    CURRENT_TIME = datetime.datetime.today()
    CURRENT_TIME = str(CURRENT_TIME.day) + '-' + str(CURRENT_TIME.month) + '=' + str(CURRENT_TIME.year)
    CURRENT_TIME_STAMPS = CURRENT_TIME.split('-')
    CURRENT_TIME_STAMPS2 = CURRENT_TIME_STAMPS[1].split('=')
    CURRENT_TIME_STAMPS[1] = CURRENT_TIME_STAMPS2[0]
    CURRENT_TIME_STAMPS.append(CURRENT_TIME_STAMPS2[1])

    TIME_STRINGS = [SERVER_LAST_STARTED, FILES_LAST_UPDATED, JSON_LAST_UPDATED, CURRENT_TIME]
    TIME_STAMPS = [SERVER_LAST_STARTED_STAMPS, FILES_LAST_UPDATED_STAMPS, JSON_LAST_UPDATED_STAMPS, CURRENT_TIME_STAMPS]
    
    update(TIME_STRINGS, TIME_STAMPS)


def update(TIME_STRINGS, TIME_STAMPS):
    FILES_UPDATED = False
    if (int(TIME_STAMPS[3][2]) > int(TIME_STAMPS[1][2])) or (TIME_STRINGS[1] == '00-00=0000'):
        try:
            retrieve_All()
            FILES_UPDATED = True
            print('Files updated')
        except Exception:
            FILES_UPDATED = False
            print('Files failed to update')
    
    if int(TIME_STAMPS[3][2]) == int(TIME_STAMPS[1][2]):
        if int(TIME_STAMPS[3][1]) > int(TIME_STAMPS[1][1]):
            try:
                retrieve_All()
                FILES_UPDATED = True
                print('Files updated')
            except Exception:
                FILES_UPDATED = False
                print('Files failed to update')

    JSON_UPDATED = False
    if TIME_STRINGS[2] == '00-00=0000':
        try:
            write_All()
            JSON_UPDATED = True
            print('JSON written')
        except Exception:
            print('JSON failed to write')

    if FILES_UPDATED:
        if not(JSON_UPDATED):
            try:
                update_All()
                JSON_UPDATED = True
                print('JSON updated')
            except Exception:
                print('JSON failed to update')

    if FILES_UPDATED:
        if JSON_UPDATED:
            write_status(TIME_STRINGS[3], TIME_STRINGS[3], TIME_STRINGS[3])
        write_status(TIME_STRINGS[3], TIME_STRINGS[3], TIME_STRINGS[2])
    else:
        write_status(TIME_STRINGS[3], TIME_STRINGS[1], TIME_STRINGS[2])
