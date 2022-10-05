def convert(n : int, b : int) -> str :
    rep=''
    q=-1
    if b>16:
        return 'la base est sup a 16'
    if b==10:
        return str(n)

    while q !=0: #q pour quotient
        q=n//b
        r=n%b
        n=q
        if r<10 or b<10:
            rep+=str(r)
        elif r==10 and b>10:
            rep+='A'
        elif r==11 and b>11:
            rep+='B'
        elif r==12 and b>12:
            rep+='C'
        elif r==13 and b>13:
            rep+='D'
        elif r==14 and b>14:
            rep+='E'
        elif r==15 and b>15:
            rep+='F'
        else:
            return ('erreur',r)
    return rep[::-1]
