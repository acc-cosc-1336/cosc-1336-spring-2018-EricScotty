def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
   

    for ch in dna_string:
        if ch == 'A' or ch == 'A':
            count1 += 1

        if ch == 'C' or ch == 'c':
            count2 += 1

        if ch == 'G' or ch == 'g':
            count3 += 1

        if ch == 'T' or ch == 't':
            count4 += 1

    return count1,count2,count3,count4
