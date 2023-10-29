import logging
import unittest

# Configure logging globally
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Trace Route Transaction Code
def trace_transaction(transaction_id, step, message):
    logger.info(f"Transaction ID: {transaction_id}, Step: {step}, Message: {message}")

# Your application code
def some_function():
    transaction_id = "123"
    logger.info("Starting some_function")
    # Perform some actions
    logger.info("Action completed")
    trace_transaction(transaction_id, "Step 1", "Action completed")

# Create Test Cases
class TestLogging(unittest.TestCase):
    def test_log_output(self):
        with self.assertLogs(__name__, level="INFO") as log_context:
            some_function()

        log_output = "\n".join(log_context.output)
        self.assertIn("Starting some_function", log_output)
        self.assertIn("Action completed", log_output)
        self.assertIn("Transaction ID: 123, Step: Step 1, Message: Action completed", log_output)

if __name__ == "__main__":
    unittest.main()
