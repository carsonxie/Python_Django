############
# This simple script gives a example how to get envir variables
# Hide password inside environment varibles
# In ubuntun, run nano .bashrc and then set Email_USER to these vars
#  export EMAIL_USER="useforcoding@gmail.com"
#  export EMAIL_PASS="ricbbnsruckjfzen"
# To get these value, see below
# 

import os

#EMAIL_USER = 'useforcoding@gmail.com'
#EMAIL_PASS = 'ricbbnsruckjfzen'


email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')

print(email_user)
print(email_pass)