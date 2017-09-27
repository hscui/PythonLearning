# verify username and pin

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843'],
    ['崔', '1234']
]
username = input('User name:')
pin = input('PIN code:')

if [username, pin] in database:
    print('Access Granted')
else:
    print('Access Denied')
