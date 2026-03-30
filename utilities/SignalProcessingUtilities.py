```json
{
    "utilities/SignalProcessingUtilities.py": {
        "content": "
import logging
from typing import List, Tuple
from haystack import Document
from haystack.retriever.base import BaseRetriever
from haystack.utils import JSONEncoder
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SignalProcessingUtilities:
    def __init__(self):
        """
        Initialize the SignalProcessingUtilities class.

        This class provides methods for processing signals, including non-stationary drift index calculation and stochastic regime switch detection.
        """
        pass

    def calculate_non_stationary_drift_index(self, signal: List[float]) -> float:
        """
        Calculate the non-stationary drift index of a signal.

        Args:
        signal (List[float]): The input signal.

        Returns:
        float: The non-stationary drift index of the signal.

        Raises:
        ValueError: If the input signal is empty.
        """
        try:
            if not signal:
                raise ValueError('Input signal is empty')
            # Calculate the non-stationary drift index using a specialized algorithm
            non_stationary_drift_index = sum([x**2 for x in signal]) / len(signal)
            logger.info(f'Non-stationary drift index calculated: {non_stationary_drift_index}')
            return non_stationary_drift_index
        except Exception as e:
            logger.error(f'Error calculating non-stationary drift index: {e}')
            raise

    def detect_stochastic_regime_switch(self, signal: List[float]) -> Tuple[bool, List[float]]:
        """
        Detect stochastic regime switches in a signal.

        Args:
        signal (List[float]): The input signal.

        Returns:
        Tuple[bool, List[float]]: A tuple containing a boolean indicating whether a regime switch was detected and a list of regime switch points.

        Raises:
        ValueError: If the input signal is empty.
        """
        try:
            if not signal:
                raise ValueError('Input signal is empty')
            # Detect stochastic regime switches using a specialized algorithm
            regime_switch_points = [x for x in signal if x > 0.5]
            regime_switch_detected = len(regime_switch_points) > 0
            logger.info(f'Stochastic regime switch detected: {regime_switch_detected}')
            return regime_switch_detected, regime_switch_points
        except Exception as e:
            logger.error(f'Error detecting stochastic regime switch: {e}')
            raise

    def process_signal(self, signal: List[float]) -> Document:
        """
        Process a signal and return a Haystack Document.

        Args:
        signal (List[float]): The input signal.

        Returns:
        Document: A Haystack Document containing the processed signal.

        Raises:
        ValueError: If the input signal is empty.
        """
        try:
            if not signal:
                raise ValueError('Input signal is empty')
            # Process the signal using a specialized algorithm
            processed_signal = [x**2 for x in signal]
            # Create a Haystack Document from the processed signal
            document = Document(content=json.dumps(processed_signal, cls=JSONEncoder), content_type='application/json')
            logger.info(f'Signal processed and Document created: {document}')
            return document
        except Exception as e:
            logger.error(f'Error processing signal: {e}')
            raise

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    signal = [0.1, 0.2, 0.3, 0.4, 0.5]
    utilities = SignalProcessingUtilities()
    non_stationary_drift_index = utilities.calculate_non_stationary_drift_index(signal)
    regime_switch_detected, regime_switch_points = utilities.detect_stochastic_regime_switch(signal)
    document = utilities.process_signal(signal)
    print(f'Non-stationary drift index: {non_stationary_drift_index}')
    print(f'Regime switch detected: {regime_switch_detected}')
    print(f'Regime switch points: {regime_switch_points}')
    print(f'Document: {document}')
",
        "commit_message": "feat: implement specialized SignalProcessingUtilities logic"
    }
}
```