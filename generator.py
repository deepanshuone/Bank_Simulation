import random 
def generate_pass():
   pwd=""
   for i in range(2):
        c=chr(random.randint(97,123))
        pwd+=c
        c=chr(random.randint(65,90))
        pwd+=c
        return pwd
def otp_generator():
   otp=random.randint(1000,9999)
   return otp