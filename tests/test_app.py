from src.app import translate
from src.language import LanguageEnum


def test_translate() -> None:
	assert translate("good morning", LanguageEnum.PT) == "bom dia"
