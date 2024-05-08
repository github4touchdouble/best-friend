import unittest
import pandas as pd
from smurtls import Reader

class TestReader(unittest.TestCase):
    def test_read_csv_default(self):
        expected_columns = ["A", "B", "C", "D"]
        df = Reader.read_csv("tests/data/case_read_csv_default.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df[df.isna().any(axis=1)]), 2)
        self.assertListEqual(list(df.columns), expected_columns)

        df = Reader.read_csv("tests/data/case_read_csv_default.csv", dropna_rows=True)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df[df.isna().any(axis=1)]), 0)
        self.assertListEqual(list(df.columns), expected_columns)

        df = Reader.read_csv("tests/data/case_read_csv_default.csv", dropna_rows=True, head=0.5, head_type="frac")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df[df.isna().any(axis=1)]), 0)
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertEqual(df.shape[0], 4)


    
    def test_read_csv_dtype(self):
        expected_columns_dtype = [{"A":"nan"}, {"B":"bin"}, {"C":"bin"}, {"D":"num"}]
        expected_columns = list(map(lambda d: list(d.keys())[0], expected_columns_dtype))
        df = Reader.read_csv("tests/data/case_read_csv_default.csv", expected_columns, dropna_rows=True)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df[df.isna().any(axis=1)]), 0)
        self.assertListEqual(list(df.columns), expected_columns)
       
        

if __name__ == '__main__':
    unittest.main()