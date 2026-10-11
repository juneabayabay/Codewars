class Instrument:
  def play(self):
    print()

class Guitar(Instrument):
  def play(self):
    print("This is for leading")

class Piano():
  def play(self):
    print("This is for mid tone")

class Drum:
   def play(self):
      print("Best for metronome ")

g = Guitar()
p = Piano()
d = Drum()

ins = [g, p, d]

for instrumentals in ins:
    instrumentals.play()

