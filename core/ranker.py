"""
Ranker Module
Ranks models based on their weighted scores
"""

def rank_models(evaluated_scores):
    """
    Sorts models by their scores in descending order and assigns ranks
    
    Args:
        evaluated_scores (dict): Model names and their weighted scores
    
    Returns:
        list: List of tuples (rank, model_name, score) sorted by rank
    """
    # Sort models by score in descending order (highest score first)
    sorted_models = sorted(evaluated_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Create ranked list with rank numbers
    ranked_models = []
    for rank, (model_name, score) in enumerate(sorted_models, start=1):
        ranked_models.append((rank, model_name, score))
    
    return ranked_models


def get_ranking_justification(rank, model_name):
    """
    Provides a brief justification for each model's ranking
    
    Args:
        rank (int): The rank position of the model
        model_name (str): Name of the model
    
    Returns:
        str: One or two line justification
    """
    justifications = {
        "GPT-4o": "Top performance and ease of use offset higher costs, making it ideal for production.",
        "Claude": "Excellent long-context handling and safety features make it reliable for complex tasks.",
        "Gemini": "Balanced performance with Google integration, suitable for general-purpose applications.",
        "LLaMA 3": "Strong customization and cost benefits, but requires technical expertise to deploy.",
        "Mistral": "Efficient and open-source, but limited context and ecosystem maturity hold it back."
    }
    
    return justifications.get(model_name, "Solid choice for specific use cases.")