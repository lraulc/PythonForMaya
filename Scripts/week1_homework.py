from maya import cmds as mc

# Body
body_name = "Body"
body = mc.polySphere(name=body_name, constructionHistory=False)
mc.xform(body[0], worldSpace=True, scale=(15, 15, 15))
mc.xform(body[0], worldSpace=True, translation=(0, 25, 0))

# Torso
torso_name = "Torso"
torso = mc.polyCylinder(name=torso_name, constructionHistory=False)
mc.xform(torso[0], worldSpace=True, scale=(14, 5, 14))
mc.xform(torso[0], worldSpace=True, translation=(0, 35, 0))

# Head
head_name = "Head"
head = mc.polySphere(name=head_name, constructionHistory=False)
head_scale = 10
mc.xform(head[0], worldSpace=True, scale=(
    head_scale, head_scale, head_scale))
mc.xform(head[0], worldSpace=True, translation=(0, 45, 0))

# Hat
hat_name = "Hat"
hat = mc.polyCylinder(name=hat_name, constructionHistory=False)
mc.xform(hat[0], worldSpace=True, translation=(0, 55, 0))
mc.xform(hat[0], worldSpace=True, scale=(11, 2, 11))

############################## Shoulders Start #################################

# Left Shoulder
left_shoulder_name = "LeftShoulder"
left_shoulder = mc.polyCube(name=left_shoulder_name, constructionHistory=False)
mc.xform(left_shoulder[0], worldSpace=True, translation=(-15, 34, 0))
mc.xform(left_shoulder[0], worldSpace=True, scale=(5, 9, 5))
# Right Shoulder
right_shoulder_name = "RightShoulder"
right_shoulder = mc.polyCube(
    name=right_shoulder_name, constructionHistory=False)
mc.xform(right_shoulder[0], worldSpace=True, translation=(15, 34, 0))
mc.xform(right_shoulder[0], worldSpace=True, scale=(5, 9, 5))

# Combines shoulders into single Shoulder piece and assigns new name
shoulders_name = "Shoulders"
shoulders = mc.polyUnite(right_shoulder, left_shoulder,
                         centerPivot=True, name=shoulders_name)
# Delete breadcrumbs after combining
mc.delete([left_shoulder_name, right_shoulder_name],
          inputConnectionsAndNodes=False)
# Select merged asset and assign default lambert
mc.select(shoulders[0])
mc.hyperShade(assign="lambert1")

############################## Shoulders End #################################

############################## Arms Start #################################
# Left Arm
left_arm_name = "LeftArm"
left_arm = mc.polyCube(name=left_arm_name, constructionHistory=False)
mc.xform(left_arm[0], worldSpace=True, translation=(-15, 30, 4))
mc.xform(left_arm[0], worldSpace=True, scale=(5, 5, 15))

# Right Arm
right_arm_name = "RightArm"
right_arm = mc.polyCube(
    name=right_arm_name, constructionHistory=False)
mc.xform(right_arm[0], worldSpace=True, translation=(15, 30, 4))
mc.xform(right_arm[0], worldSpace=True, scale=(5, 5, 15))

############################## Arms End #################################

############################## Hands Start #################################
# Left hand
left_hand_name = "LeftHand"
left_hand = mc.polyCube(name=left_hand_name, constructionHistory=False)
mc.xform(left_hand[0], worldSpace=True, translation=(-15, 30, 12))
mc.xform(left_hand[0], worldSpace=True, scale=(3, 3, 3))

# Right hand
right_hand_name = "RightHand"
right_hand = mc.polyCube(
    name=right_hand_name, constructionHistory=False)
mc.xform(right_hand[0], worldSpace=True, translation=(15, 30, 12))
mc.xform(right_hand[0], worldSpace=True, scale=(3, 3, 3))

############################## Hands End #################################

############################## Legs Start #################################

# Left Hip
left_hip_name = "LeftHip"
left_hip_group = mc.polyCylinder(name=left_hip_name, constructionHistory=False)
left_hip = left_hip_group[0]
mc.xform(left_hip, worldSpace=True, scale=(5, 2, 5))
mc.xform(left_hip, worldSpace=True, translation=(9, 13, 0))
mc.xform(left_hip, worldSpace=True, euler=True, rotation=(0, 45, 45))

# Left Shin
left_shin_name = "LeftShin"
left_shin_group = mc.polyCylinder(
    name=left_shin_name, constructionHistory=False)
left_shin = left_shin_group[0]
mc.xform(left_shin, worldSpace=True, scale=(2, 1, 2))
mc.xform(left_shin, worldSpace=True, translation=(10, 11, 0))
mc.xform(left_shin, worldSpace=True, euler=True, rotation=(0, 45, 45))


# Left Leg
left_leg_name = "LeftLeg"
left_leg_group = mc.polyCylinder(
    name=left_leg_name, constructionHistory=False)
left_leg = left_leg_group[0]
mc.xform(left_leg, worldSpace=True, scale=(1, 10, 1))
mc.xform(left_leg, worldSpace=True, translation=(10, 11, 0))
mc.xform(left_leg, worldSpace=True, euler=True, rotation=(0, 45, 45))

# Left foot
left_foot_name = "LeftFoot"
left_foot_group = mc.polySphere(
    name=left_foot_name, constructionHistory=False)
left_foot = left_foot_group[0]
mc.xform(left_foot, worldSpace=True, scale=(3, 3, 3))
mc.xform(left_foot, worldSpace=True, translation=(17, 4, 0))
mc.xform(left_foot, worldSpace=True, euler=True, rotation=(0, 45, 45))

# Right Hip
right_hip_name = "RightHip"
right_hip_group = mc.polyCylinder(
    name=right_hip_name, constructionHistory=False)
right_hip = right_hip_group[0]
mc.xform(right_hip, worldSpace=True, scale=(5, 2, 5))
mc.xform(right_hip, worldSpace=True, translation=(-9, 13, 0))
mc.xform(right_hip, worldSpace=True, euler=True, rotation=(0, 45, -45))

# Right Shin
right_shin_name = "RightShin"
right_shin_group = mc.polyCylinder(
    name=right_shin_name, constructionHistory=False)
right_shin = right_shin_group[0]
mc.xform(right_shin, worldSpace=True, scale=(2, 1, 2))
mc.xform(right_shin, worldSpace=True, translation=(-10, 11, 0))
mc.xform(right_shin, worldSpace=True, euler=True, rotation=(0, 45, -45))

# Right Leg
right_leg_name = "RightLeg"
right_leg_group = mc.polyCylinder(
    name=right_leg_name, constructionHistory=False)
right_leg = right_leg_group[0]
mc.xform(right_leg, worldSpace=True, scale=(1, 10, 1))
mc.xform(right_leg, worldSpace=True, translation=(-10, 11, 0))
mc.xform(right_leg, worldSpace=True, euler=True, rotation=(0, 45, -45))

# Right foot
right_foot_name = "RightFoot"
right_foot_group = mc.polySphere(
    name=right_foot_name, constructionHistory=False)
right_foot = right_foot_group[0]
mc.xform(right_foot, worldSpace=True, scale=(3, 3, 3))
mc.xform(right_foot, worldSpace=True, translation=(-17, 4, 0))
mc.xform(right_foot, worldSpace=True, euler=True, rotation=(0, 45, -45))

############################## Legs End #################################

# Clear Selection after creationg
mc.select(deselect=True)
