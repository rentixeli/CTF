########################
#                      #
#   written by bymix   #
#                      #
########################

def main():
    flagenc = "197b18317d060376340c67073161190e6a2d0267063770171860"
    token = "T_O_K_E_N"
    key = ""
    flag = ""

    for i in xrange(0, len(token), 2):
        first_two_chars = flagenc[i:i+2]
        dec_first_two_chars = int(first_two_chars, 16)

        key += chr(dec_first_two_chars ^ ord(token[i]))

    key = (5* 'M4St3RK3y')[:26]
    print key

    for i in range(len(key)):
        first_two_chars = flagenc[:2]
        flagenc = flagenc[2:]

        dec_first_two_chars = int(first_two_chars, 16)
        first_char_key = key[i]

        flag += chr(dec_first_two_chars ^ ord(first_char_key))

    print flag



if __name__ == '__main__':
    main()
