# import the Ev3 python bindings
import ev3dev.ev3 as ev3

#color dictioniary (key value pair)
dcolor = {
          0:'No color',
          1:'black',
          2:'blue',
          3:'green',
          4:'yellow',
          5:'red',
          6:'white',
          7:'brown'
          }

#connect medium motor on motorport A (chk if connected, if not throw error)
m = ev3.MediumMotor('outA'); assert m.connected

#connect touch and color sensor (chk if connected, if not throw error) 
tch = ev3.TouchSensor();    assert tch.connected
cols = ev3.ColorSensor();   assert cols.connected

#set color sensor mode in color sense mode
#cols.mode = 'COL_COLOR'

#loop until Touch sensor is pressed
while not tch.value():
    #get value for motorspeed and multiply by 10
    speed = cols.value()*10
    #set motor speed depending on the color
    m.run_forever(duty_cycle_sp=speed)
    # get color value from dictionary and print
    print dcolor[cols.value()]

print "i am out of the loop "
