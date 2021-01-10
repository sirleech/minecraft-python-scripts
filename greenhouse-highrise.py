from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

SonarNeedle = mc.getPlayerEntityId("SonarNeedle")
sirleech = mc.getPlayerEntityId("sirleech")
# replace with your player entity ID
x, y, z = mc.entity.getPos(sirleech)

#canopy size
size = 20
height = size/1

#offset from player
off = 0

#make multi-storey building
for b in range (0,3):
    #s = storey of building
    s = b * height
    #glass
    mc.setBlocks(x + off, y+s, z+ off, x+size, y+height+s, z+size, 20)
    #glowstone
    mc.setBlocks(x + off, y+s, z+ off, x+size, y+s, z+size, 138)
    #air
    mc.setBlocks(x+off+1, y+1+s, z+off+1, x+size-1, y+height+s-1, z+size-1, 0)
    #grass=2
    mc.setBlocks(x+off+1, y+1+s, z+off+1, x+size-1, y+1+s, z+size-1, 2)
    #saplings
    # 0: Oak
    # 1: Spruce
    # 2: Birch
    # 3: Jungle (Not on Pi)
    trunk = 12
    mid = size/2
    saplingType = random.randint(0, 3)
    mc.setBlocks(x+off+mid-(trunk/2),y+2+s,z+off+mid-(trunk/2),x+off+trunk,y+2+s,z+off+trunk, 6, saplingType)
