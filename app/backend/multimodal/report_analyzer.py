
import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from llm import generate_report_analysis


def analyze_report(report_text):
    return generate_report_analysis(report_text)

