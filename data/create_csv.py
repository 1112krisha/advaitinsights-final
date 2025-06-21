import pandas as pd

data = {
    "Company Name": ["Genentech", "Pfizer", "Advait Theragnostics"],
    "What Happened": [
        "Announced breakthrough in protein biomarker detection",
        "Launched AI-powered drug prediction platform",
        "Initiated new metabolomics research in plant-based compounds"
    ],
    "Date": ["2025-06-20", "2025-06-18", "2025-06-21"],
    "Category": ["Biomarkers", "Drug Discovery", "Metabolomics"],
    "Priority": ["High", "Medium", "High"],
    "Insight Type": ["Launch", "Tech Update", "Research"],
    "AI Summary": [
        "New detection tech improves protein tracking in early disease stage.",
        "AI model predicts drug interactions with 89% accuracy.",
        "Focus on metabolite mapping for gut-plant-human interactions."
    ],
    "Advait Angle": [
        "Can explore compatibility with Advait’s antibody platforms.",
        "Opportunity to test against Advait’s metabolic gene datasets.",
        "Adds strong rationale to plant-based vertical of Advait pipeline."
    ],
    "Source Link": [
        "https://example.com/genentech-news",
        "https://example.com/pfizer-ai-platform",
        "https://advaittheragnostics.com/news"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data/insights_data.csv", index=False)
