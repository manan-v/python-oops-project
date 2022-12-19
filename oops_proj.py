class Login:
  
    def __init__(self) -> None:
        self.name=""
        self.password=""
        self.data={}
        self.menu()

    def menu(self):
        while(1):
            x = input("""
                         1. Enter 1 if you are a new user:
                         2. Enter 2 if you are a current user: 
                         3. Enter 3 for the user list:        
                        4. Exit: 
""")
            if(x=='1'):
             self.signup()
            if(x=='2'):
              self.login()
            if(x=='3'):
              self.ulist()
            if(x=='4'):
              break
    def login(self):
          name = input("enter the name:")
          p= input("enter password:")    
          if(name in self.data):
                obj2 = store()
    def signup(self):
        name = input("enter the name:")
        if(name in self.data):
            print("user already exists")

        else:
          p= input("enter password:")    
          self.data[name]=p  

    def ulist(self):
        for i in self.data:
            print(i)     



class store:
      def __init__(self) -> None:
          # self.medic=""
          # self.price=""
          self.data2={
            "paracetamol": [40,119],
            "vomikind": [30,112],
            "combiflime":[70,67],
            "l-dio1":[47,87],
            "avil": [45,34]
        }
          self.menu2()

      def menu2(self):
            while(1):
                  m = input("""
                                1.Enter 1 to sell the medicine:
                                2.Enter 2 to view all medicine data:
                                3.Exit
                                """)
                  if(m=='1'):
                        self.selling()
                  if(m=='2'):
                        self.view()      
                  if(m=='3'):
                        break   
      # def pdata(self):
      #   print("Medicine   Price   Items")
      #   for i in self.data2:
      #         # print(i+"  "+self.data2[i][0]+"  "+self.data2[i][1])
      #         print("{}  {}  {}".format(i,self.data2[i][0],self.data2[i][12]))
      def view(self):
            print("Medicine     item available        price")
            for it in self.data2:
                  
            # print(it+" "+self.data[it][0]," ",self.data[it][1])
                    print("{}  {}   {}".format(it,self.data2[it][0],self.data2[it][1]))
            # print(self.data[it][0])
      def selling(self):
            medic= input("Enter the name of the medicine:")

            if(medic in self.data2):
                  item = int(input("Enter no. of items for "+medic))
                  if(self.data2[medic][0]<item):
                        print("Sorry we have only " + str(self.data2[medic][0]) + "items available for " + medic)
                        print("selling the available items anyway")
                        print("The Bill for" + str(self.data2[medic][0]) + "items is" + str(self.data2[medic][0]*self.data2[medic][1]))
                        self.data2[medic][0]=0
                  else:
                        print("The Bill for" + str(self.data2[medic][0]) + "items is" + str(self.data2[medic][0]*self.data2[medic][1]))
                        self.data2[medic][0]-= item
            else:
                print("Sorry"+ medic + "is not available") 




obj = Login()
