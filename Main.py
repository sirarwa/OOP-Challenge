#import the Pet class from the Pet module.
from Pet import Pet
# Create an instance of the Pet class.
# The instance is created with the name "Kenan" and default values for hunger, energy, and happiness.
Pet= Pet("Kenan", hunger=17, energy=3, happiness=0)
# Create an instance of the Pet class
Pet.eat()
# Call the eat method
Pet.sleep() 
# Call the sleep method
Pet.play()
# Call the play method
Pet.get_status()
