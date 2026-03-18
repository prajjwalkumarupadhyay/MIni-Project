import string
print('Caesar Cipher by Prajjwal Kumar Upadhyay')
def choose():
    def shift():
        while True:
            try:
                shift=int(input('Please enter the key (o to 25) to use.\n'))
                if 0<=shift<=25:
                    return shift
                else:
                    print('The value should be b/w (0-25).')
            except ValueError:
                print('Error:Input must be an integer.')
    def encrypt():
        Alpha=list(string.ascii_uppercase)
        msg=input('Enter the message you want to encrypt.\n')
        new=msg.upper().split()
        old=''.join(new)
        if old.isaplha() is False:
            print('Error: The message should only contains alphabets.Please enter message in alphabets.')
            encrypt()
        for i in new:
            for j in i:
                pass
    while True:
        option=input('Do you want to (e)ncrypt or (d)ecrypt ?\n')
        if option.lower()=='e':
            move=shift()
        elif option.lower()=='d':
            pass
        else:
            print('Please enter the right input.')
            continue
choose()
        