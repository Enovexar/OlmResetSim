#resetSim function
from random import randint

def resetSim(hand, weapon, attempts, fails):
	speed = weapon.speed
	maxHit = weapon.max
	accTarget = weapon.accuracy*1000
#simulate x times with breaking if hand dies, and incrementing fails if ticks run out
	for x in range(attempts):
		hitpoints = hand.hp
		timeLeft = hand.resetTime
		while timeLeft > 0:
			accRoll = randint(1,1000)
			if accRoll < accTarget:
				dmg = randint(0,maxHit)
				#print("Damage:",dmg)
				hitpoints = hitpoints - dmg
			timeLeft = timeLeft - speed
			if hitpoints < 1:
				break

		if hitpoints > 0:
			fails += 1
	return fails