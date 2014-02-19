print "Type 'CO' to convert the text to new characters"
print "Type 'EN' to convert the text to English"
print "Type 'BF' to brute force the text."

response = None

while response not in ["CO", "EN", "BF"]:
    response = raw_input("").upper()

stri = [i for i in raw_input("Phrase: ")]
phrase = []
num = ""

if response != "BF":
    while type(num) != int:
        try: num = int(raw_input("Number: "))
        except ValueError: num=""
        if not 0 <= num <= 26: num = ""

if response in ["CO", "EN"]:
    for i in stri:
        if i.isalpha():
            if response == "CO":
                value = ord(i.lower()) + num
                if value > 122:
                    value = 97 + (value - 123)
            elif response == "EN":
                value = ord(i.lower()) - num
                if value < 97:
                    value = 123 - (97 - value)
        else:
            value = ord(i)
        if i.isupper():
            phrase.append(chr(value).upper())
        else:
            phrase.append(chr(value))
    print "".join(phrase)
if response == "BF":
    for x in range(26):
        for i in stri:
            if i.isalpha():
                value = ord(i.lower()) + x
                if value > 122:
                    value = 97 + (value - 123)
            else:
                value = ord(i)
            if i.isupper():
                phrase.append(chr(value).upper())
            else:
                phrase.append(chr(value))
        print str(x).zfill(2) + ") " + "".join(phrase)
        phrase = []