import pybullet as p
import time
import pybullet_data

# Connect to the graphical physics server (GUI mode)
physicsClient = p.connect(p.GUI)

# Set the data path to load default assets (like planes and robots)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity and load a simple floor plane and robot
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# Run a brief simulation loop
for i in range(500):
    p.stepSimulation()
    time.sleep(1.0 / 240.0)

p.disconnect()
print("PyBullet test completed successfully!")