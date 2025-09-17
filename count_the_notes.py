amount=int(input("put your money here :"))

note1= amount//100
note2=(amount%100)//50
note3=(amount%100%50)//25

print("the value of 100 notes is:", note1)
print("the value of 50 notes is:", note2)
print("the value of 25 notes is :", note3)

