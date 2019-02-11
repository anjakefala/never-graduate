def get_earliest(*dates):

    earliest = None

    for date in dates:

        date = {
                    key:value
                    for key, value in zip(['m', 'd', 'y'], date.split('/'))
                }

        if earliest is None:
            earliest = date
            continue

        if (earliest['y'], earliest['m'], earliest['d']) >= (date['y'], date['m'], date['d']):
            earliest = date

    return '/'.join([earliest['m'], earliest['d'], earliest['y']])
