def create_phone_number(n):
    if max(n) > 9:
        return ''

    phone_format = ['(', '', ') ', '', '-', '']

    phone_format[1] = ''.join(n[:-7].split())
    #phone_format[3] = ''.join(str(n[3:-4]))
    #phone_format[5] = ''.join(str(n[-4:]))

    return ''.join(phone_format)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))