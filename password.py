import re              
while True:
   password=re.compile(r'^(?=.*[0-9]).+$')
   output=password.fullmatch(input('Create your password \n'))
   if output is None:
      print('Please create a strong Password')
   else:
      print('Password Created! Your password is:',output.group())