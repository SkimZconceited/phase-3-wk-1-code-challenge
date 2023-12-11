def convert_to_24_hrs(hh = 0, mm = 0, time = ''):
    if (hh >= 1 and hh <= 12) and (mm >= 00 and mm <=59) and (time == 'am' or time == 'pm'):
        if time == 'am':
            if hh <= 9:
                time = 'hrs'
                print(f'0{hh}{mm}{time} 1')
            else:
                time = 'hrs'
                print(f'{hh}{mm}{time} 2')
        else:
            hh += 12
            mm += 00
            time = 'hrs'
            print(f'{hh}{mm}{time} 3')
        pass
    else:
        print('enter valid time')
    pass

# convert_to_24_hrs(1, 36, 'am')
# convert_to_24_hrs(6, 36, 'am')
# convert_to_24_hrs(12, 36, 'am')
# convert_to_24_hrs(1, 36, 'pm')
# convert_to_24_hrs(6, 36, 'pm')
# convert_to_24_hrs(12, 36, 'pm')
