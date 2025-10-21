import json

def combine_summaries(agent_outputs):
    """
    Combines all agent outputs (dicts or strings) into a clear, sectioned narrative.
    Automatically formats Clinical Trials data into readable bullet points.
    """

    sections = [
        "📊 Market Insights",
        "🧪 Clinical Trials",
        "⚖️ Patent Landscape",
        "🌍 Trade Insights",
        "🧠 Internal Knowledge",
        "🌐 Web Intelligence"
    ]

    final_report = []

    for i, output in enumerate(agent_outputs):
        title = sections[i] if i < len(sections) else f"Section {i+1}"
        final_report.append(f"\n\n{title}\n{'-' * len(title)}")

        # --- Handle dictionaries ---
        if isinstance(output, dict):
            # Handle API errors
            if "error" in output:
                final_report.append(f"⚠️ Error: {output['error']}")
                continue

            data = output.get("data", {})

            # 🎯 Clinical trials pretty-print
            if "studies" in data:
                trials = data["studies"]
                if not trials:
                    final_report.append("No active or completed trials found.")
                else:
                    for idx, t in enumerate(trials, start=1):
                        final_report.append(
                            f"\n• {idx}. {t.get('Title', 'Untitled Study')}\n"
                            f"   ├─ Phase: {t.get('Phase', 'N/A')} | Status: {t.get('OverallStatus', 'N/A')}\n"
                            f"   ├─ Sponsor: {t.get('SponsorName', 'N/A')}\n"
                            f"   ├─ Country: {t.get('LocationCountry', 'N/A')}\n"
                            f"   ├─ Start: {t.get('StartDate', 'N/A')} | Completion: {t.get('CompletionDate', 'N/A')}\n"
                        )
            else:
                # Generic dict pretty-print
                formatted = json.dumps(output, indent=2)
                final_report.append(formatted)

        # --- Handle plain text ---
        elif isinstance(output, str):
            final_report.append(output.strip())

        # --- Handle lists ---
        elif isinstance(output, list):
            final_report.append("\n".join(map(str, output)))

        # --- Fallback ---
        else:
            final_report.append(str(output))

    # Combine all sections
    return "\n".join(final_report)
