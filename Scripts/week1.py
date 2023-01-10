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
                      subdivisionsZ=2, axis=(0, 1, 0), createUVs=False, constructionHistory=False)
# Create, then Move
mc.move("25cm", "0cm", "0cm", myCube2)

# Rotate
# rotate -r -os -fo -52.77125 10.221411 -51.780312 ;
mc.rotate(90, 125, 0, myCube2,  absolute=True, centerPivot=True,
          deletePriorHistory=True, translate=False)
# Rename Object
mc.select(myCube2, replace=True)
mc.rename("NewName")
