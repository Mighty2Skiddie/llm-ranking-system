
# LLM Comparison and Ranking System

A comprehensive Python-based system for evaluating, scoring, and ranking Large Language Models (LLMs) using weighted criteria analysis with automated PDF report generation.

## Table of Contents

- [Overview](#overview)
- [Why This Project](#why-this-project)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Customization](#customization)
- [Output](#output)
- [Technical Details](#technical-details)

## Overview

This system evaluates five major LLM models (GPT-4o, Claude, Gemini, LLaMA 3, and Mistral) across multiple criteria and generates a professional PDF report with rankings, scores, advantages, disadvantages, and justifications.

The evaluation uses a weighted scoring methodology where each model is assessed on:
- Performance (30%)
- Cost Efficiency (25%)
- Ease of Use (20%)
- Customization (15%)
- Support & Documentation (10%)

## Why This Project

### The Problem

With the rapid proliferation of LLMs, developers and organizations face analysis paralysis when selecting the right model for their use case. Each model has different strengths, costs, and trade-offs that aren't immediately obvious.

### The Solution

This system provides:

1. **Objective Comparison Framework** - Standardized criteria for fair evaluation
2. **Weighted Scoring** - Prioritizes what matters most (customizable)
3. **Comprehensive Analysis** - Not just scores, but pros/cons and context
4. **Professional Reporting** - Automated PDF generation for presentations and documentation
5. **Transparency** - All scoring logic is visible and modifiable

### Use Cases

- **Academic Research** - Compare models for research papers or assignments
- **Business Decision-Making** - Help teams select the right LLM for projects
- **Personal Learning** - Understand the LLM landscape and trade-offs
- **Documentation** - Generate reports for stakeholders or management

## Features

### Core Capabilities

- ✅ Multi-criteria evaluation with configurable weights
- ✅ Weighted scoring algorithm (0-10 scale)
- ✅ Automatic ranking based on total scores
- ✅ Detailed advantage/disadvantage analysis
- ✅ Comfort level assessment for each model
- ✅ Professional PDF report generation
- ✅ Clean, modular, maintainable codebase

### Report Features

- 📊 Summary ranking table with scores and comfort levels
- 📋 Detailed analysis for each model
- 📝 3 advantages and 3 disadvantages per model
- 💡 Justification for each ranking
- 🎨 Professional formatting with tables and colors
- 📄 Export to PDF for easy sharing

## Architecture

### Design Principles

The project follows a **layered architecture** with clear separation of concerns:

```
┌─────────────────────────────────────┐
│         Presentation Layer          │
│    (PDF Export, Report Display)     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│         Business Logic Layer        │
│   (Evaluation, Ranking, Scoring)    │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│           Data Layer                │
│      (Model Information Store)      │
└─────────────────────────────────────┘
```

### Component Breakdown

#### 1. Data Layer (`models/`)

**Purpose**: Centralized storage of LLM information

- `llm_data.py` - Contains model definitions, advantages, disadvantages, and comfort levels
- Single source of truth for all model data
- Easy to add new models or update existing ones

#### 2. Business Logic Layer (`core/`)

**Purpose**: Implements evaluation and ranking algorithms

- `evaluator.py` - Defines criteria, weights, and calculates weighted scores
- `ranker.py` - Sorts models by score and provides ranking justifications
- Pure business logic with no UI dependencies

#### 3. Presentation Layer (`reports/`)

**Purpose**: Formats and exports results

- `generator.py` - Combines data and creates formatted text reports
- `pdf_exporter.py` - Generates professional PDF documents using ReportLab
- Handles all presentation concerns

#### 4. Orchestration (`main.py`)

**Purpose**: Coordinates the entire workflow

- Entry point for the application
- Manages the execution pipeline
- Provides user feedback and error handling

#### 5. Configuration (`config.py`)

**Purpose**: Centralizes all configurable settings

- PDF formatting options
- Color schemes
- Output paths
- Makes customization easier without touching core logic

### Data Flow

```
┌──────────────┐
│  main.py     │ ← Entry Point
└──────┬───────┘
       ↓
┌──────────────────────────────────────┐
│  reports/generator.py                │
│  - Calls get_llm_models()            │
│  - Calls evaluate_all_models()       │
│  - Calls rank_models()               │
└──────┬───────────────────────────────┘
       ↓
┌──────────────────────────────────────┐
│  reports/pdf_exporter.py             │
│  - Receives compiled report data     │
│  - Formats using ReportLab           │
│  - Exports to PDF                    │
└──────┬───────────────────────────────┘
       ↓
┌──────────────────────────────────────┐
│  output/assignment.pdf               │ ← Final Output
└──────────────────────────────────────┘
```

### Algorithm: Weighted Scoring

```
For each model:
    weighted_score = 0
    
    For each criterion:
        weighted_score += (raw_score × criterion_weight)
    
    Round to 2 decimal places
    
Sort models by weighted_score (descending)
Assign ranks 1, 2, 3, etc.
```

**Example Calculation for GPT-4o:**

```
Performance:    9.5 × 0.30 = 2.85
Cost:           6.0 × 0.25 = 1.50
Ease of Use:    9.0 × 0.20 = 1.80
Customization:  6.5 × 0.15 = 0.975
Documentation:  9.0 × 0.10 = 0.90
                        ──────
Total Score:              8.03
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download

```bash
# If using git
git clone <repository-url>
cd llm-ranking-system

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `reportlab==4.0.7` - PDF generation library

### Step 4: Verify Installation

```bash
python main.py
```

If successful, you'll see:

```
Starting LLM Comparison and Ranking System...
--------------------------------------------------

[Step 1] Gathering model data and evaluating...
✓ Evaluation complete

[Step 2] Generating formatted report...
✓ Report formatted

[Step 3] Exporting to PDF...
✓ PDF generated successfully: output/assignment.pdf

==================================================
Process completed successfully!
Your report is ready at: output/assignment.pdf
```

## Usage

### Basic Usage

```bash
python main.py
```

This generates `output/assignment.pdf` with the complete ranking report.

### Preview Mode

```bash
python main.py --preview
```

Shows the formatted text report in the console before generating PDF.

### Custom Output Path

Edit `config.py`:

```python
OUTPUT_DIR = "my_reports"
PDF_FILENAME = "llm_analysis_2024.pdf"
```

## Project Structure

```
llm-ranking-system/
│
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── config.py                # Configuration settings
├── main.py                  # Entry point
│
├── models/                  # Data Layer
│   ├── __init__.py
│   └── llm_data.py         # LLM definitions and properties
│
├── core/                    # Business Logic Layer
│   ├── __init__.py
│   ├── evaluator.py        # Scoring and evaluation logic
│   └── ranker.py           # Ranking and justifications
│
├── reports/                 # Presentation Layer
│   ├── __init__.py
│   ├── generator.py        # Report formatting
│   └── pdf_exporter.py     # PDF generation
│
└── output/                  # Generated files
    ├── .gitkeep
    └── assignment.pdf       # Generated report (not in git)
```

## Configuration

### Modify Evaluation Criteria

Edit `core/evaluator.py`:

```python
def get_evaluation_criteria():
    criteria = {
        "Performance": 0.40,        # Change weights here
        "Cost Efficiency": 0.30,    # Must sum to 1.0
        "Ease of Use": 0.15,
        "Customization": 0.10,
        "Support & Documentation": 0.05
    }
    return criteria
```

### Modify Scores

Edit `core/evaluator.py` in `get_model_scores()` function:

```python
"GPT-4o": {
    "Performance": 9.5,      # Adjust scores here (0-10)
    "Cost Efficiency": 6.0,
    # ... etc
}
```

### Modify PDF Styling

Edit `config.py`:

```python
PRIMARY_COLOR = "#3498db"      # Change colors
TITLE_FONT_SIZE = 24           # Change font sizes
MARGIN_INCH = 0.5              # Change margins
```

## Customization

### Add a New Model

1. Edit `models/llm_data.py`:

```python
"Cohere": {
    "advantages": [
        "Advantage 1",
        "Advantage 2",
        "Advantage 3"
    ],
    "disadvantages": [
        "Disadvantage 1",
        "Disadvantage 2",
        "Disadvantage 3"
    ],
    "comfort_level": "Medium"
}
```

2. Edit `core/evaluator.py` and add scores:

```python
"Cohere": {
    "Performance": 7.5,
    "Cost Efficiency": 8.0,
    "Ease of Use": 7.0,
    "Customization": 7.5,
    "Support & Documentation": 7.0
}
```

3. Edit `core/ranker.py` and add justification:

```python
"Cohere": "Strong enterprise features but limited adoption compared to market leaders."
```

### Add New Criteria

1. Edit `core/evaluator.py`:

```python
def get_evaluation_criteria():
    criteria = {
        "Performance": 0.25,
        "Cost Efficiency": 0.20,
        "Ease of Use": 0.20,
        "Customization": 0.15,
        "Support & Documentation": 0.10,
        "Security": 0.10         # New criterion
    }
    return criteria
```

2. Add scores for all models:

```python
"GPT-4o": {
    # ... existing criteria
    "Security": 8.5
}
```

## Output

### PDF Report Contents

1. **Title Page**
   - Report title
   - Clean, professional header

2. **Overall Rankings Table**
   - Rank number
   - Model name
   - Weighted score (X/10)
   - Comfort level

3. **Detailed Analysis** (for each model)
   - Model name and rank
   - Overall score
   - 3 Advantages (bullet points)
   - 3 Disadvantages (bullet points)
   - Ranking justification (1-2 sentences)

### Sample Output

```
================================================================================
OVERALL RANKINGS
--------------------------------------------------------------------------------
#1. GPT-4o - Score: 8.03/10
#2. Claude - Score: 7.78/10
#3. Gemini - Score: 7.63/10
#4. LLaMA 3 - Score: 7.43/10
#5. Mistral - Score: 7.15/10
```

## Technical Details

### Dependencies

- **ReportLab 4.0.7** - PDF generation
  - Handles tables, paragraphs, styling
  - Professional document formatting
  - No external dependencies required

### Python Version

- Tested on Python 3.7+
- Compatible with Python 3.8, 3.9, 3.10, 3.11

### Performance

- Execution time: < 2 seconds
- PDF size: ~50-100 KB
- Memory usage: Minimal (< 50 MB)

### Code Quality

- **Modular design** - Easy to maintain and extend
- **Type hints** - Clear function signatures
- **Docstrings** - Every function documented
- **Comments** - Explains reasoning and logic
- **No external API calls** - Runs completely offline
- **Error handling** - Graceful failure with helpful messages

### Limitations

- Static data (not fetching live benchmarks)
- Subjective scoring (based on research, not automated testing)
- Limited to 5 models (easily extendable)
- Single evaluation run (not comparative over time)

## Troubleshooting

### "No module named reportlab"

```bash
pip install reportlab
```

### PDF not generating

- Check that `output/` directory exists
- Verify write permissions
- Check console for error messages

### Scores don't sum correctly

- Ensure criteria weights sum to 1.0 in `evaluator.py`
- Check the assertion in `get_evaluation_criteria()`

## Future Enhancements

Possible improvements (not implemented):

- [ ] Live benchmark data fetching
- [ ] Interactive web interface
- [ ] Comparison graphs and charts
- [ ] Export to Excel/CSV
- [ ] Model cost calculator
- [ ] Custom criteria builder
- [ ] Historical tracking

---

**Created for academic assignment purposes**  
