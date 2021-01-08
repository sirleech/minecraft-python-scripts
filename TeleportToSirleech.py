#!/usr/bin/python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

Brooklyn = mc.getPlayerEntityId("sirleech")
Chris = mc.getPlayerEntityId("SonarNeedle")
mc.entity.setPos(Chris,mc.entity.getPos(Brooklyn))
