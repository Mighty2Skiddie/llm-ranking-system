"""
Main Entry Point
Orchestrates the entire LLM comparison and ranking workflow
"""

from reports.generator import generate_report_data, format_report_text
from reports.pdf_exporter import create_pdf_report


def main():
    """
    Main function that runs the complete workflow:
    1. Generate report data
    2. Create formatted text report
    3. Export to PDF
    """
    print("Starting LLM Comparison and Ranking System...")
    print("-" * 50)
    
    # Step 1: Generate all report data
    print("\n[Step 1] Gathering model data and evaluating...")
    report_data = generate_report_data()
    print("✓ Evaluation complete")
    
    # Step 2: Format text report (optional - for console output)
    print("\n[Step 2] Generating formatted report...")
    report_text = format_report_text(report_data)
    print("✓ Report formatted")
    
    # Optional: Print to console
    print("\n" + report_text)
    
    # Step 3: Export to PDF
    print("[Step 3] Exporting to PDF...")
    pdf_path = create_pdf_report(report_data)
    print(f"✓ PDF generated successfully: {pdf_path}")
    
    print("\n" + "=" * 50)
    print("Process completed successfully!")
    print(f"Your report is ready at: {pdf_path}")


if __name__ == "__main__":
    main()