from maya import cmds as mc

# To run code in Maya - Select Line and Right click, send to maya

# pyramid = mc.polyPyramid(name="myPyramid")


# # select -r pPyramid1 ;
# # move -r -os -wd 0 0 8.546087 ;
# mc.select(pyramid)
# mc.move("25cm", "0cm", "0cm")


# myCube = mc.polyCube(width=5, height=2, depth=0.5, name='MyCube', subdivisionsX=10, subdivisionsY=6,
#                      subdivisionsZ=2, axis=(0, 1, 0), createUVs=False, constructionHistory=True)

# Construction History = INPUT
wallName = "Boxey"
myCube2 = mc.polyCube(width=5, height=2, depth=0.5, name=wallName, subdivisionsX=10, subdivisionsY=6,
                      subdivisionsZ=2, axis=(0, 1, 0), createUVs=False)
# Create, then Move
mc.move("25cm", "0cm", "0cm", myCube2)

# # Rotate
# rotate - r - os - fo - 52.77125 10.221411 - 51.780312 = MEL
mc.rotate(90, 125, 0, myCube2,  absolute=True, centerPivot=True,
          deletePriorHistory=True, translate=False)
# # Rename Object
mc.select(myCube2, replace=True)
mc.rename("NewName")

width1 = mc.polyCube("NewName", q=True, width=True)


myCube3 = mc.polyCube(name="cubey")
mc.move(5, 0, 0, myCube3[0], relative=True,
        objectSpace=True, worldSpaceDistance=True)
mc.rotate(45, 10, 3, myCube3[0], absolute=True)

# Use Query to store flags as variables = Example - Width
# Query = Get - Flag = q
width = mc.polyCube(myCube3[0], q=True, width=True)
# Edit = Set - Flag = e
mc.polyCube(myCube3[0], e=True, width=5.34)

# Dont access using string, because it will only look up for the one with the name
myCube4 = mc.polyCube(name="cubey", constructionHistory=False)
mc.move(5, 0, 0, "cubey", relative=True,
        objectSpace=True, worldSpaceDistance=True)
mc.rotate(45, 10, 3, "cubey", absolute=True)


# Get ATTR
# Get attribute of an object
mc.getAttr(myCube3[0] + ".rz")
mc.polyCube(myCube3[0], q=True, width=True)
# To Get some attributes that are not in a transform, they must be taken from the second node, not from the transform
mc.getAttr(myCube3[1] + ".width")


######### TRANSFORMS ###############

# Additive = When using "relative" space it will add to the previous value
# Override = When using "World" space it will add to the previous value

# Relative vs Worlspace transform
mc.xform(myCube3[0], worldSpace=True, translation=(
    5, 5, 5))  # Will not add aditional units
mc.xform(myCube3[0], relative=True, translation=(5, 5, 5))  # Additive

# Get translation in worldspace(ws=) or relative(r=) and store it in "position variable (list)"
position = mc.xform(myCube3[0], worldSpace=True, translation=True, q=True)
print(f"{myCube3[0]} position : {position}")

# Set rotation relative or ws - Euler
mc.xform(myCube3[0], euler=True, rotation=(45, 45, 45))  # Override
mc.xform(myCube3[0], relative=True, euler=True,
         rotation=(45, 90, 120))  # Additive
