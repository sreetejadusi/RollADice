import random


class Variables:
    lower = 1
    upper = 6
    dice = 1


class Begin:
    initial = 1
    values = []

    def __init__(self):

        try:
            Variables.dice = int(input("How Many Dice You Want To Roll?: "))

        except ValueError:
            print("Only input numbers!")
            self.__init__()

        if Variables.dice == 0:
            print("Okay!")

        while self.initial <= Variables.dice:
            self.roll = random.randint(Variables.lower, Variables.upper)
            self.values.append(self.roll)
            self.initial += 1
        self.output = sum(self.values)


begin = Begin()

print("Your Values are: ")

for x in list(begin.values):
    print(x)

print("Total:" + str(begin.output))

#A Code By Sree Teja Dusi
#GitHub: https://github.com/sreetejadusi
#LinkedIn: https://linkedin.com/in/sreetejadusi
#Website: https://sreetejadusi.me
#Twitter: https://twitter.com/sreetejadusi
#Instagram: https://instagram.com/sreeteja_dusi
#Facebook: https://facebook.com/sreetejadusi