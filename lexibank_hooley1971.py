import dataclasses
from pathlib import Path
from typing import Optional

from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset, FormSpec, Language as BaseLanguage, Lexeme as BaseLexeme


@dataclasses.dataclass
class Language(BaseLanguage):
    Note: Optional[str] = None


@dataclasses.dataclass
class Lexeme(BaseLexeme):
    # Confidence of the PDF extraction: HIGH (OCR-verified), MED (visual-only marks),
    # MANUAL (checked by an editor against the print). See raw/README.md.
    Extraction_Confidence: Optional[str] = None


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "hooley1971"
    language_class = Language
    lexeme_class = Lexeme

    form_spec = FormSpec(
        separators="",  # one form per cell; spaces are word boundaries within a form
        missing_data=("—",),
        replacements=[(" ", "_")],
        first_form_only=True,
    )

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        args.writer.add_sources()
        languages = args.writer.add_languages(lookup_factory="Name")
        concepts = args.writer.add_concepts(
            id_factory=lambda c: f"{c.number}_{slug(c.english)}", lookup_factory="english")
        for row in filter(None, self.raw_dir.read_csv("Hooley1971_lexical.txt")):
            language, gloss, value, cognate, confidence = row
            for lex in args.writer.add_forms_from_value(
                Language_ID=languages[language],
                Parameter_ID=concepts[gloss],
                Value=value,
                Source=["Hooley1971"],
                Cognacy=cognate or None,
                Extraction_Confidence=confidence,
            ):
                if cognate:
                    args.writer.add_cognate(
                        lexeme=lex, Cognateset_ID=f"{concepts[gloss]}-{cognate}", Source=["Hooley1971"])
