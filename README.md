# maya-control-creator
A control creator for rigging in Autodesk Maya. 

## Running the script
1. Past both these files into the Maya scripts folder
2. Run the following into Mayas python editor:
```python
from maya_control_creator import *
controlCreator = MayaControlCreator()
controlCreator.buildUI()
```

## TODO: List
- [x] Create more 2D control shapes
- [x] Create more 3D control shapes
- [x] Set UI width wider (width+20)
- [x] Set height value to 850
- [x] Control Parent to joint button
- [ ] Create Attributes doesn't work with custom control name
- [ ] Show attribute button should unlock control
- [ ] Transform, rotation and scale tools should unlock control if locked
- [ ] Delete history/freeze transforms should ignore the error
- [ ] Transform, rotation, scale should ignore error if control is locked
- [ ] Add decision if name is empty, don't add underscore
- [x] Add for loop to work with multiple joints
- [x] Square control doesn't take chosen name from naming textfields
- [x] Control position gets joints position from parent not world
- [x] Joints don't spawn if nothing is selected. Should spawn at 0, 0, 0
- [ ] Add dropdown box for rotation, translate
- [x] Add floatslider for scale
- [x] Reverse rotation options
