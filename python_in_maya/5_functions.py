# Some pymel basic functions.
import pymel.core as pm

creations = pm.ls('polyCube*')
transforms = pm.ls('pCube*', type='transform')

print(pm.objectType(creations[0]), '\n')

for index, (pcube, transform) in enumerate(zip(creations, transforms)):
    pcube.width.set(5)
    transform.translateY.set(index)
    transform.translateZ.set(-index)



import pymel.core as pm
def stairs(steps):
    for index  in range(steps):
        transform, pcube = pm.polyCube()
        pcube.width.set(5)
        transform.translateY.set(index)
        transform.translateZ.set(-index)

# 3 nested fors
import pymel.core as pm
steps = 10
for index_y  in range(steps):
    for index_z in range(steps):
        for index_x in range(steps):
            transform, pcube = pm.polyCube()
            pcube.width.set(.8)
            pcube.height.set(.8)
            pcube.depth.set(.8)
            transform.translateY.set(index_y)
            transform.translateZ.set(index_z)
            transform.translateX.set(index_x)