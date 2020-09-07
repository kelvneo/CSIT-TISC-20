# CSIT The InfoSec Challenge 2020

## Stage 1:
>Main Writeup: [stage1.md](stage1.md)

The general solution is to use johntheripper/hashcat/fcrackzip to first crack the initial encrypted zip, then write a short script to decompress or decode the file type based on its MIME type.

### Reflections

The main challenges I faced in this problem was definitely finding the correct linux command to run to decompress the file, only to find out I can just use python libraries to do everything for me... 

## Stage 2
>Main Writeup: [stage2.md](stage2.md)

The general solution is to first unpack the executable file, then finding the instruction address that corresponds to the decoding of Base64. Set a breakpoint at that address and run the program. Analyse the registers values to find out the base64 value stored inside the program, then SHA256 that base64 value and submit it as a flag.

### Reflections
There were a few red herrings, especially when I check the strings of the file itself. There was a RSA testing key, and another Base64 string that was not decodeable.

## Stage 3
>Main Writeup: [stage3.md](stage3.md)

To decrypt the file, we have to find the key and IV, which is conveniently stored in the `keydetails-enc.txt`, but it is encoded or encrypted with an unknown format.

Analysing the program yields an instructions that calls the exponent function in Golang, right before the writing to file. We can check the arguments the function will be executed with to determine the power value. In this instance, they cubed the value of a string.

So we can take the cube root of the integer value of the file, and convert the bytes of the integer into ASCII to derive a URL encoded key and IV.

We can then take the key and IV, and inject it back into the ransomware to decrypt the files (as the encryption scheme is AES-CTR, which is invertible). We then check the strings of our decrypted files, and we would obtain the flag.

### Reflections
While I could get the key and IV by guessing in a few hours, it took me ridiculously long to decrypt the files. There is a third variable called `EnvIVCur` which is probably the reason why online tools and default AES-CTR parameters would not work, even after swapping endians. So in order to decrypt the files, I just went heck it, and decided to replace the key and IV when the ransomware is running to simulate decrypting of the files, which somehow worked.

## Stage 4
While I did not solve the challenge, I was able to generate the domain name by injecting the unix time to `$rax` and `$rcx` at address `0x00000000006614c2`, then checking the stack for the domain name at `0x000000000066172b`.

