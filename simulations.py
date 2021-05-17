from Robot import Robot

obj = Robot()
print("Your new robot has moved CMS: ", obj.distaceTraveledCms)
# obj.leftMotor.run(200)
# obj.runTopMotors(300, 90)
obj.driveForward(400, 120)
print("Now your robot has moved CMS: ", obj.distaceTraveledCms)