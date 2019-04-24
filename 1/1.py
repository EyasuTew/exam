import _bpy
import bpy
import os
for ob in bpy.context.scene.objects:
    print("object name:  ", ob.data.name)
    l=ob.location
    print(l)