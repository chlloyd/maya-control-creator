import maya.cmds as cmds

height = 1100
width = 300
cbw = 50


class mayaControlCreator(object):
    def __init__(self):
        self.window = 'controlcreator'
        self.title = "Rigging Control Creator"
        self.size = (width, height)

    def buildUI(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)

        # Creates a form layout to window
        cmds.rowColumnLayout(width=width)
        cmds.text(label='Instructions', align='center', font="boldLabelFont")
        cmds.text(label='Select the joint and press a control shape to create.', align='center')
        cmds.text(label='Naming', align='center', font="boldLabelFont")
        cmds.text(label="Use $OBJ to use selected joint name. ", align='center')
        cmds.rowColumnLayout(nc=3, cw=[(1, width / 3), (2, width / 3), (3, width / 3)])

        cmds.text(label='Prefix', align='center')
        cmds.text(label='Name', align='center')
        cmds.text(label='Suffix', align='center')

        self.prefix = cmds.textField("prefix")
        self.name = cmds.textField("name", text="$OBJ")
        self.suffix = cmds.textField("suffix")

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label='2D Shapes', align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, width / 2), (2, width / 2)])
        circle = cmds.button(label="Circle", command=self.createcircle)
        square = cmds.button(label="Square", command=self.createsquare)
        # TODO: ADD MORE 2D SHAPES FOR CONTROLS

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label='3D Shapes', align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, width / 2), (2, width / 2)])
        sphere = cmds.button(label="Sphere", command=self.createsphere)
        cube = cmds.button(label="Cube", command=self.createcube)
        # TODO: ADD MORE 3D SHAPES FOR CONTROLS

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label="Transform", align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, width / 5), (2, width / 5), (3, width / 5), (4, width / 5), (5, width / 5)])
        cmds.text(label="X")
        cmds.button(label="-10", command=self.transformXminus10)
        cmds.button(label="-1", command=self.transformXminus1)
        cmds.button(label="1", command=self.transformX1)
        cmds.button(label="10", command=self.transformX10)
        cmds.text(label="Y")
        cmds.button(label="-10", command=self.transformYminus10)
        cmds.button(label="-1", command=self.transformYminus1)
        cmds.button(label="1", command=self.transformY1)
        cmds.button(label="10", command=self.transformY10)
        cmds.text(label="Z")
        cmds.button(label="-10", command=self.transformZminus10)
        cmds.button(label="-1", command=self.transformZminus1)
        cmds.button(label="1", command=self.transformZ1)
        cmds.button(label="10", command=self.transformZ10)

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label="Rotation", align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, width / 3), (2, width / 3), (3, width / 3)])
        cmds.button(label="Rotate X 45", command=self.rotationX45)
        cmds.button(label="Rotate Y 45", command=self.rotationY45)
        cmds.button(label="Rotate Z 45", command=self.rotationZ45)
        cmds.button(label="Rotate X 90", command=self.rotationX90)
        cmds.button(label="Rotate Y 90", command=self.rotationY90)
        cmds.button(label="Rotate Z 90", command=self.rotationZ90)

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label="Scale", align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, width / 3), (2, width / 3), (3, width / 3)])
        cmds.button(label="Scale X0.125", command=self.scale0125)
        cmds.button(label="Scale X0.25", command=self.scale025)
        cmds.button(label="Scale X0.5", command=self.scale05)
        cmds.button(label="Scale X1.5", command=self.scale15)
        cmds.button(label="Scale X2", command=self.scale2)
        cmds.button(label="Scale X4", command=self.scale4)
        cmds.rowColumnLayout(width=width)

        cmds.separator(style='in')
        cmds.text(label="Delete History/Freeze Transformations", align='center', font="boldLabelFont")
        cmds.button(label="Apply", command=self.freezetransform)

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label="Colouring", align='center', font="boldLabelFont")

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, width / 3), (2, width / 3), (3, width / 3)])
        cmds.button(backgroundColor=[1.0, 0.0, 0.0], label="", command=self.changecolourred)
        cmds.button(backgroundColor=[0.0, 1.0, 0.0], label="", command=self.changecolourgreen)
        cmds.button(backgroundColor=[0.0, 0.0, 1.0], label="", command=self.changecolourblue)
        cmds.button(backgroundColor=[1.0, 1.0, 0.0], label="", command=self.changecolouryellow)
        cmds.button(backgroundColor=[0.0, 1.0, 1.0], label="", command=self.changecolourturquoise)
        cmds.button(backgroundColor=[1.0, 0.0, 1.0], label="", command=self.changecolourpink)
        cmds.button(backgroundColor=[1.0, 1.0, 1.0], label="", command=self.changecolourwhite)
        cmds.button(backgroundColor=[0.369, 0.369, 0.369], label="", command=self.changecolourgrey)
        cmds.button(backgroundColor=[0.0, 0.0, 0.0], label="", command=self.changecolourblack)

        cmds.rowColumnLayout(width=width)
        cmds.separator(style='in')
        cmds.text(label="Create Attributes", align='center', font="boldLabelFont")
        cmds.rowColumnLayout(nc=3, cw=[(1, width / 3), (2, width / 3), (3, width / 3)])

        cmds.text(label='Name', align='center')
        cmds.text(label='Min Value', align='center')
        cmds.text(label='Max Value', align='center')

        attrname = cmds.textField("attrname")
        attrminvalue = cmds.textField("attrminvalue", text="-360.0")
        attrmaxvalue = cmds.textField("attrmaxvalue", text="360.0")


        cmds.rowColumnLayout(width=width)
        cmds.rowColumnLayout(nc=3, cw=[(1, width / 3), (2, width / 3), (3, width / 3)])
        attrtype = cmds.radioCollection("attrtype")
        float = cmds.radioButton(label='Float', select=True)
        integer = cmds.radioButton(label='Integer')
        boolean = cmds.radioButton(label='Boolean')
        string = cmds.radioButton(label='String')
        vector = cmds.radioButton(label='Vector')
        blank = cmds.radioButton(visible=False)
        cmds.rowColumnLayout(width=width)
        cmds.button(label="Create Attribute", command=self.createattr)

        cmds.separator(style='in')
        cmds.text(label="Lock Attributes", align='center', font="boldLabelFont")
        cmds.rowColumnLayout(width=width)

        cmds.rowColumnLayout(nc=5, cw=[(1, width / 4.5), (2, width / 6.5), (3, width / 5), (4, width / 6), (5, width / 6)])
        cmds.text(label='', w=cbw)
        cmds.text(label='X', w=cbw)
        cmds.text(label='Y', w=cbw)
        cmds.text(label='Z', w=cbw)
        cmds.text(label='All', w=cbw)
        cmds.rowColumnLayout(width=width)

        cmds.rowColumnLayout(nc=2, cw=[(1, 80), (2, width - 80)])
        cmds.text(label='Translation:')
        cmds.checkBoxGrp('translate_checkBoxes', ncb=4,
                         cw4=(cbw, cbw, cbw, cbw))  # ,cc4=cmds.callbacks(self.set_checkBoxGrp, 'translate_checkBoxes'))
        cmds.text(label='Rotation:')
        cmds.checkBoxGrp('rotate_checkBoxes', ncb=4, cw4=(cbw, cbw, cbw, cbw))  # , cc4=cmds.callbacks(self.set_checkBoxGrp, 'rotate_checkBoxes'))
        cmds.text(label='Scale: ')
        cmds.checkBoxGrp('scale_checkBoxes', ncb=4, cw4=(cbw, cbw, cbw, cbw))  # , cc4=cmds.callbacks(self.set_checkBoxGrp, 'scale_checkBoxes'))
        cmds.text(label='Visibility:')
        cmds.checkBoxGrp('visibility_checkBox', cw=(1, cbw))

        cmds.rowColumnLayout(width=width)
        cmds.rowColumnLayout(nc=4, cw=[(1, width / 4), (2, width / 4), (3, width / 4), (4, width / 4)])
        cmds.button(visible=False)
        cmds.button(label="Lock/Hide", command=self.lockattribute)
        cmds.button(label="Show", command=self.showattribute)
        cmds.button(visible=False)
        cmds.rowColumnLayout(width=width)

        cmds.button(label="Close", command=self.close)
        cmds.rowColumnLayout(width=width)
        # Renders the final UI
        cmds.showWindow()

    def getobjectname(self):
        selectedname = cmds.ls(selection=True)
        if selectedname[0] == "":
            pass
        else:
            return selectedname[0]

    def getobjecttype(self):
        selected = cmds.ls(selection=True)
        return cmds.objectType(selected)

    def nurbname(self):
        prefixName = cmds.textField(self.prefix, q=1, text=1)
        nameName = cmds.textField(self.name, q=1, text=1)
        suffixName = cmds.textField(self.suffix, q=1, text=1)
        if prefixName == "$OBJ":
            prefixName = self.getobjecstname()
        if nameName == "$OBJ":
            nameName = self.getobjectname()
        if suffixName == "$OBJ":
            suffixName = self.getobjectname()
        objectName = str(prefixName) + "_" + str(nameName) + "_" + str(suffixName)
        return objectName

    def getposition(self):
        selected = cmds.ls(selection=True)
        if selected == []:
            position = [0, 0, 0]
        else:
            X = cmds.getAttr(selected[0] + ".translateX")
            Y = cmds.getAttr(selected[0] + ".translateY")
            Z = cmds.getAttr(selected[0] + ".translateZ")
            position = [X, Y, Z]
        return position

    def getrotation(self):
        selected = cmds.ls(selection=True)
        if selected == []:
            pass
        else:
            X = cmds.getAttr(selected[0] + ".rotateX")
            Y = cmds.getAttr(selected[0] + ".rotateY")
            Z = cmds.getAttr(selected[0] + ".rotateZ")
            rotation = [X, Y, Z]
        return rotation

    def createcircle(self, *args):
        position = self.getposition()
        cmds.circle(nr=[0, 1, 0], name=self.nurbname())
        cmds.setAttr(self.getobjectname() + ".translateX", position[0])
        cmds.setAttr(self.getobjectname() + ".translateY", position[1])
        cmds.setAttr(self.getobjectname() + ".translateZ", position[2])
        # rotation
        self.freezetransform()

    def createsquare(self, *args):
        position = self.getposition()
        cmds.curve(d=1, p=[(-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (-1, 0, -1)], k=[0, 1, 2, 3, 4])
        cmds.setAttr(self.getobjectname() + ".translateX", position[0])
        cmds.setAttr(self.getobjectname() + ".translateY", position[1])
        cmds.setAttr(self.getobjectname() + ".translateZ", position[2])
        # rotation
        self.freezetransform()

    def createsphere(self, *args):
        position = self.getposition()
        cmds.sphere(r=1, name=self.nurbname())
        cmds.setAttr(self.getobjectname() + ".translateX", position[0])
        cmds.setAttr(self.getobjectname() + ".translateY", position[1])
        cmds.setAttr(self.getobjectname() + ".translateZ", position[2])
        # rotation
        self.freezetransform()

    def createcube(self, *args):
        position = self.getposition()
        cmds.curve(degree=1,
                   point=[(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
                          (1, -1, -1), (-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)],
                   knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], name=self.nurbname())
        cmds.setAttr(self.getobjectname() + ".translateX", position[0])
        cmds.setAttr(self.getobjectname() + ".translateY", position[1])
        cmds.setAttr(self.getobjectname() + ".translateZ", position[2])
        # rotation
        self.freezetransform()

    def transformXminus10(self, *args):
        current_posX = self.getposition()[0]
        current_posX -= 10
        cmds.setAttr(self.getobjectname() + ".translateX", current_posX)

    def transformXminus1(self, *args):
        current_posX = self.getposition()[0]
        current_posX -= 1
        cmds.setAttr(self.getobjectname() + ".translateX", current_posX)

    def transformX10(self, *args):
        current_posX = self.getposition()[0]
        current_posX += 10
        cmds.setAttr(self.getobjectname() + ".translateX", current_posX)

    def transformX1(self, *args):
        current_posX = self.getposition()[0]
        current_posX += 1
        cmds.setAttr(self.getobjectname() + ".translateX", current_posX)

    def transformYminus10(self, *args):
        current_posY = self.getposition()[1]
        current_posY -= 10
        cmds.setAttr(self.getobjectname() + ".translateY", current_posY)

    def transformYminus1(self, *args):
        current_posY = self.getposition()[1]
        current_posY -= 1
        cmds.setAttr(self.getobjectname() + ".translateY", current_posY)

    def transformY10(self, *args):
        current_posY = self.getposition()[1]
        current_posY += 10
        cmds.setAttr(self.getobjectname() + ".translateY", current_posY)

    def transformY1(self, *args):
        current_posY = self.getposition()[1]
        current_posY += 1
        cmds.setAttr(self.getobjectname() + ".translateY", current_posY)

    def transformZminus10(self, *args):
        current_posZ = self.getposition()[2]
        current_posZ -= 10
        cmds.setAttr(self.getobjectname() + ".translateZ", current_posZ)

    def transformZminus1(self, *args):
        current_posZ = self.getposition()[2]
        current_posZ -= 1
        cmds.setAttr(self.getobjectname() + ".translateZ", current_posZ)

    def transformZ10(self, *args):
        current_posZ = self.getposition()[2]
        current_posZ += 10
        cmds.setAttr(self.getobjectname() + ".translateZ", current_posZ)

    def transformZ1(self, *args):
        current_posZ = self.getposition()[2]
        current_posZ += 1
        cmds.setAttr(self.getobjectname() + ".translateZ", current_posZ)

    def rotationX45(self, *args):
        current_rotX = self.getrotation()[0]
        current_rotX += 45
        cmds.setAttr(self.getobjectname() + ".rotateX", current_rotX)

    def rotationY45(self, *args):
        current_rotY = self.getrotation()[1]
        current_rotY += 45
        cmds.setAttr(self.getobjectname() + ".rotateY", current_rotY)

    def rotationZ45(self, *args):
        current_rotZ = self.getrotation()[2]
        current_rotZ += 45
        cmds.setAttr(self.getobjectname() + ".rotateZ", current_rotZ)

    def rotationX90(self, *args):
        current_rotX = self.getrotation()[0]
        current_rotX += 90
        cmds.setAttr(self.getobjectname() + ".rotateX", current_rotX)

    def rotationY90(self, *args):
        current_rotY = self.getrotation()[1]
        current_rotY += 90
        cmds.setAttr(self.getobjectname() + ".rotateY", current_rotY)

    def rotationZ90(self, *args):
        current_rotZ = self.getrotation()[2]
        current_rotZ += 90
        cmds.setAttr(self.getobjectname() + ".rotateZ", current_rotZ)

    def scale0125(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 0.125
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def scale025(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 0.25
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def scale05(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 0.5
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def scale15(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 1.5
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def scale2(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 2
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def scale4(self, *args):
        selectedobject = cmds.ls(selection=True)[0]
        currentscale = cmds.getAttr(selectedobject + ".scaleX")
        scalechange = 4
        cmds.setAttr(selectedobject+".scaleX", float(currentscale)*scalechange)
        cmds.setAttr(selectedobject + ".scaleY", float(currentscale) * scalechange)
        cmds.setAttr(selectedobject + ".scaleZ", float(currentscale) * scalechange)

    def freezetransform(self, *args):
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.constructionHistory(q=True, tgl=True)

    def changecolourred(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 13)

    def changecolourgreen(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 14)

    def changecolourblue(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 6)

    def changecolourwhite(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 16)

    def changecolourgrey(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 0)

    def changecolourblack(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 1)


    def changecolourpink(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 9)

    def changecolouryellow(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 17)

    def changecolourturquoise(self, *args):
        selected = self.getobjectname()
        cmds.setAttr(selected + ".overrideEnabled", 1)
        cmds.setAttr(selected + '.overrideColor', 18)

    def createattr(self, *args):
        attrname = cmds.textField("attrname", q=1, text=1)
        attrminvalue = cmds.textField("attrminvalue", q=1, text=1)
        attrmaxvalue = cmds.textField("attrmaxvalue", q=1, text=1)
        attrtype = cmds.radioCollection("attrtype", query=True, select=True)
        attrradioselection = cmds.radioButton(attrtype, query=True, label=True)
        selected = self.getobjectname()
        if attrradioselection == "Float":
            self.createfloatattr(attrname, float(attrminvalue), float(attrmaxvalue), selected)
        elif attrradioselection == "Integer":
            self.createintegerattr(attrname, int(attrminvalue), int(attrmaxvalue), selected)
        elif attrradioselection == "Boolean":
            self.createbooleanattr(attrname, selected)
        elif attrradioselection == "String":
            self.createstringattr(attrname, selected)
        else:
            self.createvectorattr(attrname, attrminvalue, attrmaxvalue)

    def createfloatattr(self, name, minvalue, maxvalue, selected):
        cmds.select(selected)
        cmds.addAttr(longName=name, min=minvalue, max=maxvalue, attributeType="float")

    def createintegerattr(self, name, minvalue, maxvalue, selected):
        cmds.select(selected)
        cmds.addAttr(longName=name, min=minvalue, max=maxvalue, attributeType="integer")

    def createbooleanattr(self, name, selected):
        cmds.select(selected)
        cmds.addAttr(longName=name, attributeType="boolean")

    def createstringattr(self, name, selected):
        cmds.select(selected)
        cmds.addAttr(longName=name, attributeType="string")

    def createvectorattr(self, name, minvalue, maxvalue, selected):
        cmds.select(selected)
        cmds.addAttr(longName=name, attributeType="vector", min=minvalue, max=maxvalue)

    def close(self, *args):
        cmds.deleteUI(self.window, window=True)

    def getselectedattributes(self, *args):
        translatelist = [False, False, False]
        rotatelist = [False, False, False]
        scalelist = [False, False, False]
        visibilitylist = [False]

        if cmds.checkBoxGrp("translate_checkBoxes", query=True, v1=True):
            translatelist[0] = True
        if cmds.checkBoxGrp("translate_checkBoxes", query=True, v2=True):
            translatelist[1] = True
        if cmds.checkBoxGrp("translate_checkBoxes", query=True, v3=True):
            translatelist[2] = True
        if cmds.checkBoxGrp("translate_checkBoxes", query=True, v4=True):
            translatelist[0], translatelist[1], translatelist[2], = True, True, True

        if cmds.checkBoxGrp("rotate_checkBoxes", query=True, v1=True):
            rotatelist[0] = True
        if cmds.checkBoxGrp("rotate_checkBoxes", query=True, v2=True):
            rotatelist[1] = True
        if cmds.checkBoxGrp("rotate_checkBoxes", query=True, v3=True):
            rotatelist[2] = True
        if cmds.checkBoxGrp("rotate_checkBoxes", query=True, v4=True):
            rotatelist[0], rotatelist[1], rotatelist[2], = True, True, True

        if cmds.checkBoxGrp("scale_checkBoxes", query=True, v1=True):
            scalelist[0] = True
        if cmds.checkBoxGrp("scale_checkBoxes", query=True, v2=True):
            scalelist[1] = True
        if cmds.checkBoxGrp("scale_checkBoxes", query=True, v3=True):
            scalelist[2] = True
        if cmds.checkBoxGrp("scale_checkBoxes", query=True, v4=True):
            scalelist[0], scalelist[1], scalelist[2], = True, True, True

        if cmds.checkBoxGrp("visibility_checkBox", query=True, v1=True):
            visibilitylist[0] = True

        return [translatelist, rotatelist, scalelist, visibilitylist]

    def lockattribute(self, *args):
        attribute = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
        selectedattributes = self.getselectedattributes()
        name = self.getobjectname()
        counter = 0
        for result in selectedattributes:
            if type(result) is list:
                for i in result:
                    cmds.setAttr(name+attribute[counter], lock=i)
                    counter += 1

    def showattribute(self, *args):
        attribute = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
        selectedattributes = self.getselectedattributes()
        name = self.getobjectname()
        counter = 0
        for result in selectedattributes:
            print(result)
            if type(result) is list:
                for i in result:
                    print(i)
                    cmds.setAttr(name+attribute[counter], keyable=i, channelBox=i)
                    counter += 1


controlCreator = mayaControlCreator()
controlCreator.buildUI()
