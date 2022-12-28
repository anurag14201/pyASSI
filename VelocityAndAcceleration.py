u = int(input("Initial Velocity :"))
v = int(input("Final Velocity :"))
t = int(input("Time :"))

initialVelocity = u
finalVelocity = v
time = t

acceleration = (finalVelocity - initialVelocity) / time
print("Acceleration = ", acceleration)
