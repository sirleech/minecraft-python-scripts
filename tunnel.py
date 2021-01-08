from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)


x, y, z = mc.player.getPos()
size = 5
mc.setBlocks(x+1, y+1, z+1, x+size*10, y+size, z+size, 0)