from mcpi.minecraft import Minecraft

mc = Minecraft.create()

SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
sirleech = mc.getPlayerEntityId("sirleech")
# replace with your player entity ID
x, y, z = mc.entity.getPos(sirleech)

#canopy size
size = 20

#offset from player
off = 2
mc.setBlocks(x + off, y, z+ off, x+size, y+size/2, z+size, 18)

#glassfloor so leaves don't fall
mc.setBlocks(x + off, y, z+ off, x+size, y, z+size, 20)

#trunk
trunk = 4
mid = size/2
mc.setBlocks(x+off+mid , y, z+off+mid, x+mid+off+trunk, y-50, z+mid+off+trunk, 17)
