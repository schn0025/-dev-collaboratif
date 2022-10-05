def convert(n : int, b : int) -> str :
    rep=''
    q=-1
    if b>10:
        return 'la base est sup a 16'
    while q !=0: #q pour quotient
        q=n//b
        r=n%b
        n=q
        rep+=str(r)
    return rep[::-1]
