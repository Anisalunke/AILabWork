class Vehicle:
    def __init__(self,name,bike,fuel,tyres,storage,economical):
        self.name = name
        self.bike = bike
        self.fuel= fuel
        self.tyres = tyres
        self.storage = storage
        self.economical = economical
    
    
    def check_if_mountain_bike(self,object):
        if(object.bike == True and object.fuel=="good" and object.tyres == "good"):
            print(f"{object.name} is a mountrin bike\n")
            return True
        else:
            print(f"{object.name} is not a mountain bike\n")
            return False
    
    def check_if_best(self,object):
        if(object.check_if_mountain_bike(object)):
            if(object.storage=="good" and object.economical =="yes"):
                print(f"-->{object.name} is the best bike for a ladakh road trip\n")
            else:
                print(f"{object.name} is not best bike for ladakh road trip\n")

def main():
    him = Vehicle("Royal Enfield Himalayan",True,"good","good","good","yes")
    Spl = Vehicle("Splendor",True,"bad","good","good","yes")
    ktm = Vehicle("KTM Duke",True,"good","good","bad","yes")
    Hon = Vehicle("Honda City",False,"good","good","good","no")
    check_list =[him,Spl,ktm,Hon]
    for i in check_list:
        i.check_if_best(i)

main()
