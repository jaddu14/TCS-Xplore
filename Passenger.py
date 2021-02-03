class Passenger:
    def __init__(self,id,name,gender,miles):
        self.id=id
        self.name=name
        self.gender=gender
        self.miles=miles
    def CalculateDiscount(self,rate):
        discount=self.miles*rate/100
        return discount
class Organisation:
    def __init__(self,name,plist):
        self.name=name
        self.plist=plist
    def CalcDisc(self,id,drates):
        dis=0
        for i in self.plist:
            if i.id==id:
                dis=i.CalculateDiscount(drates)
                if dis>0:
                    return dis
                else:
                    return -1
        return 0

if __name__ =="__main__":
    n=int(input())
    plist=[]
    for i in range(n):
        id=int(input())
        name=input()
        gender=input()
        miles=int(input())
        plist.append(Passenger(id,name,gender,miles))
    O=Organisation('TCS',plist)
    id=int(input())
    drates=int(input())
    res=O.CalcDisc(id,drates)
    if res!=0:
        if res>0:
            print(res)
        else:
            print('No discount rates')
    else:
        print('no passenger is there with this id')
