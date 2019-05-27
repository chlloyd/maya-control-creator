# Version 0.3

import maya.cmds as cmds
from constants import *


class MayaControlCreator(object):
    def __init__(self):
        self.window = "controlcreator"
        self.title = "Rigging Control Creator"
        self.size = (width + 20, height)

    def buildUI(self):
        """Creates the user interface

        Returns:User interface.

        """
        if cmds.window(self.window, exists=True):
            self.close()

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)

        # Creates a form layout to window
        cmds.rowColumnLayout(width=width)
        cmds.text(label="Instructions", align="center", font="boldLabelFont")
        cmds.text(label="Select the joint and press a control shape to create.", align="center")
        cmds.text(label="Naming", align="center", font="boldLabelFont")
        cmds.text(label="Use $OBJ to use selected joint name. ", align="center")
        cmds.rowColumnLayout(nc=3, cw=[(1, width / 3), (2, width / 3), (3, width / 3)])

        cmds.text(label="Prefix", align="center")
        cmds.text(label="Name", align="center")
        cmds.text(label="Suffix", align="center")

        self.prefix = cmds.textField("prefix")
        self.name = cmds.textField("name", text="$OBJ")
        self.suffix = cmds.textField("suffix")

        cmds.rowColumnLayout(width=width)
        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, width)])
        cmds.separator(style="in")
        cmds.text(label="Shapes", align="center", font="boldLabelFont")

        self.shapeoption = cmds.optionMenu(label="Shape", maxVisibleItems=13)
        cmds.menuItem(divider=True, dividerLabel="--3D Shapes--")
        cmds.menuItem(label="--2D Shapes--", enable=False)
        cmds.menuItem(label="Circle")
        cmds.menuItem(label="Square")
        cmds.menuItem(label="Triangle")
        cmds.menuItem(label="Plus")
        cmds.menuItem(label="Arrow")
        cmds.menuItem(divider=True, dividerLabel="--3D Shapes--")
        cmds.menuItem(label="--3D Shapes--", enable=False)
        cmds.menuItem(label="Sphere")
        cmds.menuItem(label="Cube")
        cmds.menuItem(label="Torus")
        cmds.menuItem(label="Cone")

        cmds.text(label="")
        cmds.button(label="Create", command=self.createshapebtn)

        cmds.separator(style="in")
        cmds.text(label="Translate", align="center", font="boldLabelFont")
        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, width)])
        cmds.floatSliderGrp(label="Translate X", field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.setpositionX, columnOffset2=[-50, 50])
        cmds.floatSliderGrp(label="Translate Y", field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.setpositionY)
        cmds.floatSliderGrp(label="Translate Z", field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.setpositionZ)

        cmds.separator(style="in")
        cmds.text(label="Rotation", align="center", font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, width / 3), (2, width / 3), (3, width / 3)])

        cmds.button(label="Rotate X 45", command=lambda unused: self.rotationX(45))
        cmds.button(label="Rotate Y 45", command=lambda unused: self.rotationY(45))
        cmds.button(label="Rotate Z 45", command=lambda unused: self.rotationZ(45))
        cmds.button(label="Rotate X 90", command=lambda unused: self.rotationX(90))
        cmds.button(label="Rotate Y 90", command=lambda unused: self.rotationY(90))
        cmds.button(label="Rotate Z 90", command=lambda unused: self.rotationZ(90))

        cmds.rowColumnLayout(width=width)
        cmds.separator(style="in")
        cmds.text(label="Scale", align="center", font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, width)])
        cmds.floatSliderGrp(label="Scale X", field=True, minValue=0.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=1, dragCommand=self.setscaleX, changeCommand=self.setscaleX)
        cmds.floatSliderGrp(label="Scale Y", field=True, minValue=0.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=1, dragCommand=self.setscaleY, changeCommand=self.setscaleY)
        cmds.floatSliderGrp(label="Scale Z", field=True, minValue=0.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=1, dragCommand=self.setscaleZ, changeCommand=self.setscaleZ)
        cmds.rowColumnLayout(width=width)

        cmds.separator(style="in")
        cmds.text(label="Delete History/Freeze Transformations", align="center", font="boldLabelFont")
        cmds.button(label="Apply", command=self.freezetransform)

        cmds.rowColumnLayout(width=width)
        cmds.separator(style="in")
        cmds.text(label="Colouring", align="center", font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, width / 3), (2, width / 3), (3, width / 3)])
        cmds.button(backgroundColor=[1.0, 0.0, 0.0], label="", command=self.changecolourFn(COLOUR_RED))
        cmds.button(backgroundColor=[0.0, 1.0, 0.0], label="", command=self.changecolourFn(COLOUR_GREEN))
        cmds.button(backgroundColor=[0.0, 0.0, 1.0], label="", command=self.changecolourFn(COLOUR_BLUE))
        cmds.button(backgroundColor=[1.0, 1.0, 0.0], label="", command=self.changecolourFn(COLOUR_YELLOW))
        cmds.button(backgroundColor=[0.0, 1.0, 1.0], label="", command=self.changecolourFn(COLOUR_TURQUOISE))
        cmds.button(backgroundColor=[1.0, 0.0, 1.0], label="", command=self.changecolourFn(COLOUR_PINK))
        cmds.button(backgroundColor=[1.0, 1.0, 1.0], label="", command=self.changecolourFn(COLOUR_WHITE))
        cmds.button(backgroundColor=[0.369, 0.369, 0.369], label="", command=self.changecolourFn(COLOUR_GREY))
        cmds.button(backgroundColor=[0.0, 0.0, 0.0], label="", command=self.changecolourFn(COLOUR_BLACK))
        cmds.rowColumnLayout(width=width)

        cmds.separator(style="in")
        cmds.text(label="")

        cmds.button(label="Close", command=self.close)
        cmds.rowColumnLayout(width=width)
        # Renders the final UI
        cmds.showWindow()

    def getobjectname(self):
        """Get the object name from selected objects

        Returns:
            A List of items selected.
        """
        return cmds.ls(selection=True)

    def namesplit(self, name):
        """Splits the name of an object by "_".

        Args:
            name: Name to be split.

        Returns:
            The split name.
        """
        name.split("_")
        return name

    def getobjecttype(self):
        """Gets the object type of selected item.

        Returns:
            The object type of the selection.
        """
        selected = cmds.ls(selection=True)
        return cmds.objectType(selected)

    def getobjectposition(self, objectname):
        """Gets the selected objects position.
        If no item is selected, object are spawned at the 0, 0, 0.
        If the selected item is a joint, the global position is returned.
        Args:
            objectname: The name of the object to get the position of.

        Returns:
            the position of the object as a list.
        """
        if objectname == "":
            position = [0.0, 0.0, 0.0]
        elif cmds.objectType(objectname) == "joint":
            # world position rather than object position
            position = cmds.xform(objectname, query=True, worldSpace=True, rotatePivot=True)
        else:
            position = cmds.getAttr(objectname + ".translate")
        return position

    def nurbname(self, name):
        """Creates the name of the spawned NURB shape.
        Gets the names wanted for the object from the UI. If "$OBJ" is used, it uses the name of the selected object instead.
        Args:
            name: Name of selected object.

        Returns:
            The name of the Nurb shape.
        """
        prefixName = cmds.textField(self.prefix, query=1, text=1)
        middleName = cmds.textField(self.name, query=1, text=1)
        suffixName = cmds.textField(self.suffix, query=1, text=1)
        if prefixName == "$OBJ":
            fullname = name + "_" + middleName + "_" + suffixName
        elif middleName == "$OBJ":
            fullname = prefixName + "_" + name + "_" + suffixName
        else:
            fullname = prefixName + "_" + middleName + "_" + name
        return fullname

    def createshapebtn(self, *args):
        """Creates the NURB shape using Variable from the constants file.
        The function can create Circles, Squares, Triangles, Pluses, Arrows, Spheres, Cubes, Torus, Cones.
        Args:
            *args:Ignored.

        Returns:
            None
        """
        shape = cmds.optionMenu(self.shapeoption, query=True, value=True).lower()
        all_objects = self.getobjectname()
        all_objects_attr = []
        for object in all_objects:
            cmds.select(object)
            object_attr_list = [shape, self.nurbname(object), self.getobjectposition(object), object]
            all_objects_attr.append(object_attr_list)
        for object in all_objects_attr:

            if object[0] == "circle":
                cmds.circle(normal=[0, 1, 0], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "square":
                cmds.curve(degree=SQUARE[0], point=SQUARE[1], knot=SQUARE[2], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "triangle":
                cmds.curve(degree=TRIANGLE[0], point=TRIANGLE[1], knot=TRIANGLE[2], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "plus":
                cmds.curve(degree=PLUS[0], point=PLUS[1], knot=PLUS[2], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "arrow":
                cmds.curve(degree=ARROW[0], point=ARROW[1], knot=ARROW[2], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "sphere":
                all_circles = []
                for i in range(0, 5):
                    current_circle = cmds.circle(normal=SPHERE[0], radius=SPHERE[1], name=object[1])
                    cmds.setAttr(current_circle[0] + ".ry", i * 45)
                    all_circles.append(current_circle[0])
                outer_circle = cmds.circle(normal=[0, 1, 0], radius=0.5)
                all_circles.append(outer_circle[0])
                cmds.select(all_circles)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.pickWalk(direction="down")
                cmds.select(all_circles[0], toggle=True)
                cmds.parent(relative=True, shape=True)
                cmds.delete(all_circles[1:])
                cmds.xform(all_circles[0], centerPivots=True)
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "cube":
                cmds.curve(degree=CUBE[0], point=CUBE[1], knot=CUBE[2], name=object[1])
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "torus":
                bottom_circle = cmds.circle(normal=[0, 1, 0], center=[0, -0.5, 0], name=object[1])
                top_circle = cmds.circle(normal=[0, 1, 0], center=[0, 0.5, 0], name=object[1])
                outer_circle = cmds.circle(normal=[0, 1, 0], radius=1.5, name=object[1])
                inner_circle = cmds.circle(normal=[0, 1, 0], radius=0.5, name=object[1])
                circle_position_list = [[-1, 0, 0], [-(sqrt(2) / 2), 0, (sqrt(2) / 2)], [0, 0, 1], [(sqrt(2) / 2), 0, (sqrt(2) / 2)], [1, 0, 0],
                                        [(sqrt(2) / 2), 0, -(sqrt(2) / 2)], [0, 0, -1], [-(sqrt(2) / 2), 0, -(sqrt(2) / 2)]]
                all_circles = [bottom_circle[0], top_circle[0], outer_circle[0], inner_circle[0]]
                for i in range(0, 8):
                    current_circle = cmds.circle(normal=[0, 0, 1], radius=0.5, name=object[1])
                    cmds.setAttr(current_circle[0] + ".translate", circle_position_list[i][0], circle_position_list[i][1], circle_position_list[i][2])
                    cmds.setAttr(current_circle[0] + ".ry", i * 45)
                    all_circles.append(current_circle[0])
                cmds.select(all_circles)
                cmds.makeIdentity(apply=True, t=True, r=True, s=True)
                cmds.pickWalk(direction="down")
                cmds.select(all_circles[0], toggle=True)
                cmds.parent(relative=True, shape=True)
                cmds.delete(all_circles[1:])
                cmds.xform(all_circles[0], centerPivots=True)
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            elif object[0] == "cone":
                cone = []
                circle = cmds.circle(normal=[0, 0.5, 0], name=object[1])
                lines = cmds.curve(degree=CONE[0], point=CONE[1], knot=CONE[2], name=object[1])
                cone.append(circle[0])
                cone.append(lines)
                cmds.select(cone)
                cmds.makeIdentity(apply=True, translate=True, rotate=True, scale=True)
                cmds.pickWalk(direction="down")
                cmds.select(cone[0], toggle=True)
                cmds.parent(relative=True, shape=True)
                cmds.delete(cone[1:])
                cmds.xform(cone[0], centerPivots=True)
                cmds.setAttr(object[1] + ".translate", object[2][0], object[2][1], object[2][2])
                cmds.select(object[1], object[3])
                self.parentconstrain()

            else:
                cmds.error("No Shape Selected")

    def setpositionX(self, value):
        """Sets the X position of the selected shape from the IntSlider.
        Args:
            value: The amount to move in the X direction.

        Returns:
            None
        """
        for object in self.getobjectname():
            self.breakparentconnections()
            cmds.setAttr(object + ".translateX", self.getobjectposition(object.split("_")[1])[0] + value)
            cmds.select(object, (object.split("_")[1]))
            self.parentconstrain()
            cmds.select(object)

    def setpositionY(self, value):
        """Sets the Y position of the selected shape from the IntSlider.
        Args:
            value: The amount to move in the Y direction.

        Returns:
            None
        """
        for object in self.getobjectname():
            self.breakparentconnections()
            cmds.setAttr(object + ".translateY", self.getobjectposition(object.split("_")[1])[0] + value)
            cmds.select(object, (object.split("_")[1]))
            self.parentconstrain()
            cmds.select(object)

    def setpositionZ(self, value):
        """Sets the Z position of the selected shape from the IntSlider.
        Args:
            value: The amount to move in the Z direction.

        Returns:
            None
        """
        for object in self.getobjectname():
            self.breakparentconnections()
            cmds.setAttr(object + ".translateZ", self.getobjectposition(object.split("_")[1])[0] + value)
            cmds.select(object, (object.split("_")[1]))
            self.parentconstrain()
            cmds.select(object)

    def getrotation(self, objectname):
        """Gets the rotation of the selected object.

        Args:
            objectname: Name of object to get rotation.

        Returns:
            A list with the objects rotation
        """
        return [cmds.getAttr(objectname + ".rotateX"),
                cmds.getAttr(objectname + ".rotateY"),
                cmds.getAttr(objectname + ".rotateZ")]

    def rotationX(self, amount):
        """Rotates all selected object by set amount in X direction.
        Set amount from pressed button.

        Args:
            amount: Pressed X button.

        Returns:
            None
        """
        for item in self.getobjectname():
            self.breakparentconnections()
            current_rot = self.getrotation(item)[0]
            new_rot = current_rot + amount
            cmds.setAttr(item + ".rotateX", new_rot)
            cmds.select(item, (item.split("_")[1]))
            self.parentconstrain()
            cmds.select(item)

    def rotationY(self, amount):
        """Rotates all selected object by set amount in Y direction.
        Set amount from pressed button.

        Args:
            amount: Pressed Y button.

        Returns:
            None
        """
        for item in self.getobjectname():
            self.breakparentconnections()
            current_rot = self.getrotation(item)[0]
            new_rot = current_rot + amount
            cmds.setAttr(item + ".rotateY", new_rot)
            cmds.select(item, (item.split("_")[1]))
            self.parentconstrain()
            cmds.select(item)

    def rotationZ(self, amount):
        """Rotates all selected object by set amount in Z direction.
        Set amount from pressed button.

        Args:
            amount: Pressed Z button.

        Returns:
            None
        """
        for item in self.getobjectname():
            self.breakparentconnections()
            current_rot = self.getrotation(item)[0]
            new_rot = current_rot + amount
            cmds.setAttr(item + ".rotateZ", new_rot)
            cmds.select(item, (item.split("_")[1]))
            self.parentconstrain()
            cmds.select(item)

    def setscaleX(self, value):
        """Sets the X scale from the selected object.

        Args:
            value:The amount to the scale the selected object.

        Returns:
            None
        """
        for object in self.getobjectname():
            cmds.setAttr(object + ".scaleX", value)

    def setscaleY(self, value):
        """Sets the Y scale from the selected object.

        Args:
            value:The amount to the scale the selected object.

        Returns:
            None
        """
        for object in self.getobjectname():
            cmds.setAttr(object + ".scaleY", value)

    def setscaleZ(self, value):
        """Sets the Z scale from the selected object.

        Args:
            value:The amount to the scale the selected object.

        Returns:
            None
        """
        for object in self.getobjectname():
            cmds.setAttr(object + ".scaleZ", value)

    def getscaleX(self, *args):
        """Gets the X scale of the selected object.

        Args:
            *args:None

        Returns:
            The X scale of the selected object.
        """
        return cmds.getAttr(self.getobjectname() + ".scale"[0])

    def getscaleY(self, *args):
        """Gets the Y scale of the selected object.

        Args:
            *args:None

        Returns:
            The Y scale of the selected object.
        """
        return cmds.getAttr(self.getobjectname() + ".scale"[1])

    def getscaleZ(self, *args):
        """Gets the Z scale of the selected object.

        Args:
            *args:None

        Returns:
            The Z scale of the selected object.
        """
        return cmds.getAttr(self.getobjectname() + ".scaleZ"[2])

    def freezetransform(self, *args):
        """Deletes the history and freezes the transformations of the selected object.

        Args:
            *args: Ignored

        Returns:
            None
        """
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)
        cmds.constructionHistory(query=True, toggle=True)

    def parentconstrain(self):
        """Parents the joint to the Control NURB.
        Uses Constrain -> Parent.
        Returns:
            None
        """
        cmds.parentConstraint(maintainOffset=True, weight=True)

    def breakparentconnections(self):
        """Breaks the connection between the joint and control.
        Breaks the constrain parent to change something on the NURB.
        Returns:
            None
        """
        constraint = cmds.listConnections(self.getobjectname(), type="parentConstraint")
        cmds.delete(constraint[0])

    def changecolourFn(self, colour):
        """ Passes the colour to change the NURB shapes.

        Args:
            colour: Name of the colour to change the shape to.

        Returns:
            The colours name.
        """

        def changeColour(*args):
            """Changes the colour of the NURB shapes.

            Args:
                *args: Ignored

            Returns:
                None
            """
            selected = self.getobjectname()
            for item in selected:
                cmds.setAttr(item + ".overrideEnabled", 1)
                cmds.setAttr(item + ".overrideColor", colour)

        return changeColour

    def close(self):
        """Closes the UI window.

        Returns:
            None
        """
        cmds.deleteUI(self.window, window=True)


controlCreator = MayaControlCreator()
controlCreator.buildUI()
