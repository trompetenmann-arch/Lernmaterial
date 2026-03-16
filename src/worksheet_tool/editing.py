from __future__ import annotations

import re

COMMON_REPLACEMENTS = {
    " z.b. ": " zum Beispiel ",
    " bzgl. ": " bezüglich ",
    " d.h. ": " das heißt ",
}


def rewrite_task_text(raw_text: str) -> str:
    """Lightweight redaction of rough task descriptions into polished German text."""
    text = f" {raw_text.strip()} "
    text = re.sub(r"\s+", " ", text)

    for source, target in COMMON_REPLACEMENTS.items():
        text = text.replace(source, target)

    text = text.strip()
    if not text:
        return text

    text = text[0].upper() + text[1:]

    if text[-1] not in {".", "!", "?"}:
        text += "."

    text = _normalize_math_notation(text)
    return text


def _normalize_math_notation(text: str) -> str:
    text = re.sub(r"\bf\s*\(\s*x\s*\)", "f(x)", text)
    text = re.sub(r"\bR\b", "ℝ", text)
    text = re.sub(r"\bN\b", "ℕ", text)
    text = re.sub(r"\bZ\b", "ℤ", text)
    return text


def lint_task_text(text: str) -> list[str]:
    """Simple consistency hints for mathematically phrased exercises."""
    hints: list[str] = []
    if "sei" in text.lower() and "gegeben" not in text.lower():
        hints.append("Prüfe, ob Annahmen klar mit 'gegeben' spezifiziert sind.")
    if "beweise" in text.lower() and "für alle" not in text.lower():
        hints.append("Bei Beweisaufgaben ggf. Quantoren explizit angeben ('für alle ...').")
    if text.count("(") != text.count(")"):
        hints.append("Klammern sind nicht ausgeglichen.")
    return hints
