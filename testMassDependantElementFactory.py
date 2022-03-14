'''series of test around MassDependantElement and MassDependantElementFactory'''
import unittest
from mooring.massDependantElement import MassDependantElement
from library.massDependantElementFactory import MassDependantElementFactory


class testMassDependantElementFactory(unittest.TestCase):
    
    def setUp(self):
        '''Parameters initialization'''
        self.factoryParameters = {  'category': "LPO",
                                    'name' : "rain train",
                                    'image' : "\Pictures\Anchors\lest.bmp",
                                    'length' : 1,
                                    'diametre' : 1,
                                    'aireProjetee' : .785,
                                    'coeffNormal' : 1.2,
                                    'coeffTangentiel' : 1}
        self.elementParameters1 = {'mass' : 1000}
        self.elementParameters2 = {'mass' : 100}

    def test_Mass_Dependant_Factory_Creation(self):
        '''test a normal creation of a factory'''
        mef = MassDependantElementFactory(   self.factoryParameters['category'],
                                    self.factoryParameters['name'], 
                                    self.factoryParameters['image'], 
                                    self.factoryParameters['length'],
                                    self.factoryParameters['diametre'],
                                    self.factoryParameters['aireProjetee'],
                                    self.factoryParameters['coeffNormal'],
                                    self.factoryParameters['coeffTangentiel'])

        self.assertIsInstance(mef,MassDependantElementFactory)
        self.assertEqual(mef.category, self.factoryParameters['category'])
        self.assertEqual(mef.name, self.factoryParameters['name'])
        self.assertEqual(mef.imageFile, self.factoryParameters['image'])
        self.assertEqual(mef.length, self.factoryParameters['length'])
        self.assertEqual(mef.diameter, self.factoryParameters['diametre'])
        self.assertEqual(mef.projectedArea, self.factoryParameters['aireProjetee'])
        self.assertEqual(mef.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(mef.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        return mef

    def test_Mass_Dependant_Element_Creation(self):
        '''test a normal creation of an element with the previous factory'''
        mef = self.test_Mass_Dependant_Factory_Creation()
        me = mef.creationElement(self.elementParameters1)

        self.assertIsInstance(me,MassDependantElement)
        self.assertEqual(me.category, self.factoryParameters['category'])
        self.assertEqual(me.name, self.factoryParameters['name'])
        self.assertEqual(me.imageFile, self.factoryParameters['image'])
        self.assertEqual(me.mass, self.elementParameters1['mass'])
        self.assertEqual(me.length, self.factoryParameters['length'])
        self.assertEqual(me.diameter, self.factoryParameters['diametre'])
        self.assertEqual(me.projectedArea, self.factoryParameters['aireProjetee'] )
        self.assertEqual(me.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(me.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        return me

    def test_Mass_Dependant_Element_Modification(self):
        '''test a normal modification of the previous element'''
        re = self.test_Mass_Dependant_Element_Creation()
        re.mass = self.elementParameters2['mass']

        self.assertIsInstance(re,MassDependantElement)
        self.assertEqual(re.category, self.factoryParameters['category'])
        self.assertEqual(re.name, self.factoryParameters['name'])
        self.assertEqual(re.imageFile, self.factoryParameters['image'])
        self.assertEqual(re.mass, self.elementParameters2['mass'] )
        self.assertEqual(re.length, self.factoryParameters['length'])
        self.assertEqual(re.diameter, self.factoryParameters['diametre'])
        self.assertEqual(re.projectedArea, self.factoryParameters['aireProjetee'] )
        self.assertEqual(re.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(re.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        

    def test_Element_Wrong_parameters_Name(self):
        '''test the handle of an Key Name Exception for the creation of an element'''
        ref = self.test_Mass_Dependant_Factory_Creation()
        with self.assertRaises(KeyError):
            ref.creationElement({"mas" : 0})


if __name__ == '__main__':
    unittest.main()