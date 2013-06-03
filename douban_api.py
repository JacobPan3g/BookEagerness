from douban_client import DoubanClient

KEY = '0defea680ef7603929cfbf382ce620ab'
SECRET = 'ebb2926e5d8d14ab'
CALLBACK = 'http://myapp.com/callback'

SCOPE = ''
client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

print client.authorize_url
code = raw_input('Enter the verification code:')

client.auth_with_code(code)
print client.user.me
