alphabhat=['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    chiper_text=""
    for char in plain_text:
        position=alphabhat.index(char)
        new_position=(position+shift_key)%26
        chiper_text += alphabhat[new_position]
    print(f"encrytion is :{chiper_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position=alphabhat.index(char)
        new_position=(position-shift_key)%26
        plain_text += alphabhat[new_position]
    print(f"decrytion is :{plain_text}")



what_to_do=input("type 'encrypt' to encryption,type 'decrypt' to decryption.:\n")
text=input("enter your message:\n").lower()
shift=int(input("enter shift key:\n"))
if what_to_do=="encrypt":
    encryption(plain_text=text,shift_key=shift)
elif what_to_do=="decrypt":
    decryption(cipher_text=text,shift_key=shift)
