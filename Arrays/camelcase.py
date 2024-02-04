
# input -->  helloIndiaMan

# output -->  
# HELLO
# iNDIA
# mAN

def camelcase(string):
    string_mod = ""
    i = 0
    while i < len(string):
        if 'a' <= string[i] <= 'z':
            string_mod += string[i].upper()
        elif 'A' <= string[i] <= 'Z':
            print(string_mod)
            string_mod = ""
            string_mod += string[i].lower()
        else:
            string_mod += string[i]

        i += 1

    print(string_mod)

    # for i in string:
    #     if i.islower:
    #         string_mod += i.upper()
    #     elif i.isupper:
    #         print(string_mod)
    #         string_mod = ''
    #         string_mod += i.lower()
    #     else:
    #         string_mod += i
        
    #     # i += 1

    # print(string_mod)


input_str = "helloIndiaMan"
camelcase(input_str)





