
from models.llm_data import get_llm_models
from core.evaluator import evaluate_all_models
from core.ranker import rank_models, get_ranking_justification


def generate_report_data():
    
    models_data = get_llm_models()
    evaluated_scores = evaluate_all_models()
    ranked_models = rank_models(evaluated_scores)
    
    report_data = {
        "models": models_data,
        "scores": evaluated_scores,
        "rankings": ranked_models
    }
    
    return report_data


def format_report_text(report_data):
    
    text = "=" * 80 + "\n"
    text += "LLM COMPARISON AND RANKING REPORT\n"
    text += "=" * 80 + "\n\n"
    
    # Add rankings overview
    text += "OVERALL RANKINGS\n"
    text += "-" * 80 + "\n"
    for rank, model_name, score in report_data["rankings"]:
        text += f"#{rank}. {model_name} - Score: {score}/10\n"
    
    text += "\n" + "=" * 80 + "\n\n"
    
    # Add detailed information for each model
    text += "DETAILED MODEL ANALYSIS\n"
    text += "=" * 80 + "\n\n"
    
    for rank, model_name, score in report_data["rankings"]:
        model_info = report_data["models"][model_name]
        
        text += f"RANK #{rank}: {model_name}\n"
        text += "-" * 80 + "\n"
        text += f"Overall Score: {score}/10\n"
        text += f"Comfort Level: {model_info['comfort_level']}\n\n"
        
        text += "Advantages:\n"
        for i, adv in enumerate(model_info["advantages"], 1):
            text += f"  {i}. {adv}\n"
        
        text += "\nDisadvantages:\n"
        for i, dis in enumerate(model_info["disadvantages"], 1):
            text += f"  {i}. {dis}\n"
        
        text += "\nJustification:\n"
        text += f"  {get_ranking_justification(rank, model_name)}\n"
        
        text += "\n" + "=" * 80 + "\n\n"
    
    return text