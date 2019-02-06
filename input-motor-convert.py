# Learning how to normalize the analog inputs to my motor control

xMax = 0
xMin = 1024

yMax = 0
yMin = 1024

def convertInputsToMotorInstructions(x, y, minVal, maxVal):
  # Reverse values because inputs start 0,0 in the top right, and max out in the bottom right of the coordinate plane
  y = maxVal - y
  x = maxVal - x

  # Calculate center
  center = (maxVal - minVal) / 2

  deltaX = (center - x) * 2
  deltaY = (center - y) * 2

  print(str(deltaX) + ', ' + str(deltaY))

  leftSpeed = deltaX - deltaY
  rightSpeed = -deltaX - deltaY

  print('Left Speed: ' + str(leftSpeed))
  # print('Left Forward: ' + str(leftForward))

  print('Right Speed: ' + str(rightSpeed))
  # print('Right Forward: ' + str(rightForward))

convertInputsToMotorInstructions(128, 256, 0, 256)

# print('Straight Ahead')
# convertInputsToMotorInstructions(128, 0, 0, 256)
# print('')

# print('Straight Back')
# convertInputsToMotorInstructions(128, 256, 0, 256)
# print('')

# print('Rotate Left')
# convertInputsToMotorInstructions(0, 128, 0, 256)
# print('')

# print('Rotate Right')
# convertInputsToMotorInstructions(256, 128, 0, 256)
# print('')