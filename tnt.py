from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")

Sirleech = mc.getPlayerEntityId("sirleech")
SonarNeedle = mc.getPlayerEntityId("SonarNeedle")

x, y, z = mc.entity.getPos(SonarNeedle)
#x, y, z = mc.player.getPos()

length = 8
width = 8
height = 8

# tnt
mc.setBlocks(x+1, y+1, z+1, x+width, y+height, z+length, 46, 1)
