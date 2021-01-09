from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# Chris = mc.getPlayerEntityId("SonarNeedle")
# x, y, z = mc.entity.getPos(Chris)
x, y, z = mc.player.getPos()

#canopy
size = 25
mc.setBlocks(x+1, y+1, z+1, x+size, y+size/2, z+size, 18)

#trunk
size = 3
mc.setBlocks(x+size, y, z+size, x-size, y-size*30, z-size, 17)
