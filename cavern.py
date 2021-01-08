from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)


x, y, z = mc.player.getPos()
size = 10
mc.setBlocks(x+1, y+1, z+1, x+size*5, y+size*5, z+size*5, 0)