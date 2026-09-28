def information(**details):
    for key, value in details.items():
        print(key, ":", value)

information(name="John", age=20, city="Manila")
