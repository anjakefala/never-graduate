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

        for key in ['year', 'month', 'day']:
            if int(date[key]) < int(earliest[key]):
                earliest = date
                break
            elif int(date[key]) > int(earliest[key]):
                break
            else:
                continue


    return '/'.join([earliest['month'], earliest['day'], earliest['year']])
