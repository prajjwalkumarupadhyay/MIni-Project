import re              
while True:
   password=re.compile(r'\d+\w*{8,}',re.I)
   output=password.search(input('Create your password \n'))
   if output is None:
      print('Please create a strong Password')
   else:
      print('Password Created! Your password is:',output.group())
      