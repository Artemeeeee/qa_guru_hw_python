def clean_text(text: str) -> str:
    """Заменяет \t и \n на пробелы, лишние пробелы обрезает."""
    if not text:
        return ""
    cleaned = text.replace('\t', ' ').replace('\n', ' ')
    cleaned = ' '.join(cleaned.split())
    return cleaned