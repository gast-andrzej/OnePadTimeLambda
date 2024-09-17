'''
As a program
'''

OPT = lambda xa = list(input("Klucz szyfrowania: ")): print(''.join(chr(h) for h in list(ord(i)+ord(xa[g % len(xa)]) for g, i in enumerate(list(input("Tekst do zaszyfrowania: "))))))
OPT()

DEC_OPT = lambda xa = list(input("Klucz szyfrowania: ")) : print(''.join(chr(h) for h in list(ord(i)-ord(xa[g % len(xa)]) for g, i in enumerate(list(input("Tekst zaszyfrowanej wiadomości: "))))))
DEC_OPT()

'''
As a function
'''
OPT_F = lambda KEY, MESSAGE : ''.join(chr(h) for h in list(ord(i)+ord(KEY[g % len(KEY)]) for g, i in enumerate(list(MESSAGE))))
print(OPT_F('abcd','Example, or maybe not 314'))

DEC_OPT_F = lambda KEY, MESSAGE_TO_DECODE : ''.join(chr(h) for h in list(ord(i)-ord(KEY[g % len(KEY)]) for g, i in enumerate(list(MESSAGE_TO_DECODE))))
print(DEC_OPT_F("abcd", "¦ÚÄÑÑÎÈÑÕÎÃÜÆÆÑÓÕ"))
