#All calculation of Arithmetic function----
def add(a,b):
    '''Add the two number'''
    return( a + b)
def sub(a,b):
    '''It will substract the second number to first one '''
    return(a - b)
def multi(n,m):
    '''Multiply the both number to each other'''
    return(n * m)
def div(n,m):
    '''Divide the first number by the second number'''
    return(n/m)
def remd(n,m):
    '''Finds the reminder after division of two number'''
    return(n%m)
def pow(a,b):
    '''just find the power

    a - give the base number
    b - give the power number of base'''
    return(a**b)

#Function of bitwise operation----
def bitand(a,b):
    '''it check both are true or not, on the basis of bit-by-bit'''
    bi=(a & b)
    return((bi))
def bitor(a,b):
    '''it check one of them are true or not, on the basis of bit-by-bit'''
    bi=(a | b)
    return((bi))
def bitnot(a):
    '''it check condition are true or not, if true it will give false and if false will give true'''
    bi= ~a
    return((bi))
def bitxor(a,b):
    '''it will return 1 if one is 1 and other is 0 else 0'''
    bi=(a^b)
    return(bi)
def bit_r_shift(n,m):
    bi = n >> m
    return(bi)
def bit_l_shift(n,m):
    bi = n << m
    return(bi)

