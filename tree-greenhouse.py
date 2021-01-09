from mcpi.minecraft import Minecraft

mc = Minecraft.create()

SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
# sirleech = mc.getPlayerEntityId("sirleech")
# replace with your player entity ID
x, y, z = mc.entity.getPos(SonarNeedle)

#canopy size
size = 20
height = size/1

#offset from player
off = 0
#glass
mc.setBlocks(x + off, y, z+ off, x+size, y+height, z+size, 20)
#glowstone
mc.setBlocks(x + off, y, z+ off, x+size, y, z+size, 138)
#air
mc.setBlocks(x+off+1, y+1, z+off+1, x+size-1, y+height-1, z+size-1, 0)
#grass=2
mc.setBlocks(x+off+1, y+1, z+off+1, x+size-1, y+1, z+size-1, 2)
#saplings
trunk = 12
mid = size/2
mc.setBlocks(x+off+mid-(trunk/2),y+2,z+off+mid-(trunk/2),x+off+trunk,y+2,z+off+trunk, 6)
