from mcpi.minecraft import Minecraft

mc = Minecraft.create()

Sirleech = mc.getPlayerEntityId("sirleech")
SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
mc.entity.setPos(SonarNeedle,mc.entity.getPos(Sirleech))
