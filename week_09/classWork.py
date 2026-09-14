#Single Inher.. (class A(B))
# class A:
#     def __init__(self, name):
#         self.name = name
#         print(f"CLass A! {self.name}")
# class B(A):
#     def __init__(self, name):
#         super().__init__(name)
#         print("CLass B")


#Multi Inher..   (class B(A) ,,,,  class C(B))
# class A:
#     def __init__(self, name):
#         self.name = name
#         print(f"CLass A! {self.name}")
# class B(A):
#     def __init__(self, name):
#         super().__init__(name)
#         print("CLass B")
# class C(B):
#     def __init__(self,name):
#         super().__init__(name)
#         print("CLass C")

#Multiple Inher..   (class C(A,B))

# o1 = C("Owais")
# print(o1.name)

# Multiple inher..
# class A:
#     def __init__(self, name):
#         self.name = name
#         print(f"CLass A! {self.name}")
# class B:
#     def __init__(self, name):
#         self.name = name
#         print(f"CLass B! {self.name}")
# class C(B, A):
#     def __init__(self,name):
#         super().__init__(name)
#         print("CLass C")
# o1 = C("Owais")

# class A:
#     user_id = 1234
#     def __init__(self, name):
#         self.name = name
#         print(f"CLass A! {self.name}")

# o1 = A("Owais")
# print(o1.name)
# print(o1.user_id)
# o1.user_id = 4321
# print(o1.user_id)

class A:
    def __init__(self, name, user_id):
        self.name = name 
        self.__user_id = user_id 
        print(f"CLass A! {self.name}")
        print(f"CLass A! {self.__user_id}")
    # def user_id(self):
    #     return self.__user_id
    
    @property
    def userID(self):
        return self.__user_id

    @userID.setter
    def userID(self, val):
        self.__user_id = val

value = 10
o1 = A("Owais", value)
print(o1.userID)
o1.userID = 4
print(o1.userID)
o1.userID=5
print(o1.userID)
# print(o1.__user_id) # Error
# print(o1.user_id()) # Using Fucntion/Methods
# print(o1._A__user_id) # Using Name Mangling
