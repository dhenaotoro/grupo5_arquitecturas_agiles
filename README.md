# grupo5_arquitecturas_agiles analisis de seguridad

A continuación compartimos la arquitectura que seguimos para validar las historias de usuario "registro de candidato" y "consultar evaluación". Esta arquitectura fue hecha en la nube AWS:

![image](https://github.com/dhenaotoro/grupo5_arquitecturas_agiles/assets/78186561/1373611b-7767-49a0-8436-9fe7b840a0ce)

# Datos de conexión a AWS:

Tener en cuenta que el trabajo fue realizado con servicios en la nube de Amazon, por tanto, gran parte de este trabajo se puede visualizar al ingresar a la consola web de Amazon con las siguientes credenciales.

 - Account ID: misogrupo1
 - IAM user name: misogrupo1
 - Contraseña: M1sogrupo12023!

   Nota: No olvidar selecciona la opción IAM user antes de ingresar el valor de Account ID.

En este expiremento se creó un endpoint expuesto por el servicio API-Gateway, dos lambdas, un SQS y un SNS. Por tanto, el único servicio que contiene código corresponde a las lambdas el cual se encuentran en este repositorio.
Tener presente que el código de la función Lambda del Login se encuentra en el directorio: `lambda_login_usuario`.

El API-Gateway que se configuró para este experimento posee la siguiente url: https://kxx3etkj2c.execute-api.us-east-1.amazonaws.com/Test y el siguiente ID: kxx3etkj2c en AWS.

Por tanto se podrá consumir este endpoint usando POSTMAN de acuerdo a como se muestra en la siguiente imagen:

![image](https://github.com/dhenaotoro/grupo5_arquitecturas_agiles/assets/78186561/95957497-673c-4991-8e93-0dd04adbbc75)

La lambda de login se denomina: `loginTest` con el fin de poder encontrarla en la consola de AWS

La base de datos se encuentra en el servicio RDS de la consola de AWS y se denomina: `database-test`

# grupo5_arquitecturas_agiles analisis de disponibilidad

A continuación compartimos la arquitectura que seguimos para validar la historia de usuario "Registrar empleado". Esta arquitectura fue hecha en la nube AWS:

![image](https://github.com/dhenaotoro/grupo5_arquitecturas_agiles/assets/78186561/90da59a1-f645-4906-8461-d456a1bdcf81)

 Nota: Tener presente que para ingresar al experimento de disponibilidad también se usan las mismas credenciales que se usan para el experimento de seguridad.
 


