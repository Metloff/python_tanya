# Strings
mystring = 'Python for "Beginners"'
print(mystring)
mystring = "Python for 'Beginners'"
print(mystring)

mystring = ''' 
Python course for "Beginners".

Let start!
'''
print(mystring)


# String Manipulation

## The + Operator
print("The + Operator:")
print('foo' + 'bar' + 'baz')
print('Go team' + '!!!')
print("======================")

## The * Operator
print("The * Operator:")
print('foo.' * 4) # foo.foo.foo.foo.
print('foo' * -8) # ''
print("======================")

## The in Operator (есть или нет строка в строке)
print("The in Operator:")
print('foo' in 'That\'s food for thought.') # True
print('foo' in 'That\'s good for now.') # False
print('z' not in 'abc') # True
print("======================")

## Built-in String Functions
print("Built-in String Functions:")
print(len("qwe")) # 3
print(str(49.3)) # '49.3'

## String Indexing
print("String Indexing:")
s = 'foobar'
print(s[0]) # f
print(s[1]) # o
print(s[3]) # b
print(len(s)) # 6
print(s[len(s)-1]) # r
print(s[-1]) # r

## String Slicing
print("String Slicing:")
s = 'foobar'
print(s[2:5]) # 'oba'
print(s[:4]) # 'foob'
print(s[2:]) # 'obar'
print(s[:4] + s[4:]) # foobar
print(s[2:2]) # ''
print(s[4:2]) # ''

## Interpolating Variables Into a String
print("Interpolating Variables Into a String")
n = 20
m = 25
prod = n * m
print('The product of', n, 'and', m, 'is', prod)
print(f'The product of {n} and {m} is {prod}')

## Built-in String Methods
print("Interpolating Variables Into a String")
print('foO BaR BAZ quX'.capitalize()) # 'Foo bar baz qux'
print('FOO Bar 123 baz qUX'.lower()) # 'foo bar 123 baz qux'
print('FOO Bar 123 baz qUX'.swapcase()) # 'foo bAR 123 BAZ Qux'
print('the sun also rises'.title()) # 'The Sun Also Rises'
print('FOO Bar 123 baz qUX'.upper()) # 'FOO BAR 123 BAZ QUX'
print('foo bar foo baz foo qux'.replace('foo', 'grault')) # 'grault bar grault baz grault qux'
print('   foo bar baz\t\t\t'.strip()) # 'foo bar baz'


# https://realpython.com/python-strings/#bytes-objects