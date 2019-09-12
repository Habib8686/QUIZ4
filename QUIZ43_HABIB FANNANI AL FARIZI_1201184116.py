listGPA = [2.1,2.5,4,3]

def Reward (GPA):
    bonus = 500000
    Reward = GPA*bonus
    return Reward 

for GPA in listGPA:
    if GPA > 2.5:
        print("Selamat bos! anda mendapat reward : Rp", Reward(GPA))
    else :
        print("Yah Kasian bos,Di coba lagi ya.")
