# Characters used in the story
define mc = Character("[mc_name]", color="#ff0000", callback = name_callback, cb_name = None)
define unknown = Character("???")
define kuviis = Character("Kuviis", color="#DEC8C4", callback = name_callback, cb_name = "kuviis")
define professor = Character("Professor")
define gudrak = Character("Gudrak", color="#844A48", callback = name_callback, cb_name = "gudrak")
define bluejay = Character("Bluejay", color="#C1AA9D", callback = name_callback, cb_name = "bluejay")
define ralph = Character("Ralph", color="#885431", callback = name_callback, cb_name = "ralph")

image kuviis = At('images/characters/kuviis.png', sprite_highlight('kuviis'))
image kuviis annoyed = At('images/characters/kuviis_annoyed.png', sprite_highlight('kuviis'))
image kuviis blush = At('images/characters/kuviis_blush.png', sprite_highlight('kuviis'))

image gudrak = At('images/characters/gudrak.png', sprite_highlight('gudrak'))
image gudrak embarrassed = At('images/characters/gudrak_embarrassed.png', sprite_highlight('gudrak'))

image bluejay = At('images/characters/bluejay.png', sprite_highlight('bluejay'))

image ralph = At('images/characters/ralph.png', sprite_highlight('ralph'))