import numpy as np


class MultiHotEncoder:

    @staticmethod
    def multi_hot_encode(sequences, num_classes):
        results = np.zeros((len(sequences), num_classes))

        for i, sequence in enumerate(sequences):
            results[i][sequence] = 1.0

        return results

    @staticmethod
    def one_hot_encode(labels, num_classes=46):
        results = np.zeros((len(labels), num_classes))
        for i, label in enumerate(labels):
            results[i, label] = 1
        return results