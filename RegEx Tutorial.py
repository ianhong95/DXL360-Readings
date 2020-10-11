import re

# message = "Call me 415-555-1011 tomorrow, or at 415-555-9999"

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search(message)

# # group() returns the pattern
# print(mo.group(1))

# phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# mo2 = phoneNumRegex.search(message)
# print(mo2.group())



# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo3 = batRegex.search('Batmobile lost a wheel')
# print(mo3.group())


# Question mark means what's in the brackets can appear 0 or 1 times to
# match the pattern
# batRegex = re.compile(r'Bat(wo)?man')

# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())




# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
# print(mo.group())


# Asterisk means the regex can appear 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('I am Batwowowoman')
print(mo.group())

# Plus means appear 1 or more times (not optional)