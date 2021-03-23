def write_status(SERVER_STARTED_TIMESTAMP, FILES_UPDATED_TIMESTAMP, JSON_UPDATED_TIMESTAMP):
    log = open('Log.txt', 'w')
    log.write(SERVER_STARTED_TIMESTAMP + ',' + FILES_UPDATED_TIMESTAMP + ',' + JSON_UPDATED_TIMESTAMP + "\n")
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
