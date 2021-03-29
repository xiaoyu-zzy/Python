import pynput

ctr = pynput.mouse.Controller()

_click = False
def on_press(key):
    global _click
    try:
        if bool(_click) == True:
            if str(key.char) == 'z':
                ctr.click(pynput.mouse.Button.left, 2)
            elif str(key.char) == 'x':
                ctr.click(pynput.mouse.Button.right)
    except:
        pass

def on_release(key):
    global _click
    try:
        if key == pynput.keyboard.Key.ctrl_l:
            if bool(_click) == True:
                print('off')
                _click = False
        if key == pynput.keyboard.Key.ctrl_r:
            if bool(_click) == False:
                print('on')
                _click = True
    except:
        pass

with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
