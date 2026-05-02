# Pattern by PRAJJWAL KUMAR UPADHYAY.                                                    Date-28/04/2026
import re,pyperclip,requests,sys
from bs4 import BeautifulSoup
def main():
        def WebSite():    
            address=pyperclip.paste()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            res=requests.get(str(address),headers=headers)
            if (res.status_code!=requests.codes.ok):
                sys.exit('Error: Unable to access the website. Please check the URL and try again.')
            soup=BeautifulSoup(res.text,'html.parser')
            text=soup.get_text()
            Regex() #Note: Many websites will block or slow down your request , as prevention.
            def Regex():
                number=re.compile(r'''\+91\s?\d{5}\s?\d{5}| #India
                                \+1\s?\(\d{3}\)\s?\d{3}-\d{4}| #USA/Canada
                                \+44\s?\d{4}\s?\d{6}| #UK
                                \+49\s?\d{2}\s?\d{8}| #Germany
                                \+61\s?\d{3}\s?\d{3}\s?\d{4}| #Australia
                                \+971\s?\d{2}\s?\d{3}\s?\d{4}| #UAE
                                \+86\s?\d{3}\s?\d{4}\s?\d{4}| #China
                                \+55\s?\d{2}\s?\d{5}-\d{4} #Brazil''',re.VERBOSE)
                Email=re.compile(r'[a-z0-9.*#$%^&!]+@[a-z0-9]+\.[a-z]{2,}',re.I)
                result1=number.findall(text)
                result2=Email.findall(text)
                print(result1)
                print(result2)
            #under Development
main()
