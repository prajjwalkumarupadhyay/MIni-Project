import string
print('Caesar Cipher by Prajjwal Kumar Upadhyay')
def choose():
    def shift():
        while True:
            try:
                shift=int(input('Please enter the key (1 to 25) to use.\n'))
                if (1<=shift<=25):
                    return shift
                else:
                    print('The value should be b/w (1-25).')
            except ValueError: 
                print('Error:Input must be an integer.')
    def encrypt():
        def Re_Evaluate1():
            return index-25
        Alpha=list(string.ascii_uppercase)
        msg=input('Enter the message you want to encrypt.\n')
        new=msg.upper().split()
        old=''.join(new)
        if old.isalpha() is False:
            print('Error: The message should only contains alphabets.Please enter message in alphabets.')
            encrypt()
        store=[]
        for i in new:
            new=[]
            for j in i:
                index=Alpha.index(j)
                index+=move
                if (index>25):
                    index=Re_Evaluate1()
                new.append(Alpha[index])
            word=''.join(new)
            store.append(word)
        sentence=' '.join(store)
        return sentence
    def decrypt():
        Alpha=list(string.ascii_uppercase)
        msg=input('Enter the message you want to decrypt.\n')
        new=msg.upper().split()
        old=''.join(new)
        if old.isalpha() is False:
            print('Error: The message should only contains alphabets.Please enter message in alphabets.')
            decrypt() 
        store=[]
        for i in new:
            new=[]
            for j in i:
                index=Alpha.index(j)
                index-=move
                if (index<0):
                    index-=1
                new.append(Alpha[index])
            word=''.join(new)
            store.append(word)
        sentence=' '.join(store)
        return sentence
    while True:
        option=input('Do you want to (e)ncrypt or (d)ecrypt ?\n')
        if option.lower()=='e':
            move=shift()
            sentence=encrypt()
            print(sentence)
        elif option.lower()=='d':
            move=shift()
            sentence=decrypt()
            print(sentence)
        else:
            print('Please enter the right input.')
            continue
choose()
        