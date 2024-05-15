symbols='AAPL,IBM,MSFT,YHOO,SCO'

print(symbols[0])
symbols[1]
symbols[2]
symbols[-1]
print(symbols[-2])

symbols=symbols+',GOOG'
print(symbols)
symbols ='HPQ,'+symbols
print(symbols)
first='IBM' in symbols
print(first)
sec='AA' in symbols
print(sec)

lower = symbols.lower()
print(lower)

repl = symbols.replace('SCO','BMW')
print(repl)

str = ' IBM    \n'
new_strip = str.strip()
print(str)

name='IBM'
shares=100
price=91.1
print(f'{shares} shares of {name} at ${price:0.2f}' )


text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
 # Find all occurrences of a date
import re
re.findall(r'\d+/\d+/\d+', text)
print(text)
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)


s='hello'
print(dir(s))