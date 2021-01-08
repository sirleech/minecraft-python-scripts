from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.postToChat("teleporting...")
x, y, z = mc.player.getPos()
entityIds = mc.getPlayerEntityIds()
print entityIds
#print mc.entity.getPos(entityIds[0])
#mc.player.setPos(17949,mc.player.getPos())