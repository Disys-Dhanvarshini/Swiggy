class swiggy:
        
        dc = filter(lambda x: x["rating"]>4,[{"location":"guindy","name":"Dindigul Thalapakathi","maincourse":"Chicken Biryani","rating":5},
                {"location":"anna nagar","name":"anjappar","maincourse":"Mutton Biryani","rating":5},
                {"location":"guindy","name":"Buhari","maincourse":"Prawn Biryani","rating":4}])
        for i in dc:
                print(i)
        def __init__(self):
                self.name = input("enter the hotel name")
                self.dish = input("enter the food name")
        def adressverify(self):
                self.adress = input("enter the address")
                
        
                if (type(self.adress) == str) and (self.adress != None):
                  if (len(str(self.adress)) != 0 and len(str(self.adress)) >=10  ):
                       print("added address")
                  else:
                       raise ValueError("Please Enter the address")
        def phverify(self):
                self.number = input("enter phone number")
                if type(self.number) == str:
                     if (len(str(self.number)) == 10):
                       print("Done!")
                     elif((self.number) == None or (self.number!=10)):
                             raise ValueError("Please enter your number to make your delivery easy")
                      
                
                
                for i in restaurants:
                        for x,y in  i.items():
                                if y == self.name:
                                        print("Hotel",self.name)
                for i in restaurants:
                        for x,y in i.items():
                                        if y == self.dish:
                                                print("bill")
                                                print(self.dish)
                                               
                

restaurants =  restaurants = [{"location":"guindy","name":"Dindigul Thalapakathi","maincourse":"Chicken Biryani","rating":5},
                {"location":"anna nagar","name":"anjappar","maincourse":"Mutton Biryani","rating":5},
                {"location":"guindy","name":"Buhari","maincourse":"Prawn Biryani","rating":4}]
obj = swiggy()
obj.adressverify()       
obj.phverify()
