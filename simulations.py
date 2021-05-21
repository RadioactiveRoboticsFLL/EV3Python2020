from Robot import Robot

obj = Robot()
obj.currentPosition = (43, 8)
obj.currentRotation = 0
print("Your new robot has moved CMS: ", obj.distaceTraveledCms)
# obj.leftMotor.run(200)
# obj.runTopMotors(300, 90)
obj.driveForward(400, 120)
print("Now your robot has moved CMS: ", obj.distaceTraveledCms)
print("Our new position is: ")
# newX = obj.currentPosition[0] + obj.distaceTraveledCms
# newY = obj.currentPosition[1] + 0
# print(newX, newY)
print(obj.currentPosition)
obj.driveForward(500, 360)
print(obj.currentPosition)
obj.SpinLeftAngularDistance(600, 90)
obj.driveForward(500, 360)
print(obj.currentPosition)
print("ALL positions: ")
print(obj.oldPositions)