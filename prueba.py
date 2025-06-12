# simulate.py
import time, pybullet as p, pybullet_data

client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
p.loadURDF("cube.urdf",[0,0,0.5])
for _ in range(240):
    p.stepSimulation()
    time.sleep(1/240)
p.disconnect()
