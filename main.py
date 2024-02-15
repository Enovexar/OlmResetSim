#Olm Hand Reset Simulator
#check odds of failing to kill 2nd hand before reset occurs
#I think hands reset after 36 ticks, but don't know if killing 2nd hand on tick 36 will fail
#could adjust reset time to 34 or so to account for this

from resetSim import resetSim

fails = 0
attempts = 100000

class Weapon:
	def __init__(self, accuracy, maxHit, speed):
		self.speed = speed
		self.max = maxHit
		self.accuracy = accuracy

	def getSpeed(self):
		return self.attackSpeed

	def getMax(self):
		return self.max

class OlmHand:
	hp = 50
	resetTime = 36

mageHand = OlmHand()
meleeHand = OlmHand()
trident = Weapon(.8153,44,4)
lance = Weapon(.9,52,4)

print("\n\tTesting fail rate of toxic trident:\n")
fails = resetSim(mageHand, trident, attempts, fails)
print("\tFails:",fails)
print("\tAttempts:",attempts)
failRate = (fails/attempts)*100
results = "\tBased on {} attempts, the reset chance was {:.2f}%."
print(results.format(attempts,failRate))
