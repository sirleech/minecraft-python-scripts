from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# level = world
# # # # # # # #
# home
SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
mc.entity.setPos(SonarNeedle,-200.32,33.0,-370.72)

# lava home
Sirleech = mc.getPlayerEntityId("sirleech")
mc.entity.setPos(Sirleech,-157.824659,35.0,-372.25975)
