from src.language import LanguageEnum


def translator(word: str, language: LanguageEnum) -> str:
	match language:
		case LanguageEnum.ES:
			return _get_spanish_translation(word)
		case LanguageEnum.PT:
			return _get_portuguese_translation(word)
		case _:
			raise NotImplementedError(f'Language "{language}" not implemented.')


ENGLISH_TO_PORTUGUESE = {
	"hello": "ola",
	"goodbye": "tchau",
	"good morning": "bom dia",
	"good afternoon": "boa tarde",
}


def _get_portuguese_translation(word: str) -> str:
	translated_word = ENGLISH_TO_PORTUGUESE.get(word)
	if translated_word is not None:
		return translated_word
	raise NotImplementedError(f'Word "{word}" not implemented.')


ENGLISH_TO_SPANISH = {
	"hello": "hola",
	"goodbye": "adios",
	"good morning": "buenos dias",
	"good afternoon": "buenas tardes",
}


def _get_spanish_translation(word: str) -> str:
	translated_word = ENGLISH_TO_SPANISH.get(word)
	if translated_word is not None:
		return translated_word
	raise NotImplementedError(f'Word "{word}" not implemented.')
