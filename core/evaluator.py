

def evaluation():
    
    criteria = {
        "Performance": 0.30,      
        "Cost Efficiency": 0.25,  
        "Ease of Use": 0.20,      
        "Customization": 0.15,    
        "Support & Documentation": 0.10  
    }
    
    return criteria


def model_scores():
    
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


def weighted_score(model_name, criteria_weights, model_scores):
   
    total_score = 0.0
    
    
    for criterion, weight in criteria_weights.items():
        score = model_scores[model_name][criterion]
        total_score += score * weight
    
    return round(total_score, 2)


def evaluate_all_models():
    
    criteria = evaluation()
    scores = model_scores()
    results = {}
    
    
    for model_name in scores.keys():
        results[model_name] = weighted_score(model_name, criteria, scores)
    
    return results