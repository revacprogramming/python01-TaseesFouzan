# Strings

string = "X-DSPAM-Confidence:    0.8475"


sus = string.find(':')                 
number = string[sus + 1:]                 
beach = float(number)                  
print(beach)