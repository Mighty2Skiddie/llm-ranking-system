"""
Evaluator Module
Defines evaluation criteria and computes weighted scores for each model
"""

def evaluation():
    """
    Returns evaluation criteria with their weights
    Weights must sum to 1.0 (100%)
    
    Returns:
        dict: Criteria names as keys and their weights as values
    """
    criteria = {
        "Performance": 0.30,      # 30% weight
        "Cost Efficiency": 0.25,  # 25% weight
        "Ease of Use": 0.20,      # 20% weight
        "Customization": 0.15,    # 15% weight
        "Support & Documentation": 0.10  # 10% weight
    }
    
    return criteria


def get_model_scores():
    """
    Returns raw scores (0-10) for each model across all criteria
    
    Returns:
        dict: Model names as keys and their criteria scores as values
    """
    scores = {
        "GPT-4o": {
            "Performance": 9.5,
            "Cost Efficiency": 6.0,
            "Ease of Use": 9.0,
            "Customization": 6.5,
            "Support & Documentation": 9.0
        },
        "Claude": {
            "Performance": 9.0,
            "Cost Efficiency": 6.5,
            "Ease of Use": 8.5,
            "Customization": 6.0,
            "Support & Documentation": 8.5
        },
        "Gemini": {
            "Performance": 8.0,
            "Cost Efficiency": 7.5,
            "Ease of Use": 8.0,
            "Customization": 7.0,
            "Support & Documentation": 7.5
        },
        "LLaMA 3": {
            "Performance": 7.5,
            "Cost Efficiency": 9.0,
            "Ease of Use": 5.0,
            "Customization": 9.5,
            "Support & Documentation": 7.0
        },
        "Mistral": {
            "Performance": 7.0,
            "Cost Efficiency": 8.5,
            "Ease of Use": 6.0,
            "Customization": 8.0,
            "Support & Documentation": 6.5
        }
    }
    
    return scores


def calculate_weighted_score(model_name, criteria_weights, model_scores):
    """
    Calculates the weighted total score for a single model
    
    Args:
        model_name (str): Name of the model
        criteria_weights (dict): Weights for each criterion
        model_scores (dict): Raw scores for the model
    
    Returns:
        float: Weighted total score (0-10 scale)
    """
    total_score = 0.0
    
    # Multiply each criterion score by its weight and sum them
    for criterion, weight in criteria_weights.items():
        score = model_scores[model_name][criterion]
        total_score += score * weight
    
    return round(total_score, 2)


def evaluate_all_models():
    """
    Evaluates all models and returns their weighted scores
    
    Returns:
        dict: Model names as keys and their weighted scores as values
    """
    criteria = evaluation()
    scores = get_model_scores()
    results = {}
    
    # Calculate weighted score for each model
    for model_name in scores.keys():
        results[model_name] = calculate_weighted_score(model_name, criteria, scores)
    
    return results