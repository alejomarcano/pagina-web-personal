import requests
def send_simple_message(asunto, html):
    return requests.post(
        "https://api.mailgun.net/v3/mg.vikua.com/messages",
        auth=("api", "key-362b924e925edb7fb84910005a739692"),
        data={"from": "URBOT CORREO <postmaster@mg.vikua.com>",
              "to": "alemvangrieken@gmail.com",
              "subject": asunto,
              "text": "Correo de python",
              "html": html})

if __name__ == '__main__':
    send_simple_message("Reporte de URBOT", '<h1 style="color: #5e9ca0;"><span style="color: #808000;">¡${nombres}, ha usado URBOT y ha realizado la siguiente acción!</span></h1> <h2 style="color: #2e6c80;">Recomendación de mejorar la Atención al Usuario:</h2> <p>El usuario de nombre <strong>${nombres}</strong> y correo <strong>${maill}</strong>, ha realizado una recomendación para mejorar la atención al usuario, en donde explica :</p> <blockquote><strong> <p>${funcionalidad}</p></strong> </blockquote> <p>&nbsp;</p> <p><strong>&nbsp;<img src="https://res.cloudinary.com/vikua/image/upload/v1581651986/samples/URBO/urbotsolo_w0naqo.png" alt="" width="157" height="250" /></strong></p> <p><strong>Atentamente</strong></p> <p><strong>&iexcl;URBOT!</strong></p>')



