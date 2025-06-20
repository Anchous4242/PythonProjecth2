import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_play(self):
        print("Woaf woaf `Time to play`")
        self.progress += 0.1
        self.gladness += 7


    def to_sleep(self):
        print("Yaws `Dog will sleep`")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Bad dog")
            self.gladness -= 20
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Good dog")
            self.gladness += 20

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:*^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

jack = Student(name="Jack")
luna = Student(name="Luna")
simba = Student(name="Simba")
for day in range(3650):
    if jack.alive == False:
        break
    jack.live(day)
    if luna.alive == False:
        break
    luna.live(day)
    if simba.alive == False:
        break
    simba.live(day)