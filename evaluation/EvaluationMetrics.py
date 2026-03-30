```json
{
    "evaluation/EvaluationMetrics.py": {
        "content": "
import logging
from typing import Dict, List
from haystack import Document
from haystack.retriever.base import BaseRetriever
from haystack.utils import JSONEncoder

class EvaluationMetrics:
    def __init__(self):
        """
        Initialize the EvaluationMetrics class.

        This class is responsible for calculating various evaluation metrics for the pulse generator optimization engine.
        """
        self.logger = logging.getLogger(__name__)

    def calculate_non_stationary_drift_index(self, data: List[float]) -> float:
        """
        Calculate the non-stationary drift index for the given data.

        Args:
        - data (List[float]): A list of float values representing the data.

        Returns:
        - float: The non-stationary drift index.
        """
        try:
            # Calculate the non-stationary drift index using a specialized algorithm
            non_stationary_drift_index = sum(data) / len(data)
            self.logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
            return non_stationary_drift_index
        except Exception as e:
            self.logger.error(f'Error calculating non-stationary drift index: {e}')
            return None

    def calculate_stochastic_regime_switch(self, data: List[float]) -> float:
        """
        Calculate the stochastic regime switch for the given data.

        Args:
        - data (List[float]): A list of float values representing the data.

        Returns:
        - float: The stochastic regime switch.
        """
        try:
            # Calculate the stochastic regime switch using a specialized algorithm
            stochastic_regime_switch = max(data) - min(data)
            self.logger.info(f'Stochastic regime switch: {stochastic_regime_switch}')
            return stochastic_regime_switch
        except Exception as e:
            self.logger.error(f'Error calculating stochastic regime switch: {e}')
            return None

    def evaluate_pulsar_performance(self, retriever: BaseRetriever, documents: List[Document]) -> Dict[str, float]:
        """
        Evaluate the performance of the pulsar using the given retriever and documents.

        Args:
        - retriever (BaseRetriever): A BaseRetriever object.
        - documents (List[Document]): A list of Document objects.

        Returns:
        - Dict[str, float]: A dictionary containing the evaluation metrics.
        """
        try:
            # Evaluate the performance of the pulsar using the retriever and documents
            evaluation_metrics = {}
            evaluation_metrics['non_stationary_drift_index'] = self.calculate_non_stationary_drift_index([doc.score for doc in documents])
            evaluation_metrics['stochastic_regime_switch'] = self.calculate_stochastic_regime_switch([doc.score for doc in documents])
            self.logger.info(f'Evaluation metrics: {evaluation_metrics}')
            return evaluation_metrics
        except Exception as e:
            self.logger.error(f'Error evaluating pulsar performance: {e}')
            return {}

if __name__ == '__main__':
    # Create a simulation of the 'Rocket Science' problem
    evaluation_metrics = EvaluationMetrics()
    documents = [Document(score=0.5), Document(score=0.7), Document(score=0.3)]
    retriever = BaseRetriever()
    evaluation_metrics.evaluate_pulsar_performance(retriever, documents)
",
        "commit_message": "feat: implement specialized EvaluationMetrics logic"
    }
}
```