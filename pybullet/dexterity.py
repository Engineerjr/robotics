import pybullet as p
import pybullet_data
import time

def run_dexterity_simulation():
    # 1. Connect to the PyBullet physics server in GUI mode
    physicsClient = p.connect(p.GUI)
    
    # 2. Set the search path to access built-in PyBullet assets (URDFs)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    
    # 3. Configure gravity and camera view for a better perspective
    p.setGravity(0, 0, -9.81)
    p.resetDebugVisualizerCamera(
        cameraDistance=1.2, 
        cameraYaw=50, 
        cameraPitch=-35, 
        cameraTargetPosition=[0.4, 0, 0.1]
    )

    # 4. Load ground plane and the robot (using Franka Panda arm with a gripper)
    planeId = p.loadURDF("plane.urdf")
    
    # Initial position and orientation of the robot base
    robot_start_pos = [0, 0, 0]
    robot_start_orientation = p.getQuaternionFromEuler([0, 0, 0])
    robotId = p.loadURDF("franka_panda/panda.urdf", robot_start_pos, robot_start_orientation, useFixedBase=True)

    # 5. Load a small target object (e.g., a small cube) within the robot's workspace
    cube_start_pos = [0.5, 0.0, 0.05]
    cube_start_orientation = p.getQuaternionFromEuler([0, 0, 0])
    boxId = p.loadURDF("cube.urdf", cube_start_pos, cube_start_orientation, globalScaling=0.04)

    # Disable real-time simulation to manually step through physics calculations
    p.setRealTimeSimulation(0)

    print("Starting simulation loop...")
    
    # 6. Simulation control loop
    for step in range(1000):
        # Example trajectory / control strategy:
        # Franka Panda has 7 arm joints and 2 finger joints (indices 0 to 8)
        
        if step < 200:
            # Phase 1: Move arm towards the cube and open fingers
            target_positions = [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785, 0.04, 0.04]
        elif step < 500:
            # Phase 2: Lower the arm closer to the cube
            target_positions = [0.0, -0.4, 0.0, -2.0, 0.0, 1.6, 0.785, 0.04, 0.04]
        elif step < 700:
            # Phase 3: Close the fingers to grasp the object
            target_positions = [0.0, -0.4, 0.0, -2.0, 0.0, 1.6, 0.785, 0.00, 0.00]
        else:
            # Phase 4: Lift the object up
            target_positions = [0.0, -0.8, 0.0, -2.2, 0.0, 1.8, 0.785, 0.00, 0.00]

        # Apply position control commands to each joint
        for joint_idx, target_pos in enumerate(target_positions):
            p.setJointMotorControl2(
                bodyUniqueId=robotId,
                jointIndex=joint_idx,
                controlMode=p.POSITION_CONTROL,
                targetPosition=target_pos,
                force=200.0,       # Maximum motor force / torque limit
                maxVelocity=1.0
            )

        # Step the physics simulation forward
        p.stepSimulation()
        time.sleep(1.0 / 240.0) # Maintain real-time sync (240 Hz)

    # Disconnect simulation
    p.disconnect()

if __name__ == "__main__":
    run_dexterity_simulation()