import sys
import random as rand

class Rsa:
    def __init__(self):
        
        print("從下列6數選2數")
        print(self.genRandomList())

        self.p,self.q = map(int,input().split())
        self.N=self.p*self.q
        self.N1=(self.p-1)*(self.q-1)
        print("從下列3數選1數為e: ")
        print(self.genEList(self.N1))
        self.e = int(input())
        print("從下列3數選1數為d: ")
        print(self.genDList(self.e,self.N1))
        self.d = int(input())
        
        print("加密數字:")
        self.emsg = int(input())
        print("加密後: ")
        print(self.encrypt(self.emsg,self.e,self.N))

        print("解密數字:")
        self.dmsg = int(input())
        print("解密後: ")
        print(self.decrypt(self.dmsg,self.d,self.N))
        
    def encrypt(self,emsg,e,N):
        x = emsg**e
        y = x%N
        return y

    def decrypt(self,dmsg,d,N):
        x = dmsg**d
        y = x%N
        return y
        

    
    
    def genRandomList(self):
        data = []
        while len(data)<6:
            y = rand.randint(3,2000)
            if self.isPrime(y):
                data.append(y)
        return data
    def isPrime(self,x):
        flag = True
        i= 2
        while  i<(x/2):
            if (x%i == 0):
                flag = False
                break 
            i = i+1
        return flag
    
    def genEList(self,x) :#選3個e 和N1互質
        data = []
        while len(data)<3:
            y = rand.randint(3,2000)
            if self.N1cop(x,y):
                data.append(y)
        return data
    def N1cop(self,n1,e):#互質
        i = 2
        flag = True
        while i<=n1:
            if(n1%i==0):
                if(e%i==0):
                    flag = False
                    break
            i=i+1
        return flag

    def genDList(self,e,N1) :#(d*e)%N1 =1
        data = []
        i = 2
        while len(data)<3:
            y = i
            d = y*e
            if (d%N1 == 1):
                data.append(y)
            i=i+1
        return data
        
    
        
 
 
 
if __name__ == "__main__":
    rsa = Rsa()
   

