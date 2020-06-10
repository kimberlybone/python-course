x = 20 

# CONDITIONAL 1 (Basic)

# if x > 2 :
#     print('Bigger')
# else :
#     print('Smaller')

# print('All done')



# CONDITIONAL 2 (Multi-way)
# if x < 2 :
#     print('small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')


# CONDITIONAL 3 (Used to catch errors)
astr = 'Hello'
# if
try:
    istr = int(astr)
# else
except:
    istr = "Your code didn't work"

print('Done.', istr)
