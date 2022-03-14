'''series of test around RopeElement and RopeElementFactory'''
import unittest
from mooring.ropeElement import RopeElement
from library.ropeElementFactory import RopeElementFactory


class testRopeElementFactory(unittest.TestCase):
    
    def setUp(self):
        '''Parameters initialization'''
        self.factoryParameters = {  'category': "LPO",
                                    'name' : "parafil kevlar 8,5 mm",
                                    'image' : "\Pictures\Ropes\cable.bmp",
                                    'masse' : -0.0034,
                                    'diametre' : 0.0085,
                                    'aireProjetee' : 0.0085,
                                    'coeffNormal' : 1.3,
                                    'coeffTangentiel' : 0.1,
                                    'coeffEtirement' : [0,0.031428571,0],
                                    'rupture' : 3000}
        self.elementParameters1 = {'length' : 0}
        self.elementParameters2 = {'length' : 100}

    def test_Rope_Factory_Creation(self):
        '''test a normal creation of a factory'''
        ref = RopeElementFactory(   self.factoryParameters['category'],
                                    self.factoryParameters['name'], 
                                    self.factoryParameters['image'], 
                                    self.factoryParameters['masse'],
                                    self.factoryParameters['diametre'],
                                    self.factoryParameters['aireProjetee'],
                                    self.factoryParameters['coeffNormal'],
                                    self.factoryParameters['coeffTangentiel'],
                                    self.factoryParameters['coeffEtirement'],
                                    self.factoryParameters['rupture'])

        self.assertIsInstance(ref,RopeElementFactory)
        self.assertEqual(ref.category, self.factoryParameters['category'])
        self.assertEqual(ref.name, self.factoryParameters['name'])
        self.assertEqual(ref.imageFile, self.factoryParameters['image'])
        self.assertEqual(ref.massByLength, self.factoryParameters['masse'])
        self.assertEqual(ref.diameter, self.factoryParameters['diametre'])
        self.assertEqual(ref.projectedAreaByLength, self.factoryParameters['aireProjetee'])
        self.assertEqual(ref.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(ref.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        self.assertEqual(ref.stretchCoeff, self.factoryParameters['coeffEtirement'])
        self.assertEqual(ref.breakingStretch, self.factoryParameters['rupture'])
        return ref

    def test_Rope_Element_Creation(self):
        '''test a normal creation of an element with the previous factory'''
        ref = self.test_Rope_Factory_Creation()
        re = ref.creationElement(self.elementParameters1)

        self.assertIsInstance(re,RopeElement)
        self.assertEqual(re.category, self.factoryParameters['category'])
        self.assertEqual(re.name, self.factoryParameters['name'])
        self.assertEqual(re.imageFile, self.factoryParameters['image'])
        self.assertEqual(re.mass, self.factoryParameters['masse'] * self.elementParameters1['length'])
        self.assertEqual(re.length, self.elementParameters1['length'])
        self.assertEqual(re.diameter, self.factoryParameters['diametre'])
        self.assertEqual(re.projectedArea, self.factoryParameters['aireProjetee'] * self.elementParameters1['length'])
        self.assertEqual(re.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(re.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        self.assertEqual(re.stretchCoeff, self.factoryParameters['coeffEtirement'])
        self.assertEqual(re.breakingStretch, self.factoryParameters['rupture'])
        return re

    def test_Rope_Element_Modification(self):
        '''test a normal modification of the previous element'''
        re = self.test_Rope_Element_Creation()
        re.length = self.elementParameters2['length']

        self.assertIsInstance(re,RopeElement)
        self.assertEqual(re.category, self.factoryParameters['category'])
        self.assertEqual(re.name, self.factoryParameters['name'])
        self.assertEqual(re.imageFile, self.factoryParameters['image'])
        self.assertEqual(re.mass, self.factoryParameters['masse'] * self.elementParameters2['length'])
        self.assertEqual(re.length, self.elementParameters2['length'])
        self.assertEqual(re.diameter, self.factoryParameters['diametre'])
        self.assertEqual(re.projectedArea, self.factoryParameters['aireProjetee'] * self.elementParameters2['length'])
        self.assertEqual(re.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(re.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        self.assertEqual(re.stretchCoeff, self.factoryParameters['coeffEtirement'])
        self.assertEqual(re.breakingStretch, self.factoryParameters['rupture'])

    def test_Element_Wrong_parameters_Name(self):
        '''test the handle of an Key Name Exception for the creation of an element'''
        ref = self.test_Rope_Factory_Creation()
        with self.assertRaises(KeyError):
            ref.creationElement({"lengt" : 0})


if __name__ == '__main__':
    unittest.main()