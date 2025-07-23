import csv, json, pathlib, datetime

csv_path = pathlib.Path("../output/puffy_llm_pack.csv")
jsonld_path = pathlib.Path("../output/puffy_llm_pack.jsonld")

faq_entities = []
with csv_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        faq_entities.append({
            "@type": "Question",
            "name": row["user_question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": row["answer"],
                "url": f"https://puffy.com/{row['source_id']}"
            }
        })

jsonld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faq_entities,
    "publisher": {
        "@type": "Organization",
        "name": "Puffy",
        "url": "https://puffy.com"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "dateModified": datetime.date.today().isoformat()
}

with jsonld_path.open("w", encoding="utf-8") as f:
    json.dump(jsonld, f, ensure_ascii=False, indent=2)

print(f"Created {jsonld_path}")