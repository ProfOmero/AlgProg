def entrada(id, tam):
    a = []
    for i in range(tam):
        a.append(int(input(f"{i+1}o. item, {id}[{i}] = ")))
        
    return(a)

def saida(id, a):
    result = "["
    for i in range(len(a)):
        result += str(a[i])
        if (i != (len(a)-1)):
            result += ", "
            
    result += "]"
    
    return(result)
    
def somar(a):
    return(sum(a))

def media(a):
    return(sum(a) / len(a))

def toString(id, a):
    return(f"{saida(id, a)}\n" + \
           f"soma = {somar(a)}\n" + \
           f"média = {media(a)}")


                 
                 
        