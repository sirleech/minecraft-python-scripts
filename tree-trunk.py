from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("Hello world")
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)


# x, y, z = mc.player.getPos()
Chris = mc.getPlayerEntityId("SonarNeedle")
x, y, z = mc.entity.getPos(Chris)
size = 4
mc.setBlocks(x+1, y+5, z+1, x+size, y-size*20, z+size, 17)