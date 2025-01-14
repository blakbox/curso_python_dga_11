import android
from time import sleep

#Se crea la instancia de la clase Android
droid = android.Android()
#Se inicia la localizacion
droid.startLocating()
#Se espera 15 segunfos
sleep(15)
#Se presenta en la consola la información de la localización
#Se maneja la información de un diccionario.
print "Altitud: ",droid.readLocation().result["network"]["altitude"]
print "Proveedor: ",droid.readLocation().result["network"]["provider"]
print "Latitud: ",droid.readLocation().result["network"]["latitude"]
print "Longitud: ",droid.readLocation().result["network"]["longitude"]
print "Tiempo: ",droid.readLocation().result["network"]["time"]
print "Velocidad: ",droid.readLocation().result["network"]["speed"]
print "Precisión: ",droid.readLocation().result["network"]["accuracy"]
#Se detiene la localización
droid.stopLocating()



