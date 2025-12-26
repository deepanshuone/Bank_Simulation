import gmail
import random
def send_credentials(email,name,acn,pwd):
    con=gmail.GMail('deepanshugarg.5556@gmail.com','axak oufy maod nqmw')
    body=f'''Hello {name} 
    Welcome to ABC Bank here is your credentials
    Account No ={acn}
    password={pwd}
    
    Kindly change your password when you login first time
    
    ABC Bank
    Sector 16,Noida 
    '''


  
    msg=gmail.Message(to=email,subject='Your Credentials for operating account',text=body)
    con.send(msg)


def otp_email(email,name,otp):
    con=gmail.GMail('deepanshugarg.5556@gmail.com','axak oufy maod nqmw')
    
    body=f'''Hello {name} 
    Welcome to PNB Bank here is your otp
    OTP is {otp}
    
   
    
    PNB Bank
    Sector 16,Noida 
    '''
    msg=gmail.Message(to=email,subject='Your OTP(One Time Password)',text=body)
    con.send(msg)

    
