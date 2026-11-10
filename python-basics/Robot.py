class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def work(self):
        self.battery -= 10
        print(f"{self.name} is working.")
        print(f"Battery remaining: {self.battery}%")

robot1 = Robot("Atlas", 100)
robot2 = Robot("Nova", 50)

robot1.work()
robot2.work()
