# -*- coding: utf-8 -*-



import android
import time
import urllib2
import sys

droid = android.Android()

def localizar():
    droid.makeToast(u"Empezando a localizar la posicion")	
    droid.startLocating(3600,1)

    time.sleep(10)
    
    fin = True
    segundos = 300
    seg_trancurridos = 0
    
    while fin:
        time.sleep(1)
        seg_trancurridos += 1
        l = droid.readLocation()
        ll = l.result
        
        if "gps" in ll:
            mensaje = u"Posición actual: "
            pos = (str(ll["gps"]["latitude"]), str(ll["gps"]["longitude"]))
            fin = False
            droid.makeToast(u"Posición GPS encontrada")
        else:

            if seg_trancurridos == segundos: 
                fin = False
                
                if "network" in ll:
                    pos = (str(ll["network"]["latitude"]), str(ll["network"]["longitude"]))
                    mensaje = u"Posición red celular: "
                    droid.makeToast(u"Posición Red Celular encontrada")
                else:
                    
                    ll = droid.getLastKnownLocation().result
                    pos = (str(ll["network"]["latitude"]), str(ll["network"]["longitude"]))
                    mensaje = u"Ultima posición red celular: "
                    droid.makeToast(u"No se pudo establecer conexión, se enviara la ultima posición registrada")
    
    droid.makeToast(u"Terminado de localizar la posicion")	

    pll = "%s,%s" % (str(pos[0]), str(pos[1]))

    mapa = "http://maps.google.com/maps?ll=%s&q=%s" % (pll, pll)

    droid.stopLocating()
    
    return mensaje, mapa    

def enviar_mensaje(numero):
    try: 
        mensaje, mapa = localizar()
        msg = "%s %s" % (mensaje,  mapa)
	asunto = u"Respuesta a la petición de localización GPS desde el numero %s" % (numero)
	para = "xxx@gmail.com"
        droid.sendEmail(para, asunto, msg)
	droid.makeToast(u"Enviada respuesta")
    except:
        droid.makeToast("Error: " + str(sys.exc_info()[0]))


def servicio():
    
    while True:
        time.sleep(10)
	# Escuchar los mensajes SMS
        msg_solicitud = droid.smsGetMessages(True)
        
        for i in msg_solicitud.result:
            
            msg_sms = i["body"].strip().upper()
            if msg_sms == "GPS":
                droid.makeToast(u"Solicitud de localización recibida")
                droid.smsMarkMessageRead([i["_id"]], True)
                telefono = i["address"]
                enviar_mensaje(telefono)
		droid.makeToast(u"%s: %s" % (telefono,msg_sms))
                
                
                
    
if __name__ == "__main__":
    servicio()
