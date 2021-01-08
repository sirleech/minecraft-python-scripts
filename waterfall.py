from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)


x, y, z = mc.player.getPos()
size = 3
mc.setBlocks(x+1, y, z+1, x+size, y-size*5, z+size, 8)