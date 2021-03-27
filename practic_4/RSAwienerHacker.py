import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)  # Создаём list частных непрерывных дрообей [a0, ..., an]
    convergents = ContinuedFractions.convergents_from_contfrac(frac)  # вычисление подходящих дробей
    
    for (k,d) in convergents:
        # print('k, d: ', k, d)
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            # print(phi, s, discr)
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                # print('sqrt: ', t)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 1
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(16)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()


    


        
    
