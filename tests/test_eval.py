import unittest
from smurtls import Eval
import numpy as np

class TestEval(unittest.TestCase):
    # --------- Trivial cases ---------
    def test_hci_default(self):
        y_pred = np.array([
            [0.75, 0.25],    
            [0.8, 0.35]
        ])                                  # -> predictions for intervals

        labels_time = np.array([100,101])   # -> in days
        labels_status = np.array([1,1])     # -> 1 = event, 0 = censored

        breaks = np.array([0,365])          # -> in days, two intervals
        time = 1.0                          # -> point of interest, in years

        expected_c_index = 1.0
        computed_c_index = Eval.hci(y_pred, labels_time, labels_status, breaks, time)
        self.assertAlmostEqual(computed_c_index, expected_c_index, places=4, msg="Trivial C-index mismatch")

   
        

if __name__ == '__main__':
    unittest.main()