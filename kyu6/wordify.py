def wordify(n):
    ones= {0:"zero",1:"one",2:"two",3:"three",4:"four", 5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}       
    tens = {2:"twenty",  3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    
    numstr = str(n).zfill(3)
    pos1int= int(numstr[0])
    pos2int = int(numstr[1])
    pos3int = int(numstr[2])
    if pos1int == 0:
        if int(numstr[1:]) in teens: 
            return teens[int(numstr[1:])]
        elif pos2int in tens:
            if pos3int == 0:
                return tens[pos2int]
            return tens[pos2int]+" "+ones[pos3int]
        elif pos2int not in tens:
                return ones[pos3int]
    
    if pos1int > 0:
        if int(numstr[1:]) in teens: 
            return ones[pos1int]+' hundred '+ teens[int(numstr[1:])]
        elif pos2int in tens:
            if pos3int == 0:
                return ones[pos1int]+' hundred '+tens[pos2int]
            return ones[pos1int]+' hundred '+tens[pos2int]+" "+ones[pos3int]
        elif pos2int not in tens:
            if pos3int > 0:
                return ones[pos1int]+' hundred '+ ones[pos3int]
            return ones[pos1int]+' hundred'
    
        
        
    