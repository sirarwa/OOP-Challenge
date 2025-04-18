# import the Pet class from the Pet module.
from Pet import Pet

# Create an instance of the Pet class.
# The instance is created with the name "Kenan" and specified values.
kenan_pet = Pet("Kenan", hunger=1, energy=3, happiness=0)

# Call the eat method
kenan_pet.eat()
# Call the sleep method
kenan_pet.sleep()
# Call the play method
kenan_pet.play()
# Call the get_status method
kenan_pet.get_status()