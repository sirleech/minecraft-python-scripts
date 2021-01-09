from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getPos()
size = 20
mc.setBlocks(x+1, y+1, z+1, x+size, y-size/1.3, z+size, 0)
