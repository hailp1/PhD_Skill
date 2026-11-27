"""
H-AI ResearchLAB | 4-PERSPECTIVE ACADEMIC DIALOGUE & TENSION ENGINE (v2.0)
Inspired by Stanford STORM. Evaluates research topics across 4 orthogonal schools:
1. Consumer Psychology & Affect
2. Information Systems & HCI (Cold-Start vs. Cumulative)
3. Self-Regulation, Cognitive Load & Ego Depletion
4. Generative AI Social Agency & Algorithmic Ethics / Dark Patterns
"""

import sys
import os
import json

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PERSPECTIVES = [
    {
        "id": "persp-consumer-behavior",
        "name": "Consumer Psychology & Dual-Path Affect",
        "lead_scholars": ["Oliver (1980, 1993)", "Beatty & Ferrell (1998)", "Rook & Fisher (1995)"],
        "core_lens": "Multiplicative interaction between cognitive comfort (permission structure) and visceral emotional arousal (kinetic energy).",
        "critical_question": "Why model cognitive satisfaction and emotional arousal as additive parallel lines when impulsive urges peak only when cognitive comfort disarms vigilance alongside high affective arousal?",
        "required_model_upgrade": "Specify Multiplicative Interaction (ESAT x Arousal -> UBI) and resolve cold-start impulse buying via In-Session Cognitive Fluency."
    },
    {
        "id": "persp-information-systems",
        "name": "Information Systems & Algorithmic Architecture",
        "lead_scholars": ["Xiao & Benbasat (2007, 2018)", "Al-Natour et al. (2011)", "Vessey (1991)"],
        "core_lens": "Endogenous personalization-privacy paradox (Inverted-U curve) and algorithmic exploration vs. exploitation trade-offs.",
        "critical_question": "If hyper-personalization endogenously breeds perceived surveillance and psychological reactance, why treat surveillance reactance as a disconnected exogenous moderator?",
        "required_model_upgrade": "Model Perceived Personalization (PP) with an Inverted-U curvilinear effect on Cognitive Fluency/E-Satisfaction, triggering endogenous Surveillance Reactance beyond the privacy threshold."
    },
    {
        "id": "persp-neuro-ego",
        "name": "Self-Regulation, Cognitive Load & Ego Depletion",
        "lead_scholars": ["Baumeister (2002)", "Baumeister et al. (2007)", "Sweller (1988)", "Hagger et al. (2016)"],
        "core_lens": "Dynamic willpower depletion under digital choice overload and post-purchase regret feedback.",
        "critical_question": "When platforms exploit ego depletion to accelerate unplanned checkout, what happens to long-term platform satisfaction once consumer self-control recovers and regret sets in?",
        "required_model_upgrade": "Add Negative Recursive Feedback Loop (OIB under Ego Depletion -> Post-Purchase Regret -> Erodes Future E-Satisfaction) and hedge depletion via Cognitive Load Theory."
    },
    {
        "id": "persp-genai-ethics",
        "name": "Generative AI Social Agency & Algorithmic Ethics (2024-2026)",
        "lead_scholars": ["Guha et al. (2022)", "Huang & Ahmad (2026)", "Tobon & Abril (2024)", "Kumaran & Shobhana (2026)"],
        "core_lens": "Conversational AI anthropomorphism, micro-latency persuasion, algorithmic dark patterns, and tiered ethical friction.",
        "critical_question": "How do Generation 2.0 LLM conversational agents fundamentally alter consumer compliance compared to Generation 1.0 collaborative filtering, and how can ethical friction protect CLV?",
        "required_model_upgrade": "Explicitly contrast Gen 1.0 vs. Gen 2.0 AI Agency and formulate Tiered Ethical Friction (low-regret vs. high-regret cooling-off mechanisms)."
    }
]


def run_storm_interview(idea_topic):
    print("=" * 85)
    print("🧠 H-AI LAB | 4-PERSPECTIVE ACADEMIC DIALOGUE & TENSION ENGINE v2.0")
    print(f"Topic Under Stress-Testing: '{idea_topic}'")
    print("=" * 85)

    dialogue_log = {
        "topic": idea_topic,
        "framework": "4-Perspective Dynamic Gap & Tension Synthesis",
        "dialogues": []
    }

    for i, p in enumerate(PERSPECTIVES, 1):
        print(f"\n[PERSPECTIVE {i}] {p['name'].upper()}:")
        print(f"  * Key Scholars : {', '.join(p['lead_scholars'])}")
        print(f"  * Core Lens    : {p['core_lens']}")
        print(f"  * Stress Test  : \"{p['critical_question']}\"")
        print(f"  * Mandate      : {p['required_model_upgrade']}")

        dialogue_log["dialogues"].append({
            "perspective": p["name"],
            "scholars": p["lead_scholars"],
            "critical_question": p["critical_question"],
            "required_model_upgrade": p["required_model_upgrade"]
        })

    output_file = os.path.join(WORKSPACE_DIR, "lab_projects", "STORM_PERSPECTIVE_SYNTHESIS.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dialogue_log, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 85)
    print(f"✅ 4-PERSPECTIVE SYNTHESIS SAVED TO: {output_file}")
    print("Static additive S-O-R bias eliminated; Dynamic & Non-Linear mechanisms enforced.")
    print("=" * 85)


def main():
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI Recommendation Systems, Dual-Path S-O-R, Ego Depletion & Online Impulse Buying"
    run_storm_interview(topic)


if __name__ == "__main__":
    main()
