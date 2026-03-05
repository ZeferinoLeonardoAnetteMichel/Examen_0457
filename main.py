import flet as ft
def main(page: ft.Page):
    page.title = "Registro de participantes"
    txt_nombre = ft.TextField(
        label="Nombre completo",
        width=400
    )
    txt_correo = ft.TextField(
        label="Correo electrónico",
        width=400,
    )
    dropdown_tipo = ft.Dropdown(
        label="Taller de interes",
        width=300,
        options=[
            ft.dropdown.Option("Python para principiantes"),
            ft.dropdown.Option("Flet intermedio"),
            ft.dropdown.Option("Analisis de datos con pandas"),
        ]
    )
    radio_modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ])
    )
    check_inscripcion = ft.Checkbox(
        label="¿Requiere computadora portatil?"
    )
    slider_duracion = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        label="{value} experiencia programando",
        value=1
    )
    txt_resumen = ft.Text(
        value="Resumen:",
        size=16
    )
    def mostrar_ficha(e):
        nombre = txt_nombre.value
        correo= txt_correo.value 
        tipo = dropdown_tipo.value
        modalidad = radio_modalidad.value
        inscripcion = "Sí" if check_inscripcion.value else "No"
        duracion = slider_duracion.value
        resumen = f"""
        Nombre: {nombre}
        Correo: {correo}
        Tipo: {tipo}
        Modalidad: {modalidad}
        Requiere inscripción previa: {inscripcion}
        Tiempo estimado: {duracion} experiencia en programacion
        """
        txt_resumen.value = resumen
        page.update()
    btn_resumen = ft.ElevatedButton(
        content=ft.Text(
        "Mostrar ficha del participante",
        size=16,             
        color=ft.Colors.WHITE 
    ),
    bgcolor=ft.Colors.BLUE_900, 
    on_click=mostrar_ficha
)
    page.add(
        ft.Text("Registro de Participantes", size=30, weight="bold"),
        ft.Text("Nombre del participante:"),
        txt_nombre,
        ft.Text("Correo electronico:"),
        txt_correo,
        ft.Text("Taller de interes:"),
        dropdown_tipo,
        ft.Text("Modalidad de pago:"),
        radio_modalidad,
        ft.Text("Requerimientos:"),
        check_inscripcion,
        ft.Text("Tiempo estimado (experiencia en programacion):"),
        slider_duracion,
        btn_resumen,
        ft.Divider(),
        txt_resumen   
    )


ft.app(target=main)
