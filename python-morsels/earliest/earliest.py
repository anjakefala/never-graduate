def get_earliest(*dates):

    earliest = None

    for date in dates:
        date = {
                    key:value
                    for key, value in zip(['month', 'day', 'year'], date.split('/'))
                }
        if earliest is None:
            earliest = date
            continue

        if int(date['year']) < int(earliest['year']):
            earliest = date
            continue
        elif int(date['year']) > int(earliest['year']):
            continue
        else:
            if int(date['month']) < int(earliest['month']):
                earliest = date
                continue
            elif int(date['month']) > int(earliest['month']):
                continue
            else:
                if int(date['day']) < int(earliest['day']):
                    earliest = date
                    continue
                else:
                    continue


    return '/'.join([earliest['month'], earliest['day'], earliest['year']])
