

from UI_Control import UIControl


class TextBox(UIControl):
    def button_click(self):
        print("button clicked")


if __name__ == "__main__":
    text_box = TextBox()
    text_box.enable()
