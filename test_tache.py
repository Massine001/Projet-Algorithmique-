import unittest
from tache import tri
from tache import max
from tache import creneau_opt
import numpy as np




class greedy_test(unittest.TestCase):
    def test_tri(self):
        a=[7,9,2,4]
        b=[10,40,20,25]
        x=tri(a,b)
        self.assertEqual(x,(([9,7,4,2]),[40,10,25,20]))

    def test_creneau_opt(self):
        a1=[70,60,50,30]
        b1=[2,1,1,3]
        w=creneau_opt(3,a1,b1)                             
        self.assertEqual(w,([60,70,30]))
    def test_creneau_opt_2(self):
        a=[100,27,25,19,15]
        b=[2,2,1,1,3]
        w=creneau_opt(3,a,b)  
        self.assertEqual(w,([27,100,15]))
   
if __name__ == '__main__' :
    unittest.main()