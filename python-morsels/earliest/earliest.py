def get_earliest(*date_list):

    dates = [
                {
                    key:value
                    for key, value in zip(['month', 'day', 'year'], date_str.split('/'))
                }
                for date_str in date_list
            ]

    earliest = dates[0]

    for date in dates[1:]:
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
