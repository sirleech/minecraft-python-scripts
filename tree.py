from mcpi.minecraft import Minecraft

mc = Minecraft.create()

SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
sirleech = mc.getPlayerEntityId("sirleech")
x, y, z = mc.entity.getPos(SonarNeedle)

#canopy
size = 10
#offset
off = 2
mc.setBlocks(x + off, y, z+ off, x+size, y+size/2, z+size, 18)

#trunk
mid = size/2
mc.setBlocks(x+off+mid , y, z+off+mid, x+mid+off+2, y-50, z+mid+off+2, 17)
