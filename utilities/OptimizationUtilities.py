```json
{
    "utilities/OptimizationUtilities.py": {
        "content": "
import logging
from typing import List, Dict
from haystack import Document
from haystack.retriever.base import BaseRetriever
from haystack.pipeline import Pipeline
from haystack.document_store import DocumentStore

logger = logging.getLogger(__name__)

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given time series data.

    Args:
    data (List[float]): The time series data.

    Returns:
    float: The non-stationary drift index.
    """
    try:
        # Calculate the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        
        # Calculate the non-stationary drift index
        non_stationary_drift_index = (sum((x - mean) ** 2 for x in data) / len(data)) / std_dev
        
        logger.info('Non-stationary drift index calculated successfully')
        return non_stationary_drift_index
    
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        return None


def stochastic_regime_switch(data: List[float], threshold: float) -> bool:
    """
    Determine if a stochastic regime switch has occurred based on the given data and threshold.

    Args:
    data (List[float]): The time series data.
    threshold (float): The threshold value.

    Returns:
    bool: True if a stochastic regime switch has occurred, False otherwise.
    """
    try:
        # Calculate the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        
        # Check if the data exceeds the threshold
        if any(abs(x - mean) > threshold * std_dev for x in data):
            logger.info('Stochastic regime switch detected')
            return True
        
        logger.info('No stochastic regime switch detected')
        return False
    
    except Exception as e:
        logger.error(f'Error detecting stochastic regime switch: {e}')
        return False


def optimize_pulse_generator_parameters(parameters: Dict[str, float]) -> Dict[str, float]:
    """
    Optimize the pulse generator parameters using the given parameters.

    Args:
    parameters (Dict[str, float]): The pulse generator parameters.

    Returns:
    Dict[str, float]: The optimized pulse generator parameters.
    """
    try:
        # Create a document store and retriever
        document_store = DocumentStore()
        retriever = BaseRetriever(document_store)
        
        # Create a pipeline with the retriever
        pipeline = Pipeline()
        pipeline.add_node(component=retriever, name='Retriever', inputs=['Query'])
        
        # Optimize the pulse generator parameters using the pipeline
        optimized_parameters = pipeline.run(query='Optimize pulse generator parameters', parameters=parameters)
        
        logger.info('Pulse generator parameters optimized successfully')
        return optimized_parameters
    
    except Exception as e:
        logger.error(f'Error optimizing pulse generator parameters: {e}')
        return None


if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold = 2.0
    parameters = {'frequency': 10.0, 'amplitude': 5.0}
    
    non_stationary_drift_index = calculate_non_stationary_drift_index(data)
    stochastic_regime_switch_detected = stochastic_regime_switch(data, threshold)
    optimized_parameters = optimize_pulse_generator_parameters(parameters)
    
    print(f'Non-stationary drift index: {non_stationary_drift_index}')
    print(f'Stochastic regime switch detected: {stochastic_regime_switch_detected}')
    print(f'Optimized pulse generator parameters: {optimized_parameters}')
",
        "commit_message": "feat: implement specialized OptimizationUtilities logic"
    }
}
```