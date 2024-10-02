import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script with multiple inputs
        command = ["python", "braille_translator.py", "Abc", "123", "xYz"]

        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output for 'Abc 123 xYz' translation into Braille
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

        # Strip any leading/trailing whitespace from the output and compare with expected output
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()