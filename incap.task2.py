##1
# 
#  class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometr = 0
#         self.fuel = 70

#     def get_info(self):
#         info = f"Car {self.make} {self.model} designed in {self.year}"
#         print(info)
        

#     def deal(self,distance):
#         self.distance = distance
#         if self.distance // 10 <= self.fuel:
#             print("lets go")
#         else:
#             print("Not enough fuel ")
#         self.__add_distance()
#         self.__subtract_fuel()

#     def __add_distance(self):
#         self.odometr += self.distance
#         print("You have drown",self.odometr,"km")

#     def __subtract_fuel(self):
#         self.fuel -= self.distance//10
#         print("You have left ", self.fuel, "litres fuel")

# car = Car("Toyota","Camry",2012)
# car.get_info()
# car.distance = 100
# car.deal(100)

##2

# import random
# class Phone:
#     __imei = "121215121212"
#     __battery_level = 100
#     __info = "Android 6.0.1 Marshmallow"

#     def access(self):
#         if self.__battery_level >= 0.5:
#             self.__battery_level -= 0.5 
#         else:
#             print("Need to charge")
        
#     def music(self):
#         if self.__battery_level > 5:
#             self.__battery_level -= 5
#             print("Music is on")
#         else:
#             print('Unavailable! Need to charge ')

#     def video(self):
#         if self.__battery_level >= 17:
#             self.__battery_level -= 7
#             print("Video is going on")
#         else:
#             print("Video is unavailable! Battery is too low")
       
#     def charge(self):
#         if self.__battery_level < 100:
#             charge = int(random.randint(1,10))
#             self.__battery_level += charge
#         else:
#             print("Battery is full")

# phone = Phone()
# phone.access()
# phone.music()
# phone.video()
# phone.charge()
# print(phone._Phone__battery_level)


##3

# import math


# class Pyramid:
#     __lenghth_of_basic = ''
#     __lenghth_of_side =''

#     def __init__(self,__lenghth_of_basic,__lenghth_of_side):
#         self.__lenghth_of_basic = __lenghth_of_basic
#         self.__lenghth_of_side = __lenghth_of_side



#     def __square_area(self):
#         self.s1 = self.__lenghth_of_basic **2
#         return self.s1

#     def __sides_area(self):
#         p = (self.__lenghth_of_side + self.__lenghth_of_side + self.__lenghth_of_basic)/2
#         self.s2 = math.sqrt((p*(p - self.__lenghth_of_basic)*((p- self.__lenghth_of_side )**2)))
#         return self.s2
#     def area(self):
#         self.__square_area()
#         self.__sides_area()
#         s = self.s1 + (self.s2)*4
#         return s
#     def __height(self):
#         h1 = math.sqrt((self.__lenghth_of_basic**2)*2)
#         h2 = h1/2
#         self.h = math.sqrt((self.__lenghth_of_side**2)-(h2**2))

#     def volume(self):
#         self.__square_area()
#         self.__height()
#         v = (self.s1*self.h)/3
#         return v


# pyr = Pyramid(20,30)
# pyr.area()
# print(pyr.area())
# pyr.volume()
# print(pyr.volume())
