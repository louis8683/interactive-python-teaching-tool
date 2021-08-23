import json

from PySide6.QtGui import QFont


class Settings:
    def __init__(self, settings_filename="settings.json"):
        self.load(settings_filename)

    def load(self, settings_filename="settings.json"):
        self.filename = settings_filename
        with open(settings_filename, "r", encoding="UTF-8") as file:
            self.json = json.load(file)
        
        self.font = {}

        # load the settings into Qt objects
        self.font["ui"] = self._load_font("ui")
        self.font["editor"] = self._load_font("editor")
        self.path = self._load_path()
    
    def save(self, filename=None):
        if filename is None:
            filename = self.filename
        with open(self.filename, "w") as file:
            json.dump(self.json, file, indent=4)
    
    def _load_path(self) -> dict[str, str]:
        return self.json["path"]
    
    def _load_font(self, key: str) -> QFont:
        font_setting = self.json["font"][key]
        font = QFont()
        if "bold" in font_setting: font.setBold(font_setting["bold"])
        if "capitalization" in font_setting: eval(f"font.setCapitalization(QFont.{font_setting['capitalization']})")
        if "families" in font_setting: font.setFamilies(font_setting["families"])
        if "family" in font_setting: font.setFamily(font_setting["family"])
        if "fixed_pitch" in font_setting: font.setFixedPitch(font_setting["fixed_pitch"])
        if "hinting_preference" in font_setting: eval(f"font.setHintingPreference(QFont.{font_setting['hinting_preference']})")
        if "italic" in font_setting: font.setItalic(font_setting["italic"])
        if "kerning" in font_setting: font.setKerning(font_setting["kerning"])
        if "letter_spacing" in font_setting: eval(f"font.setLetterSpacing(QFont.{list(font_setting['letter_spacing'].keys())[0]}, {list(font_setting['letter_spacing'].values())[0]})")
        if "overline" in font_setting: font.setOverline(font_setting["overline"])
        if "pixel_size" in font_setting: font.setPixelSize(font_setting["pixel_size"])
        if "point_size" in font_setting: font.setPointSize(font_setting["point_size"])
        if "resolve_mask" in font_setting: font.setResolveMask(font_setting["resolve_mask"])
        if "stretch" in font_setting: font.setStretch(font_setting["stretch"])
        if "strike_out" in font_setting: font.setStrikeOut(font_setting["strike_out"])
        if "underline" in font_setting: font.setUnderline(font_setting["underline"])
        if "weight" in font_setting: font.setWeight(font_setting["weight"])
        if "word_spacing" in font_setting: font.setWordSpacing(font_setting["word_spacing"])
        return font


