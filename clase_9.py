import yagmail
from credenciales import mail, password


yag = yagmail.SMTP (user='cachi900@gmail.com', password='udnazbjquwksijxw')

destinatarios= ['cachi900@gmail.com',
                'alfredoibanez19@yahoo.com.ar',
                'cachi_1987@yahoo.com.ar']

asunto = f'nuevo correo de {mail}'
mensaje = '<h1> este mensaje es una prueba</h1> <br> este es un mensaje de prueba'
contenido = [mensaje]

yag.send(destinatarios,asunto,contenido)

