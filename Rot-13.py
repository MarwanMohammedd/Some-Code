def Rot(String : str)->str:
    '''
    ROTATE BY 13 ALGORITHM THAT CONVERTE THE CHARACTER AND ADD TO INDEX 13 
    TO ENCREPT DATA .
    '''
    __strList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __endStr = ''
    for ind in String.upper().strip():
        if ind == ' ':
            __endStr += ' '
        elif __strList.index(ind)+13 >= 26 :
            __endStr +=__strList[(__strList.index(ind)+13)-26]
        else:
            __endStr +=__strList[__strList.index(ind) + 13]
    return __endStr