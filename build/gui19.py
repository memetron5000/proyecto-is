



from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import gui18, gui20

# limpia el frame para poder actualizar la ventana
def titulo(frame5):
    # Limpia el frame
    for item in frame5.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa     
def cliente_ver_estado(frame5):
    global button_image_1, button_image_2, button_image_3, button_image_4,entry_image_1,image_image_1
    
    # Limpia el frame
    titulo(frame5)
    
    #verifica directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame19"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    #lectura de frame
    canvas = Canvas(
        frame5,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    #imagen
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        93.0,
        300.0,
        image=image_image_1
    )

    #texto
    canvas.create_text(
        400.0,
        24.0,
        anchor="nw",
        text="BIENVENIDO",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )

    #texto
    canvas.create_text(
        243.0,
        132.0,
        anchor="nw",
        text="Ver estado pedido:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        249.0,
        177.0,
        anchor="nw",
        text="Ingrese identificador del pedido:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        649.0,
        190.5,
        image=entry_image_1
    )#Cuadro donde se ingresa el ID de pedido a ver
    entry_1 = Entry(
        frame5,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=582.0,
        y=173.0,
        width=134.0,
        height=33.0
    )

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame5,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Buscar"),
        relief="flat"
    )#Boton para buscar la info del envio del ID especificado en el cuadro anterior
    button_1.place(
        x=735.0,
        y=168.0,
        width=50.0,
        height=45.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame5,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui18.cliente_ver_pedido(frame5),
        relief="flat"
    )#Boton funcionalidad
    button_2.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame5,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Ya estas aca"),
        relief="flat"
    )#Boton funcionalidad que se esta usando
    button_3.place(
        x=14.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame5,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui20.cliente_ver_historial(frame5),
        relief="flat"
    )#Boton funcionalidad
    button_4.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    