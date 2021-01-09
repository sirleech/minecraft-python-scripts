from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")
#x, y, z = mc.player.getPos()
Sirleech = mc.getPlayerEntityId("sirleech")
x, y, z = mc.entity.getPos(Sirleech)

size = 5
mc.setBlocks(x+1, y+1, z+1, x+size*10, y+size, z+size, 0)
