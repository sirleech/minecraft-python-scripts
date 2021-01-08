#!/usr/bin/python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

Chris = mc.getPlayerEntityId("SonarNeedle")
# level = world
mc.entity.setPos(Chris,-200.32,33.0,-370.72)

Brooklyn = mc.getPlayerEntityId("sirleech")
# mc.entity.setPos(Brooklyn,-200.32,33.0,-370.72)
