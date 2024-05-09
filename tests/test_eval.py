import unittest
from smurtls import Eval
import numpy as np
import pandas as pd

class TestEval(unittest.TestCase):
    # --------- Trivial cases ---------
    def test_hci_perfect_predictions(self):
        y_pred = np.array([
            [0.75, 0.25, 0.80],    # Predictions for three intervals (perfect predictions)
            [0.8, 0.35, 0.70],
            [0.8, 0.75, 0.74]
        ])

        labels_time = np.array([100, 101, 102])  # Survival times in days
        labels_status = np.array([1, 1, 1])       # Event status (1=event, 0=censored)

        breaks = np.array([0, 100, 150, 200])  # Three intervals: 0-100 days, 100-150 days, 150-200 days
        time = 1.0                              # Point of interest at 1.0 years

        expected_c_index = 1.0  # Perfect concordance for perfect predictions
        computed_c_index = Eval.hci(y_pred, labels_time, labels_status, breaks, time)
        self.assertAlmostEqual(computed_c_index, expected_c_index, places=4, msg="Perfect Predictions C-index mismatch")

    def test_hci_error_predictions(self):
        y_pred = np.array([
            [0.75, 0.25, 0.20],   
            [0.8, 0.35, 0.70],
            [0.8, 0.75, 0.74]
        ])
        
        labels_time = np.array([109, 101, 102])
        labels_status = np.array([1, 1, 1])

        breaks = np.array([0, 100, 150, 200])
        time = 1.0

        expected_c_index = 0.333333 
        computed_c_index = Eval.hci(y_pred, labels_time, labels_status, breaks, time)
        self.assertAlmostEqual(computed_c_index, expected_c_index, places=4, msg="Censored Predictions C-index mismatch")
        

   
        

if __name__ == '__main__':
    unittest.main()