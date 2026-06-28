import re , time , sys
import pyperclip as py
from pprint import pprint
def main():
    def Websites(String):
            # Website scope 
            protocol=re.compile(r"https?://\S*")
            Pattern=protocol.findall(str(String))
            return Pattern
    
    def dates(String):
            # dates Scope
            pass #Under Development
    def Sensitive(String):
            pass
    def Typos(String):
            pass
    # main() scope
    value=int(input(''' What do your want to do. 
                1. Find website URLs that begin with http:// or https://
                2. Clean up dates in different date formats 
                3. Remove sensitive information such as Social Security or credit card numbers.
                4. Find common typos such as multiple spaces between words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences.
                5. Exit\n ''' ))
    if (value==1):
        print('All the matched paterns are as follows:\n')
        pprint(Websites(String))
        print()
    elif (value==2):
        dates(String)
    elif (value==3):
        Sensitive(String)
    elif (value==4):
        Typos(String)
    elif (value==5):
        sys.exit('Program Terminated!')
    else:
        print('Please enter valid input.')
        main()
input('Copy the text on your system clipboard. Press Enter once you are done.\n ')
String=py.paste()
main()