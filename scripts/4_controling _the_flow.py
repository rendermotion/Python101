objects_list = ['L_main_arm_ctrl', 'R_main_arm_ctrl', 'L_main_leg_ctrl', 'R_main_leg_ctrl',
                'C_main00_spine_ctrl', 'C_main01_spine_ctrl', 'C_main02_spine_ctrl', 'C_main03_spine_ctrl']

string_object = 'L_main_leg_ctrl'

sting_selection = 'L_main_arm_CTRL'

# comparison operators
# == <= >= != >  <
# print(35 != 36)
#
print(not string_object in objects_list)
print ('main' in 'R_main_arm_ctrl')
# the if statement
variable='R_arm_ctrl'
if 'main' in variable:
    print('main is inside string')
elif 'arm' in variable:
    print('arm is inside string')
else:
    print('my name')

# print('hello world')

for each in objects_list:
    print(each)

for each in range(20):
    print(each)

import pymel.core as pm

for each in range(10):
    transform, prop = pm.polyCube()
    transform.translateX.set(each)
    prop.height.set(each + 1)

