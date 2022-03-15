import unittest
from mooring.unmodifiableElement import UnmodifiableElement
from library.unmodifiableElementFactory import UnmodifiableElementFactory

class testRopeElementFactory(unittest.TestCase):
    
    def setUp(self):
        '''Parameters initialization'''
        self.factoryParameters = {  'category': "LPO",
                                    'name' : "microcat",
                                    'image' : "\Pictures\Instrument\microcat.bmp",
                                    'masse' : -3,
                                    'length' : 0.6,
                                    'aireProjetee' : 0.03,
                                    'coeffNormal' : 1.3,
                                    'coeffTangentiel' : 0.9}

    def test_Unmodifiable_Factory_Creation(self):
        '''test a normal creation of a factory'''
        uef = UnmodifiableElementFactory(   self.factoryParameters['category'],
                                    self.factoryParameters['name'], 
                                    self.factoryParameters['image'], 
                                    self.factoryParameters['masse'],
                                    self.factoryParameters['length'],
                                    self.factoryParameters['aireProjetee'],
                                    self.factoryParameters['coeffNormal'],
                                    self.factoryParameters['coeffTangentiel'])

        self.assertIsInstance(uef,UnmodifiableElementFactory)
        self.assertEqual(uef.category, self.factoryParameters['category'])
        self.assertEqual(uef.name, self.factoryParameters['name'])
        self.assertEqual(uef.imageFile, self.factoryParameters['image'])
        self.assertEqual(uef.mass, self.factoryParameters['masse'])
        self.assertEqual(uef.length, self.factoryParameters['length'])
        self.assertEqual(uef.projectedArea, self.factoryParameters['aireProjetee'])
        self.assertEqual(uef.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(uef.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        return uef

    def test_Unmodifiable_Element_Creation(self):
        '''test a normal creation of an element with the previous factory'''
        uef = self.test_Unmodifiable_Factory_Creation()
        ue = uef.creationElement()

        self.assertIsInstance(ue,UnmodifiableElement)
        self.assertEqual(ue.category, self.factoryParameters['category'])
        self.assertEqual(ue.name, self.factoryParameters['name'])
        self.assertEqual(ue.imageFile, self.factoryParameters['image'])
        self.assertEqual(ue.mass, self.factoryParameters['masse'])
        self.assertEqual(ue.length, self.factoryParameters['length'])
        self.assertEqual(ue.projectedArea, self.factoryParameters['aireProjetee'])
        self.assertEqual(ue.normalDragCoeff, self.factoryParameters['coeffNormal'])
        self.assertEqual(ue.tangentialDragCoeff, self.factoryParameters['coeffTangentiel'])
        return ue


if __name__ == '__main__':
    unittest.main()