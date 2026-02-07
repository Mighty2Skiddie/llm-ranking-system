

def get_llm_models():
    
    models = {
        "GPT-4o": {
            "advantages": [
                "Excellent reasoning and problem-solving capabilities",
                "Strong multimodal support (text, images, audio)",
                "Fast response times with optimized architecture"
            ],
            "disadvantages": [
                "Expensive API pricing for high-volume usage",
                "Requires internet connection and API key",
                "Limited customization for specialized domains"
            ],
            "comfort_level": "High"
        },
        "Claude": {
            "advantages": [
                "Superior long-context understanding (200K+ tokens)",
                "Strong ethical alignment and safety features",
                "Excellent at following complex instructions"
            ],
            "disadvantages": [
                "Limited availability in some regions",
                "Fewer third-party integrations compared to GPT",
                "Can be overly cautious in responses"
            ],
            "comfort_level": "High"
        },
        "Gemini": {
            "advantages": [
                "Deep integration with Google services and tools",
                "Strong performance on technical and coding tasks",
                "Multimodal capabilities with image understanding"
            ],
            "disadvantages": [
                "Less consistent quality compared to GPT-4o and Claude",
                "Privacy concerns with Google data integration",
                "Limited documentation for advanced use cases"
            ],
            "comfort_level": "Medium"
        },
        "LLaMA 3": {
            "advantages": [
                "Open-source and fully customizable",
                "Can be run locally without API costs",
                "Strong community support and frequent updates"
            ],
            "disadvantages": [
                "Requires significant computational resources",
                "Complex setup and deployment process",
                "Lower performance than proprietary models on complex tasks"
            ],
            "comfort_level": "Medium"
        },
        "Mistral": {
            "advantages": [
                "Excellent performance-to-size ratio",
                "Open-source with commercial-friendly licensing",
                "Efficient inference and lower resource requirements"
            ],
            "disadvantages": [
                "Smaller context window than competitors",
                "Less established ecosystem and tooling",
                "Limited multilingual capabilities"
            ],
            "comfort_level": "Low"
        }
    }
    
    return models