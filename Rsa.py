import sys
from random import randint

class Rsa:
    def __init__(self):
        
        print("從下列6數選2數")
        print(self.genRandomList())  #呼叫6個亂數質數函數

        self.p,self.q = map(int,input().split())  #選擇輸入兩個亂數質數
        self.N=self.p*self.q    #製作N
        self.N1=(self.p-1)*(self.q-1)  #製作N1
        print("從下列3數選1數為e: ")  
        print(self.genEList(self.N1))  #呼叫選3個e和N1互質函數
        self.e = int(input())   #選擇輸入互質數e
        print("從下列3數選1數為d: ")
        print(self.genDList(self.e,self.N1))  #呼叫製作d的函數
        self.d = int(input())   #選擇輸入d
        print()
        print("加密金鑰: ",self.e,self.N)
        
        print("加密數字:")
        self.emsg = int(input()) #輸入要加數字
        print("加密後: ")
        print(self.encrypt(self.emsg,self.e,self.N),"\n") #呼叫加密函數

        print("解密金鑰: ",self.e,self.N)

        print("解密數字:")
        self.dmsg = int(input()) #輸入要解密函數
        print("解密後: ")
        print(self.decrypt(self.dmsg,self.d,self.N))  #呼叫解密函數
        
    def encrypt(self,emsg,e,N):  #製作加密函數
        x = emsg**e  #公式:加密數的e次方除以N的餘數
        y = x%N
        return y

    def decrypt(self,dmsg,d,N):  #製作解密函數
        x = dmsg**d  #公式:解密數的次方除以N的餘數
        y = x%N
        return y
        
    
    def genRandomList(self):#製作6個亂數質數函數
        data = []
        while len(data)<6:
            y = randint(3,2000)
            if self.isPrime(y):#呼叫製作質數函數
                data.append(y)
        return data
    def isPrime(self,x):#製作質數函數
        flag = True
        i= 2
        while  i<(x/2):
            if (x%i == 0):
                flag = False
                break 
            i = i+1
        return flag
    
    def genEList(self,x) :#選3個e和N1互質函數
        data = []
        while len(data)<3:
            y = randint(3,2000)
            if self.N1cop(x,y):#呼叫製作互質函數
                data.append(y)
        return data
    def N1cop(self,n1,e):#製作互質函數
        i = 2
        flag = True
        while i<=n1:
            if(n1%i==0):
                if(e%i==0):
                    flag = False
                    break
            i=i+1
        return flag

    def genDList(self,e,N1) :#製作d的函數 d公式:(d*e)%N1 =1
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
    
    
    
    
    
#             執行結果:  

# 從下列6數選2數
# [1889, 191, 643, 1297, 1801, 1277]
# 191 643
# 從下列3數選1數為e: 
# [1367, 1067, 773]
# 773
# 從下列3數選1數為d: 
# [40397, 162377, 284357]
# 40397

# 加密金鑰:  773 122813
# 加密數字:
# 55
# 加密後:
# 72618

# 解密金鑰:  773 122813
# 解密數字:
# 72618
# 解密後: 
# 55
