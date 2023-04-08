from collections import namedtuple
import customtkinter as ui

# Font
font_black = "Arial Black"
font_regular = "Arial"
font_bold = "Arial Bold"

style = namedtuple("Style", "style, pack")

# Colors
bg_main_color = "#0F0F0F"
bg_second_color = "##A8A8A8"
button_color = "#FF9933"
hover_button_color = "#E68A2E"
entry_color = "#1b1b1b"

# Options Button
options_button_style = {
    "width": 28,
    "fg_color": button_color,
    "hover_color": hover_button_color,
    "text_color": bg_main_color,
}
options_button_pack = {
    "fill": ui.X,
    "side": ui.RIGHT,
    "padx": 2
}
options_button = style(style=options_button_style, pack=options_button_pack)
# Main Button
main_button_style = {
    "corner_radius": 0,
    "fg_color": button_color,
    "hover_color": hover_button_color,
    "text_color": bg_main_color,
    "font": (font_bold, 18)
}
main_button_pack = {
    "fill": ui.X,
    "side": ui.BOTTOM,
    "padx": 0
}
main_button = style(style=main_button_style, pack=main_button_pack)

# h1 Label
h1_label_style = {
    "font": (font_black, 18)
}
h1_label_pack = {
    "pady": 5
}
h1_label = style(style=h1_label_style, pack=h1_label_pack)

# h2 Label
h2_label_style = {
    "font": (font_regular, 14)
}
h2_label_pack = {
    'fill': ui.X,
    "side": ui.LEFT,
    "padx": 5
}
h2_label = style(style=h2_label_style, pack=h2_label_pack)

# Frame
frame_style = {
    "fg_color": bg_main_color,
}
frame_pack = {
    'fill': ui.X,
    "side": ui.LEFT
}
frame = style(style=frame_style, pack=frame_pack)

# Entry
entry_style = {
    "fg_color": entry_color,
    "width": 200,
    "border_width": 0,
    "corner_radius": 50
}
entry_pack = {
    'fill': ui.X,
    "side": ui.LEFT,
    "padx": 5
}
entry = style(style=entry_style, pack=entry_pack)