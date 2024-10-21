import unittest


def bin_reallocation(predictions, threshold=0.5):
    audit_trail = []
    reallocated_bins = []

    for bin_id, prediction in enumerate(predictions):
        action = "Reallocate" if prediction >= threshold else "Keep"
        audit_trail.append({"bin_id": bin_id, "prediction": prediction, "action": action})
        if action == "Reallocate":
            reallocated_bins.append(bin_id)

    return reallocated_bins, audit_trail


class TestBinReallocation(unittest.TestCase):

    def test_bin_reallocation(self):
        predictions = [0.6, 0.3, 0.8, 0.4, 0.7]
        expected_reallocated_bins = [0, 2, 4]
        expected_audit_trail = [
            {"bin_id": 0, "prediction": 0.6, "action": "Reallocate"},
            {"bin_id": 1, "prediction": 0.3, "action": "Keep"},
            {"bin_id": 2, "prediction": 0.8, "action": "Reallocate"},
            {"bin_id": 3, "prediction": 0.4, "action": "Keep"},
            {"bin_id": 4, "prediction": 0.7, "action": "Reallocate"}
        ]
        reallocated_bins, audit_trail = bin_reallocation(predictions)
        self.assertEqual(reallocated_bins, expected_reallocated_bins, "Reallocated bins incorrect")
        self.assertEqual(audit_trail, expected_audit_trail, "Audit trail incorrect")

    def test_no_predictions(self):
        predictions = []
        expected_reallocated_bins = []
        expected_audit_trail = []
        reallocated_bins, audit_trail = bin_reallocation(predictions)
        self.assertEqual(reallocated_bins, expected_reallocated_bins,
                         "Reallocated bins should be empty for no predictions")
        self.assertEqual(audit_trail, expected_audit_trail, "Audit trail should be empty for no predictions")

    def test_all_predictions_below_threshold(self):
        predictions = [0.3, 0.2, 0.4]
        threshold = 0.5
        expected_reallocated_bins = []
        expected_audit_trail = [
            {"bin_id": 0, "prediction": 0.3, "action": "Keep"},
            {"bin_id": 1, "prediction": 0.2, "action": "Keep"},
            {"bin_id": 2, "prediction": 0.4, "action": "Keep"}
        ]
        reallocated_bins, audit_trail = bin_reallocation(predictions, threshold)
        self.assertEqual(reallocated_bins, expected_reallocated_bins,
                         "Reallocated bins incorrect for all predictions below threshold")
        self.assertEqual(audit_trail, expected_audit_trail, "Audit trail incorrect for all predictions below threshold")


if __name__ == "__main__":
    unittest.main()
