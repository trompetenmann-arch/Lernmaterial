from worksheet_tool.editing import lint_task_text, rewrite_task_text


def test_rewrite_task_text_polishes_and_punctuates() -> None:
    raw = "zeige z.b. dass fuer alle n in N gilt"
    edited = rewrite_task_text(raw)
    assert edited.endswith(".")
    assert "zum Beispiel" in edited
    assert "ℕ" in edited


def test_lint_unbalanced_parentheses() -> None:
    hints = lint_task_text("Beweise für alle n (in ℕ")
    assert any("Klammern" in hint for hint in hints)
