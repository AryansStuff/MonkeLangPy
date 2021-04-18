import basic

print('ur bloat')
while True:
    # Run Stuff
    text = input('MonkeLang > ')
    result, error = basic.run('<stdin>', text)




    # Syntax Stuff
    if text == 'version':
      print('0.0.0.4.2.0')
    if 'print' in text:
      noPrefix = text.replace('print(','')
      newTXT = noPrefix.replace(')','')
      print(newTXT)
    elif error: print(error.as_string())
    else: print(result)