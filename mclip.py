#! python3
#mclip.py : A Multi - Clipboard Program

TEXT={'agree':'I am attending Tomorrow classes',
      'busy':'I will be absent Tomorrow',
      'holiday':'Tomorrow is holiday.'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: py mclip.py [keyphrase]- copy phrase text.')
    sys.exit()
keyphrase=sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+ keyphrase+' copied to clipboard.')
else:
    print('There is no text for ' +keyphrase)

