import flet as ft
import math

def main(page: ft.Page):
    page.title = "Scientific Calculator"
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = "black"

    result = ft.TextField(
        value="0",
        text_align="right",
        width=350,
        text_size=40,
        color="white",
        bgcolor="#212121", 
        read_only=True,
    )

    def button_clicked(e):
        data = e.control.data
        current_value = result.value if result.value != "0" and result.value != "Error" else ""

        try:
            if data == "C":
                result.value = "0"
            elif data == "=":
                result.value = str(eval(current_value if current_value else "0"))
            elif data == "sin":
                result.value = str(math.sin(math.radians(float(current_value or 0))))
            elif data == "cos":
                result.value = str(math.cos(math.radians(float(current_value or 0))))
            elif data == "tan":
                result.value = str(math.tan(math.radians(float(current_value or 0))))
            elif data == "√":
                result.value = str(math.sqrt(float(current_value or 0)))
            elif data == "log":
                val = float(current_value or 0)
                if val > 0:
                    result.value = str(math.log10(val))
                else:
                    result.value = "Error"
            else:
                result.value = current_value + data
        except Exception:
            result.value = "Error"
        
        page.update()

    def create_button(text, color="#424242", text_color="white", data=None, width=70):
        if data is None: data = text
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(value=text, color=text_color, size=20),
                bgcolor=color,
                on_click=button_clicked,
                data=data,
                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=0),
            ),
            width=width, height=70,
        )

    def create_zero_button():
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(value="0", color="white", size=20),
                bgcolor="#424242",
                on_click=button_clicked,
                data="0",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=35), 
                    padding=20
                ),
            ),
            width=150, height=70,
        )

    row1 = [create_button("C", color="#616161"), create_button("√", color="#616161"), create_button("log", color="#616161"), create_button("/", color="orange")]
    row2 = [create_button("sin", color="#455A64"), create_button("cos", color="#455A64"), create_button("tan", color="#455A64"), create_button("*", color="orange")]
    row3 = [create_button("7"), create_button("8"), create_button("9"), create_button("-", color="orange")]
    row4 = [create_button("4"), create_button("5"), create_button("6"), create_button("+", color="orange")]
    row5 = [create_button("1"), create_button("2"), create_button("3"), create_button("+", color="orange")]
    row6 = [create_zero_button(), create_button("."), create_button("=", color="orange")]

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    result,
                    ft.Row(row1, spacing=10),
                    ft.Row(row2, spacing=10),
                    ft.Row(row3, spacing=10),
                    ft.Row(row4, spacing=10),
                    ft.Row(row5, spacing=10),
                    ft.Row(row6, spacing=10),
                ],
                spacing=10
            ),
            padding=30
        )
    )

ft.app(target=main)