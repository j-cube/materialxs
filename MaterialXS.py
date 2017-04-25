########################################################################
#  MaterialXS - An eXtra Small Python implementation of MaterialX.     #
#                                                                      #
#  Authors: Bo Zhou, Paolo Berto Durante, Omar Espinosa Rojas.         #
#                                                                      #
#  Copyright 2017 J Cube Inc. Tokyo, Japan                             #
#                                                                      #
#  Licensed under the Apache License, Version 2.0 (the "License");     #
#  you may not use this file except in compliance with the License.    #
#  You may obtain a copy of the License at                             #
#                                                                      #
#      http://www.apache.org/licenses/LICENSE-2.0                      #
#                                                                      #
#  Unless required by applicable law or agreed to in writing, software #
#  distributed under the License is distributed on an "AS IS" BASIS,   #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or     #    
#  implied. See the License for the specific language governing        #
#  permissions and limitations under the License.                      #
########################################################################

##
# Compatible with MaterialX Specs v1.33
# http://www.materialx.org

import collections
import difflib
import string
import xml.dom.minidom

import unittest

#
#
kTrueTag = 'true'
kFalseTag = 'false'

kIntegerTag = 'integer'
kBooleanTag = 'boolean'
kFloatTag = 'float'
kColor2Tag = 'color2'
kColor3Tag = 'color3'
kColor4Tag = 'color4'
kVector2Tag = 'vector2'
kVector3Tag = 'vector3'
kVector4Tag = 'vector4'
kStringTag = 'string'
kFilenameTag = 'filename'
kShaderNodeTag = 'shadernode'

kIntegerArrayTag = 'integerarray'
kFloatArrayTag = 'floatarray'
kColor2ArrayTag = 'color2array'
kColor3ArrayTag = 'color3array'
kColor4ArrayTag = 'color4array'
kVector2ArrayTag = 'vector2array'
kVector3ArrayTag = 'vector3array'
kVector4ArrayTag = 'vector4array'
kStringArrayTag = 'stringarray'

kNameTag = 'name'
kTypeTag = 'type'
kValueTag = 'value'
kRegexTag = 'regex'

kCollectionTag = 'collection'
kCollectionAddTag = 'collectionadd'

kParameterTag = 'parameter'

kGeomInfoTag = 'geominfo'
kGeomAttrTag = 'geomattr'

kCoShaderTag = 'coshader'
kAOVTag = 'aov'
kAOVSetTag = 'aovset'
kShaderTag = 'shader'
kShaderRefTag = 'shaderref'
kMaterialAssignTag = 'materialassign'
kMaterialTag = 'material'
kLookTag = 'look'
kMaterialXTag = 'materialx'

#
#
class Object(object):

    def __init__(self):
        pass

    def getTypeName(self):
        pass

#
class Attribute(Object):

    def __init__(self, name, required = False, value = None):
        self.name = name
        self.required = required
        self.value = value

    def getTypeName(self):
        pass

    def fromString(self, x):
        pass

    def __str__(self):
        if isinstance(self.value, list) or isinstance(self.value, tuple):
            return ','.join(str(x) for x in self.value)
        else:
            return str(self.value)

class IntegerAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def fromString(self, x):
        self.value = int(x)

    def getTypeName(self):
        return kIntegerTag

    def __str__(self):
        return str(self.value)

class BooleanAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kBooleanTag

    def fromString(self, x):
        self.value = bool(x)

    def __str__(self):
        if self.value:
            return kTrueTag
        else:
            return kFalseTag

class StringAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kStringTag

    def fromString(self, x):
        self.value = str(x)

class FloatAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kFloatTag

    def fromString(self, x):
        self.value = float(x)

class Color2Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor2Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Color3Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor3Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Color4Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor4Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector2Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector2Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector3Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector3Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector4Attribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector4Tag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class FilenameAttribute(StringAttribute):

    def __init__(self, name, required = False, value = None):
        StringAttribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kFilenameTag

    def fromString(self, x):
        self.value = str(x)

class ShaderNodeAttribute(StringAttribute):

    def __init__(self, name, required = False, value = None):
        StringAttribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kShaderNodeTag

    def fromString(self, x):
        self.value = str(x)

class IntegerArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kIntegerArrayTag

    def fromString(self, a):
        self.value = map(lambda x : int(x), a.split(','))

class FloatArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kFloatArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Color2ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor2ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Color3ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor3ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Color4ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kColor4ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector2ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector2ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector3ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector3ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class Vector4ArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kVector4ArrayTag

    def fromString(self, a):
        self.value = map(lambda x : float(x), a.split(','))

class StringArrayAttribute(Attribute):

    def __init__(self, name, required = False, value = None):
        Attribute.__init__(self, name, required, value)

    def getTypeName(self):
        return kStringArrayTag

    def fromString(self, a):
        a = a.replace('\,', ',')
        self.value = map(lambda x : str(x), a.split(','))

#
class Element(Object):

    def __init__(self):
        self.attributes = collections.OrderedDict()
        self.children = collections.OrderedDict()

    def getTypeName(self):
        pass

    def fromXmlNode(self, xmlNode):
        assert(xmlNode.nodeName == self.getTypeName())

        for (k, v) in xmlNode.attributes.items():
            if self.attributes.has_key(k):
                self.attributes[k].fromString(v)

    def toXmlNode(self, xmlDoc):
        thisXmlNode = xmlDoc.createElement(self.getTypeName())

        for (key, attr) in self.attributes.iteritems():
            if attr is None:
                continue

            if isinstance(attr, Attribute):
                if not attr.value is None:
                    thisXmlNode.setAttribute(key, str(attr))
            else:
                thisXmlNode.setAttribute(key, str(attr))

        for (key, child) in self.children.iteritems():
            thisXmlNode.appendChild(child.toXmlNode(xmlDoc))

        return thisXmlNode

#
class GeomInfo(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes['geom'] = StringAttribute('geom')
        self.attributes[kRegexTag] = StringAttribute(kRegexTag)
        self.attributes[kCollectionTag] = StringAttribute(kCollectionTag)

    def getTypeName(self):
        return kGeomInfoTag

#
class GeomAttr(Element):

    def __init__(self, name = '', gtype = '', value = None):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes[kTypeTag] = StringAttribute(kTypeTag, True, gtype)
        self.attributes[kValueTag] = StringAttribute(kValueTag, False, value)

    def getTypeName(self):
        return kGeomAttrTag

#
class CollectionAdd(Element):

    def __init__(self, name = '', geom = '', includechildren = False):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes['geom'] = StringAttribute('geom', True, geom)
        self.attributes['includechildren'] = BooleanAttribute('includechildren')

    def getTypeName(self):
        return kCollectionAddTag

#
class Collection(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)

    def getTypeName(self):
        return kCollectionTag

#
class Shader(Element):

    def __init__(self, name = '', shaderType = '', shaderProgram = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes['shadertype'] = StringAttribute('shadertype', True, shaderType)
        self.attributes['shaderprogram'] = StringAttribute('shaderprogram', True, shaderProgram)
        self.attributes['application'] = StringAttribute('application')
        self.attributes['aovset'] = StringAttribute('aovset')
        self.attributes['xpos'] = FloatAttribute('xpos')
        self.attributes['ypos'] = FloatAttribute('ypos')
        self.attributes['aovs'] = StringAttribute('aovs')
        self.attributes['passaovs'] = StringAttribute('passaovs')

    def getTypeName(self):
        return kShaderTag

#
class AOV(Element):

    def __init__(self, name = '', vtype = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes[kTypeTag] = StringAttribute(kTypeTag, True, vtype)

    def getTypeName(self):
        return kAOVTag

#
class AOVSet(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)

    def getTypeName(self):
        return kAOVSetTag

#
class CoShader(Element):

    def __init__(self, name = '', shader = '', aovset = None, aovs = None):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes[kShaderTag] = StringAttribute(kShaderTag, True, shader)
        self.attributes[kAOVSetTag] = StringAttribute(kAOVSetTag, False, aovset)
        self.attributes['aovs'] = StringAttribute('aovs', False, aovs)

    def getTypeName(self):
        return kCoShaderTag

#
class Parameter(Element):

    def __init__(self, name = '', ptype = '', value = None, default = None):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes[kTypeTag] = StringAttribute(kTypeTag, True, ptype)
        self.attributes[kValueTag] = value
        self.attributes['default'] = default
        self.attributes['publicname'] = StringAttribute('publicname')

    def getTypeName(self):
        return kParameterTag

    def fromXmlNode(self, xmlNode):
        self.attributes[kNameTag].value = xmlNode.attributes[kNameTag].firstChild.nodeValue
        self.attributes[kTypeTag].value = xmlNode.attributes[kTypeTag].firstChild.nodeValue
        self.attributes[kValueTag] = xmlNode.attributes[kValueTag].firstChild.nodeValue

#
class OpGraph(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)

    def getTypeName(self):
        return 'opgraph'

#
class Constant(Element):

    def __init__(self, name = '', ptype = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes[kTypeTag] = StringAttribute(kTypeTag, True, ptype)

    def getTypeName(self):
        return 'constant'

#
class Material(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes['xpos'] = FloatAttribute('xpos')
        self.attributes['ypos'] = FloatAttribute('ypos')

    def getTypeName(self):
        return kMaterialTag

    def fromXmlNode(self, xmlNode):
        assert(xmlNode.nodeName == self.getTypeName())

        super(Material, self).fromXmlNode(xmlNode)

#
class ShaderRef(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)

    def getTypeName(self):
        return kShaderRefTag

#
class Look(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)

    def getTypeName(self):
        return kLookTag

#
class MaterialAssign(Element):

    def __init__(self, name = ''):
        Element.__init__(self)

        #
        self.attributes[kNameTag] = StringAttribute(kNameTag, True, name)
        self.attributes['geom'] = StringAttribute('geom')
        self.attributes[kCollectionTag] = StringAttribute(kCollectionTag)
        self.attributes[kRegexTag] = StringAttribute(kRegexTag)

    def getTypeName(self):
        return kMaterialAssignTag

#
class MaterialX(Element):

    def __init__(self):
        Element.__init__(self)

        self.attributes['version'] = StringAttribute('version', True, '1.0')

    def getTypeName(self):
        return kMaterialXTag

    def __CreateTypedNode(self, xmlNode, myType, container):
        myNode = myType()
        myNode.fromXmlNode(xmlNode)
        myName = str(myNode.attributes[kNameTag])
        container.children[myName] = myNode

        return myNode

    def __CreateNodeRecursively(self, xmlNode, container):
        for childXmlNode in xmlNode.childNodes:
            childNodeName = childXmlNode.nodeName

            #
            if childNodeName == kMaterialTag:
                materialNode = self.__CreateTypedNode(childXmlNode, Material, container)
                self.__CreateNodeRecursively(childXmlNode, materialNode)
            elif childNodeName == kLookTag:
                lookNode = self.__CreateTypedNode(childXmlNode, Look, container)
                self.__CreateNodeRecursively(childXmlNode, lookNode)
            elif childNodeName == kShaderRefTag:
                shaderRefNode = self.__CreateTypedNode(childXmlNode, ShaderRef, container)
                self.__CreateNodeRecursively(childXmlNode, shaderRefNode)
            elif childNodeName == kShaderTag:
                shaderNode = self.__CreateTypedNode(childXmlNode, Shader, container)
                self.__CreateNodeRecursively(childXmlNode, shaderNode)
            elif childNodeName == kCoShaderTag:
                coshaderNode = self.__CreateTypedNode(childXmlNode, CoShader, container)
            elif childNodeName == kParameterTag:
                parameterNode = self.__CreateTypedNode(childXmlNode, Parameter, container)
            elif childNodeName == kAOVTag:
                aovNode = self.__CreateTypedNode(childXmlNode, AOV, container)
            elif childNodeName == kAOVSetTag:
                aovSetNode = self.__CreateTypedNode(childXmlNode, AOVSet, container)
                self.__CreateNodeRecursively(childXmlNode, aovSetNode)
            elif childNodeName == kMaterialAssignTag:
                materialAssignNode = self.__CreateTypedNode(childXmlNode, MaterialAssign, container)
            elif childNodeName == kCollectionTag:
                collectionNode = self.__CreateTypedNode(childXmlNode, Collection, container)
                self.__CreateNodeRecursively(childXmlNode, collectionNode)
            elif childNodeName == kCollectionAddTag:
                collectionAddNode = self.__CreateTypedNode(childXmlNode, CollectionAdd, container)
            elif childNodeName == kGeomInfoTag:
                geominfoNode = self.__CreateTypedNode(childXmlNode, GeomInfo, container)
                self.__CreateNodeRecursively(childXmlNode, geominfoNode)
            elif childNodeName == kGeomAttrTag:
                geomAttrNode = self.__CreateTypedNode(childXmlNode, GeomAttr, container)

    def fromXmlNode(self, xmlNode):
        assert(xmlNode.nodeName == self.getTypeName())

        versionXmlAttr = xmlNode.attributes['version']
        assert(versionXmlAttr.firstChild.nodeValue == '1.0')
        self.attributes['version'].value = versionXmlAttr.firstChild.nodeValue

        #
        self.__CreateNodeRecursively(xmlNode, self)

    def __str__(self):
        #
        xmlDoc = xml.dom.minidom.Document()
        xmlDoc.appendChild(self.toXmlNode(xmlDoc))
        return xmlDoc.toprettyxml()

###############################################################################

#
class AttributesTest(unittest.TestCase):

    def testIntegerAttribute(self):
        ia = IntegerAttribute('my_integer_attr', True, 123456)
        self.assertEqual(ia.getTypeName(), kIntegerTag)
        self.assertEqual(ia.name, 'my_integer_attr')
        self.assertEqual(ia.value, 123456)
        self.assertEqual(str(ia), '123456')

    def testFloatAttribute(self):
        fa = FloatAttribute('my_float_attr', True, 123.456)
        self.assertEqual(fa.getTypeName(), kFloatTag)
        self.assertEqual(fa.name, 'my_float_attr')
        self.assertEqual(fa.value, 123.456)

    def testVector2Attribute(self):
        v2a = Vector2Attribute('my_vector2_attr', True, [0.123, 0.321])
        self.assertEqual(v2a.getTypeName(), kVector2Tag)
        self.assertEqual(v2a.name, 'my_vector2_attr')
        self.assertEqual(str(v2a), '0.123,0.321')

        v2a.fromString('0.789,0.456')
        self.assertEqual(str(v2a), '0.789,0.456')

    def testColor3ArrayAttribute(self):
        c3a = Color3ArrayAttribute('ramp', True, [0.123, 0.456, 0.789])
        self.assertEqual(str(c3a), '0.123,0.456,0.789')

        c3a.fromString('0.789,0.456,0.123')
        print c3a.value

#
class MaterialXTest(unittest.TestCase):

    def __createCollections(self, name):
        testCollection = Collection(name)

        nameAdd = name + 'Add'
        testCollection.children[nameAdd] = CollectionAdd(nameAdd, '/pCube1/pCubeShape1,/pSphere1/pSphereShape1')

        return testCollection

    def __createGeomInfo(self):
        gi1 = GeomInfo('gi1')
        txtid = GeomAttr('txtid', kIntegerTag, '1001')
        gi1.children['txtid'] = txtid

        return gi1

    def __createOutColorAOVSet(self):
        aovset = AOVSet('outColor')

        aovset.children['outColor'] = AOV('outColor', kColor3Tag)

        return aovset

    def __createOutTransparencyAOVSet(self):
        aovset = AOVSet('outTransparency')

        aovset.children['outTransparency'] = AOV('outTransparency', kColor3Tag)

        return aovset

    def __createOutColorTransparencyAOVSet(self):
        aovset = AOVSet('outColorTransparency')

        aovset.children['outColor'] = AOV('outColor', kColor3Tag)
        aovset.children['outTransparency'] = AOV('outTransparency', kColor3Tag)

        return aovset

    def __createOutTransparencyAOVSet(self):
        aovset = AOVSet('outTransparency')

        aovset.children['outTransparency'] = AOV('outTransparency', kColor3Tag)

        return aovset

    def __createOutAlphaAOVSet(self):
        aovset = AOVSet('outAlpha')

        aovset.children['outAlpha'] = AOV('outAlpha', kFloatTag)

        return aovset

    def __createOutUVAOVSet(self):
        aovset = AOVSet('outUV')

        aovset.children['outUV'] = AOV('outUV', kVector2Tag)

        return aovset

    def __createSurfaceShaderNetwork(self, mtlx):
        # A place2dTexture shader, has special output.
        #
        place2dTextureShaderName = 'place2dTexture1'

        place2dTexture1 = Shader(place2dTextureShaderName, 'utility', 'place2dTexture')

        # Setup attribute for this.
        #
        place2dTexture1.attributes['aovset'].value = 'outUV'

        # Set up nested elements.
        #
        place2dTexture1.children['repeatUV'] = Parameter('repeatUV', kVector2Tag, '8,8')

        mtlx.children[place2dTextureShaderName] = place2dTexture1

        # A noise shader, with the AOV set of Maya.
        #
        noiseShaderName = 'noise1'

        noise1 = Shader(noiseShaderName, 'utility', 'noise')

        noise1.attributes['aovset'].value = 'outColor'

        noise1.children['amplitude'] = Parameter('amplitude', kFloatTag, '0.5')
        noise1.children['uvCoord'] = CoShader('uvCoord', place2dTextureShaderName, 'outUV')

        mtlx.children[noiseShaderName] = noise1

        # A lambert shader
        #
        lambertShaderName = 'lambert1'

        lambert1 = Shader(lambertShaderName, 'surface', 'lambert')
        lambert1.children['color'] = Parameter('color', 'color', '0.5,0.3,0.1')
        lambert1.children['incandescence'] = CoShader('incandescence', noiseShaderName, 'outColor')

        lambert1.attributes['aovset'].value = 'outColorTransparency'

        #
        mtlx.children[noiseShaderName] = noise1
        mtlx.children[lambertShaderName] = lambert1

    def __createMaterial(self, materialName, shaderName):
        sg = Material(materialName)
        sg.children[shaderName] = ShaderRef(shaderName)

        return sg

    def __createLook(self, lookName, materialName, collectionName):
        lookA = Look(lookName)

        assign = MaterialAssign(materialName)
        assign.attributes[kCollectionTag].value = collectionName

        lookA.children[materialName] = assign

        return lookA

    def __testInput(self, data):
        print data
        docXmlNode = xml.dom.minidom.parseString(data)

        #
        mtlx = MaterialX()
        mtlx.fromXmlNode(docXmlNode.firstChild)
        serializedData = str(mtlx)
        print serializedData

        #
        for line in difflib.context_diff(data, serializedData):
            print line

    def __testOutput(self):
        mtlx = MaterialX()
        self.assertIsNotNone(mtlx)
        self.assertIsNotNone(str(mtlx))

        #
        collections = self.__createCollections('xyzCol')
        mtlx.children['xyzCol'] = collections

        #
        geominfo = self.__createGeomInfo() 
        mtlx.children['gi1'] = geominfo

        # Create several AOV sets for different usage.
        #
        aovset = self.__createOutColorAOVSet()
        mtlx.children['outColor'] = aovset

        aovset = self.__createOutTransparencyAOVSet()
        mtlx.children['outTransparency'] = aovset

        aovset = self.__createOutColorTransparencyAOVSet()
        mtlx.children['outColorTransparency'] = aovset

        aovset = self.__createOutAlphaAOVSet()
        mtlx.children['outAlpha'] = aovset

        aovset = self.__createOutUVAOVSet()
        mtlx.children['outUV'] = aovset

        # Create the surface shader network.
        #
        self.__createSurfaceShaderNetwork(mtlx)

        #
        sg = self.__createMaterial('lambert1SG', 'lambert1')
        mtlx.children['lambert1SG'] = sg

        #
        lookA = self.__createLook('lookA', 'lambert1SG', 'xyzCol')
        mtlx.children['lookA'] = lookA

        data = str(mtlx)

        return data

    def testIO(self):
        data = self.__testOutput()
        self.__testInput(data)

if __name__ == '__main__':
    unittest.main()