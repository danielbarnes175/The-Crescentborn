# Narrator
define narrator = Character(None, callback = name_callback, cb_name = None)
define nvl_narrator = nvl_narrator

# Characters used in the story
define mc = Character("[mc_name]", color="#ff0000", callback = name_callback, cb_name = None)
define kuviis = Character("Kuviis", color="#DEC8C4", callback = name_callback, cb_name = "kuviis")
define professor = Character("Professor")
define gudrak = Character("Gudrak", color="#844A48", callback = name_callback, cb_name = "gudrak")
define bluejay = Character("Bluejay", color="#C1AA9D", callback = name_callback, cb_name = "bluejay")
define ralph = Character("Ralph", color="#885431", callback = name_callback, cb_name = "ralph")

define unknown_hreinar = Character("???", color="#ff0000")
define unknown = Character("???", color="#7c4e4e")
define unknown2 = Character("???", color="#7c6666")
define unknown3 = Character("???", color="#614444")
define unknown_generic = Character("???", color="#ffffff")

define hreinar = Character("Hreinar", color="ff0000")

define daskalos = Character("Daskalos", color="#7c4e4e")
define sotec = Character("Sotec", color="#7c6666")
define jeivor = Character("Jeivor", color="#614444")

image kuviis = At('images/characters/kuviis.png', sprite_highlight('kuviis'))
image kuviis annoyed = At('images/characters/kuviis_annoyed.png', sprite_highlight('kuviis'))
image kuviis blush = At('images/characters/kuviis_blush.png', sprite_highlight('kuviis'))

image gudrak = At('images/characters/gudrak.png', sprite_highlight('gudrak'))
image gudrak embarrassed = At('images/characters/gudrak_embarrassed.png', sprite_highlight('gudrak'))

image bluejay = At('images/characters/bluejay.png', sprite_highlight('bluejay'))

image ralph = At('images/characters/ralph.png', sprite_highlight('ralph'))