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

#fat trunk
trunk = 12
mid = size/2
mc.setBlocks(x+off+mid-(trunk/2),y,z+off+mid-(trunk/2),x+off+trunk,y-50,z+off+trunk, 17)
