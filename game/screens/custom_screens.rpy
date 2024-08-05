screen GameUI:
    imagebutton: # Map
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_button_%s.png"
        action Show("MapUI")
    imagebutton: # Pass time
        xalign 1.0
        yalign 0.0
        xoffset -140
        yoffset 20
        auto "UI/hourglass_%s.png"
        action Function(advance_time)

screen MapUI():
    tag MapUI
    add "backgrounds/bg map.jpg"
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_arrow_%s.png"
        action Rollback()
    imagebutton:
        at map_button(820, 24)
        idle "map/the_citadel_hover.png"
        hover "map/the_citadel_hover.png"
        action [ Hide("MapUI"), Call("the_citadel_main")]
    imagebutton:
        at map_button(1420, 277)
        idle "map/balvor_tower_hover.png"
        hover "map/balvor_tower_hover.png"
        action [ Hide("MapUI"), Call("balvor_tower_main")]
    imagebutton:
        at map_button(580, 0)
        idle "map/dalors_fury_hover.png"
        hover "map/dalors_fury_hover.png"
        action [ Hide("MapUI"), Call("dalors_fury_main")]
    imagebutton:
        at map_button(987, 552)
        idle "map/fighters_guild_hover.png"
        hover "map/fighters_guild_hover.png"
        action [ Hide("MapUI"), Call("fighters_guild_main")]
    imagebutton:
        at map_button(0, 124)
        idle "map/lilywatch_hover.png"
        hover "map/lilywatch_hover.png"
        action [ Hide("MapUI"), Call("lilywatch_main")]
    imagebutton:
        at map_button(467, 85)
        idle "map/lovers_folly_hover.png"
        hover "map/lovers_folly_hover.png"
        action [ Hide("MapUI"), Call("lovers_folly_main")]
    imagebutton:
        at map_button(200, 480)
        idle "map/praelor_hover.png"
        hover "map/praelor_hover.png"
        action [ Hide("MapUI"), Call("praelor_main")]
    imagebutton:
        at map_button(605, 672)
        idle "map/temple_of_aeyenlo_hover.png"
        hover "map/temple_of_aeyenlo_hover.png"
        action [ Hide("MapUI"), Call("temple_of_aeyenlo_main")]
    imagebutton:
        at map_button(1327, 823)
        idle "map/ursiowatch_hover.png"
        hover "map/ursiowatch_hover.png"
        action [ Hide("MapUI"), Call("ursiowatch_main")]

transform map_button(x, y):
    pos(x, y)
    on idle:
        alpha 0.0
    on hover:
        alpha 1.0

screen DayDisplay():
    tag DayDisplay
    text "[day_of_week.value]" ypos 0.05 xpos 0.05
    text "Week [week_number] Day [day_number]" ypos 0.1 xpos 0.05
    text "[time_of_day.value]" ypos 0.15 xpos 0.05
