def convert_to_24_hrs(hh = 0, mm = 0, time = ''):
    if (hh >= 1 and hh <= 12) and (mm >= 00 and mm <=59) and (time == 'am' or time == 'pm'):
        time = 'hrs'
        if time == 'am':
            print(f'{hh}{mm}{time}')
        else:
            hh += 12
            mm += 00
            print(f'{hh}{mm}{time}')
        pass
    else:
        print('failed')
    pass

convert_to_24_hrs(11, 36, 'am')
convert_to_24_hrs(11, 36, 'pm')
convert_to_24_hrs(11, 36, 'to')
convert_to_24_hrs(13, 36, 'am')
convert_to_24_hrs(11, 70, 'am')
convert_to_24_hrs(12, 60, 'am')