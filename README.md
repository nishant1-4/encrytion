# Encryption From Scratch 🔐

## First of all what is encryption?
  converting a message into an unreadable format so that only the intended receiver can read it.

## What i wrote?
  A simple code that takes a message from user and encrypts it with the random session key generated with random module from range(20,51) --inclusive of 50,
  to <=255 bits for each character in the message.

## What it contains?
  1. Random module.
  2. Session key that is used to encrypt the whole message.
  3. Decimal to binary function.
  4. Binary to decimal function.
  5. Convert bits(0,1) to base64.
  6. Convert base64 to bit(0,1) and reverse till the orginal msg.

## Why i wrote it from scratch?
  Actually, i want working on a simple terminal based banking project which have some simple operations like withdraw, deposit, etc.
  So I wanted to add a secret pin method to ask the user his pin to send or withdraw some amount.
  Then a thought came to mind, in real banking, how the pin is checked in an ATM(Automated Teller Machine). Then I went deep and came across to the word encryption and it was interesting topic.
  So I searched encryption on youtube, claude ai and any other learning platfrom and learnt encryption deeply. It was very interesting and became my top favorite part of technolgy.

  So, to know how it works under the hood, I made it from scratch.

## Note:
  This project is not completed yet, I will keep updating it eventually to a simple flexible end-to-end encryption and apply it to my banking project.

## Project Status:
   XOR Encryption ✅
   Binary Conversion ✅
   Base64 Encoding ✅
   Base64 Decoding ❌
   RSA Key Generation ❌
   RSA Encrypt / Decrypt ❌
   Digital Signatures ❌
   Full End to End Demo ❌

## How to run it?
 Just copy the code in a python file(python should be installed in your system), paste it in a python file using any code editor(vs code, cursor ,etc) then go to terminal(ctrl + j)
 go to the folder where you python file exists using (cd folder/python file) and write python your_file_name.py.
   A msg will come like this:
     Enter your message:
      Enter a message then press enter and an encrypted hash will come as output!

## Update !
  1. Today is 7-June-2026, I added base64 decoding and splitted different functions into file for maintaining clean code structure.

### Thanks for coming here!
