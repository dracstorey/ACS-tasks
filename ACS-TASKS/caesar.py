# Take each character of a message #



# brute force offset
for j in range (26):
    msg = "The quick brown fox jumped over the lazy dog"
    msg = "WKH TXLFN EURZQ IRA MXPSHG RYHU WKH ODCB GRJ"
    msg = msg.upper()

    #offset = 3
    encrypted_msg = ""
    for i in range (len(msg)):
        
        if msg[i] == " ":
            encrypted_msg = encrypted_msg + " "
        else:
            # Get value of character
            val = ord(msg[i])
            # add offset
            val = val + j

            # check highest value and loop back round
            val = ((val - 65) % 26) + 65

            # convert back to charter from ASCII
            new_char = chr(val)

            encrypted_msg = encrypted_msg + new_char
        # end if
    # Next    

    print (26-j, ":", encrypted_msg)
    
# Next j
# Shifts the character and repalces with the the offset character #