from pynput import keyboard
import mujoco
import mujoco_viewer
import time

model = mujoco.MjModel.from_xml_path('Long_Manipulator.xml')
data = mujoco.MjData(model)
ctrl = data.ctrl
viewer = mujoco_viewer.MujocoViewer(model, data)

activation = [0.0, 0.0]

key_state = {'k': False, 'l': False}

def on_press(key):
    try:
        if key.char in key_state:
            key_state[key.char] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in key_state:
            key_state[key.char] = False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    for i, keys in enumerate([['k'], ['l']]):
        if any(key_state[k] for k in keys):
            activation[i] = min(activation[i] + 0.1, 1.0)
            print(f"ctrl: {ctrl[:]}")

        else:
            activation[i] = max(activation[i] - 0.1, 0.0)
            print(f"ctrl: {ctrl[:]}")


    ctrl[0], ctrl[1] = activation
    mujoco.mj_step(model, data)
    viewer.render()
    time.sleep(0.0001)
    
