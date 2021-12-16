from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import string
import re
import secrets
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')




res = ''.join(secrets.choice(string.digits) for x in range(6)) 





entry = Entry(root,fg='#FF4517',bg='#FFF9C2',bd=1)
entry.place(x=120,y=50,width=350,height=20)


label = Label(root,text='Enter Your Mail')
label.place(x=15,y=50)

entry2 = Entry(root)
entry2.place(x=120,y=190,width=350,height=20)

label2 = Label(root,text='Enter Your OTP')
label2.place(x=15,y=190)

def vali():
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+[.com]")
                   
    if email_regex.match(entry.get()):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()

    
        smtp.login('your mail', 'mail password')


        
        def message(subject="Python Notification",
                    text="", img=None,
                    ):
            
        
            msg = MIMEMultipart()
            
        
            msg['Subject'] = subject
            
        
            msg.attach(MIMEText(text))


                
            return msg


    
        msg = message("Hey Welcome!", f"Hi there your otp: {res}")

    
        to = [entry.get()]

        
        smtp.sendmail(from_addr="your mail",
                    to_addrs=to, msg=msg.as_string())


        smtp.quit()
        
        entry.delete(0,END)
        btn['state'] =DISABLED
        btn2['state'] =NORMAL
    elif entry.get() =='':
        messagebox.showinfo('','enter your E-mail')
    else:
        messagebox.showinfo('','enter valid E-mail')
        
def result():
    if entry2.get() == res:
        messagebox.showinfo('','Login succuss')
        entry2.delete(0,END)
    else:
        messagebox.showinfo('','Login failed')
        
    entry.delete(0,END)






btn = Button(root,text="Send OTP",bd=0,bg='#1061E6',command=vali)
btn.place(x=199,y=120)

btn2= Button(root,text="Submit",bg='#B3B3FF',command=result)
btn2.place(x=199,y=260)
btn2['state'] =DISABLED

root.mainloop()