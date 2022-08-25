#!/usr/bin/python3
     
def validUTF8(data):
    number_bytes = 0
    for num in data:
        
        bin_rep = format(num, '#010b')[-8:] 
        if number_bytes == 0:
            j
            for bit in bin_rep:
                if bit == '0': break
                number_bytes += 1
                if number_bytes == 0:
                    continue
                if number_bytes == 1 or number_bytes > 4:
                    return False
            else:
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False
                number_bytes -= 1
                return number_bytes == 0
