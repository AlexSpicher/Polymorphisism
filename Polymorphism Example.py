class Instrument:
    def type(self):
        return "Each instrument has its own classification"
class Trumpet(Instrument):
    def type(self):
        return "The trumpet is a brass instrument"
class Flute(Instrument):
    def type(self):
        return "The flute is a woodwind instrument"
class Piano(Instrument):
    def type(self):
        return "The Piano is a percussion instrument"
def display_type(instrument):
    return instrument.type()
trumpet = Trumpet()
flute = Flute()
piano = Piano()

print(display_type(trumpet))
print(display_type(flute))
print(display_type(piano))