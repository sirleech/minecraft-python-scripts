from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")

Sirleech = mc.getPlayerEntityId("sirleech")
SonarNeedle = mc.getPlayerEntityId("SonarNeedle")

x, y, z = mc.entity.getPos(SonarNeedle)
#x, y, z = mc.player.getPos()

length = 8
width = 16
height = 8

#FISH TANK
#glass = 20
mc.setBlocks(x, y, z, x+length, y+height, z+width, 20)

#air
mc.setBlocks(x+1, y+1, z+1, x+(length-2), y+height, z+(width-2), 0)

# tnt
#mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, 46, 1)
