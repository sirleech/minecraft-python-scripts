from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")

Sirleech = mc.getPlayerEntityId("sirleech")
SonarNeedle = mc.getPlayerEntityId("SonarNeedle")

x, y, z = mc.entity.getPos(Sirleech)
#x, y, z = mc.player.getPos()

factor = 2

length = 16 * factor
width = 8 * factor
height = 8 * factor

#FISH TANK
#glass = 20
mc.setBlocks(x, y, z, x+length, y+height, z+width, 20)

# cut out the inside
mc.setBlocks(x+1, y+1, z+1, x+length-1, y+height, z+width-1, 8)

#sand
mc.setBlocks(x+1, y+1, z+1, x+length-1, y+3, z+width-1, 12)
