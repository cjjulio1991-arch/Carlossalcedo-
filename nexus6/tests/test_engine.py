import unittest
from nexus6.core.hive import HiveKernel
from nexus6.core.brain import DeepCognitiveStack
from nexus6.core.security import SecurityCore

class TestNexusEngine(unittest.TestCase):
    def test_brain_inference(self):
        brain = DeepCognitiveStack(window_size=5)
        initial_state = brain.dqn_state
        result = brain.process_inference()
        self.assertIsInstance(result, float)
        self.assertTrue(0 <= result <= 1.0)
        self.assertEqual(len(brain.recent_states), 2) # initial + 1 update

    def test_security_hash(self):
        security = SecurityCore()
        h1 = security.generate_integrity_hash(0.85)
        h2 = security.generate_integrity_hash(0.85)
        self.assertNotEqual(h1, h2) # Should be unique due to timestamp

    def test_hive_initialization(self):
        hive = HiveKernel(agent_count=10)
        self.assertEqual(len(hive.agents), 10)
        self.assertEqual(hive.health_index, 1.0)

    def test_hive_immunology(self):
        hive = HiveKernel(agent_count=5)
        hive.agents[0].integrity = 0.5
        hive.immunology()
        self.assertGreater(hive.agents[0].integrity, 0.5)

if __name__ == "__main__":
    unittest.main()
