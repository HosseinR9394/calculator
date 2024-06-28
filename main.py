import flet as ft

def main(page: ft.page):
    page.title = "Hossein's Calcu"
    page.window_height = 350
    page.window_width = 350
    page.window_resizable = False
    page.window_maximizable = False


    def click(e):
        if e.control.data in ["1","2","3","4","5","6","7","8","9","0",".","(",")","+","*","-","/"]:
            txt.value = str(txt.value) + str(e.control.data)
            page.update()

        if e.control.data == "=":
            txt.value = eval(str(txt.value))
            page.update()
        if e.control.data == "c":
            txt.value = ""
            page.update()
        if e.control.data == "<":
            lst = list(txt.value)
            lst.pop()
            txt.value = "".join(map(str,lst))
            page.update()



    txt= ft.TextField(
        border_color="#068DA9",
        read_only=True,
        text_size=30,
    )
    page.add(txt)


    btn_e = ft.ElevatedButton(
        text="<",bgcolor="#080202",color="#EEEDED",on_click=click,data="<",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_P_baz = ft.ElevatedButton(
        text="(",bgcolor="#001B79",color="#EEEDED",on_click=click,data="(",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_P_baste = ft.ElevatedButton(
        text=")",bgcolor="#001B79",color="#EEEDED",on_click=click,data=")",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_taghsim = ft.ElevatedButton(
        text="÷",bgcolor="#001B79",color="#EEEDED",on_click=click,data="/",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )

    r1 = ft.Row(
        controls=[btn_e,btn_P_baz,btn_P_baste,btn_taghsim],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r1)


    btn_7 = ft.ElevatedButton(
        text="7",bgcolor="#F0DE36",color="#232323",on_click=click,data="7",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_8 = ft.ElevatedButton(
        text="8",bgcolor="#F0DE36",color="#232323",on_click=click,data="8",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_9 = ft.ElevatedButton(
        text="9",bgcolor="#F0DE36",color="#232323",on_click=click,data="9",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_zarb = ft.ElevatedButton(
        text="*",bgcolor="#001B79",color="#EEEDED",on_click=click,data="*",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )

    r2 = ft.Row(
        controls=[btn_7,btn_8,btn_9,btn_zarb],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r2)


    btn_4 = ft.ElevatedButton(
        text="4",bgcolor="#F0DE36",color="#232323",on_click=click,data="4",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_5 = ft.ElevatedButton(
        text="5",bgcolor="#F0DE36",color="#232323",on_click=click,data="5",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_6 = ft.ElevatedButton(
        text="6",bgcolor="#F0DE36",color="#232323",on_click=click,data="6",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_menha = ft.ElevatedButton(
        text="-",bgcolor="#001B79",color="#EEEDED",on_click=click,data="-",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )

    r3 = ft.Row(
        controls=[btn_4,btn_5,btn_6,btn_menha],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r3)


    btn_1 = ft.ElevatedButton(
        text="1",bgcolor="#F0DE36",color="#232323",on_click=click,data="1",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_2 = ft.ElevatedButton(
        text="2",bgcolor="#F0DE36",color="#232323",on_click=click,data="2",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_3 = ft.ElevatedButton(
        text="3",bgcolor="#F0DE36",color="#232323",on_click=click,data="3",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_jam = ft.ElevatedButton(
        text="+",bgcolor="#001B79",color="#EEEDED",on_click=click,data="+",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )

    r4 = ft.Row(
        controls=[btn_1,btn_2,btn_3,btn_jam],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r4)


    btn_C = ft.ElevatedButton(
        text="C",bgcolor="#D80032",color="#EEEDED",on_click=click,data="c",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_0 = ft.ElevatedButton(
        text="0",bgcolor="#F0DE36",color="#232323",on_click=click,data="0",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_dot = ft.ElevatedButton(
        text=".",bgcolor="#7E1717",color="#EEEDED",on_click=click,data=".",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )
    btn_eq = ft.ElevatedButton(
        text="=",bgcolor="#001B79",color="#EEEDED",on_click=click,data="=",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
        )

    r5 = ft.Row(
        controls=[btn_C,btn_0,btn_dot,btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r5)

ft.app(target=main)