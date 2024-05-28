import cv2
import os
import string
#to read the image
img=cv2.imread("dragon.jpg")
#to read the message and password
msg=input("Enter the secret message: ")
password=input("Enter the password: ")
#to encrypt
#encryption key
d={}
c={}
for i in range (255):
    d[chr(i)]=i #storing value of key
    c[i]=chr(i) #for decryption
    #setting variables
m=0; #row
n=0; #column
z=0;

    
# encryption of message
for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    #location where we store the message
    n=n+1
    m=m+1
    z=(z+1)%3
#to write a message in image assigned
cv2.imwrite("encryptedImage.jpg",img)
os.startfile("encryptedImage.jpg")
# Decryption
message="" #storing message
#initializing the variables
n=0
m=0
z=0
pas=input("Enter passcode for Decryption: ")
if(password==pas):
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        #retrieving message from location
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decrypted message is ",message)

else:
    print("You are not the Authenticated")
        
