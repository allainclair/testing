from src.language import LanguageEnum
from src.service import translator


def translate(word: str, language: LanguageEnum) -> str:
	return translator(word, language)
