# -*- coding: utf-8 -*-

import android
import time
import sys

droid = android.Android()

def servicio():
    
    while True:
        time.sleep(10)
	# Escuchar los mensajes SMS
        msg_solicitud = droid.smsGetMessages(True)
        
        for i in msg_solicitud.result:
		msg_sms = i["body"].strip().upper()
                telefono = i["address"]
		droid.makeToast(u"%s: %s" % (telefono,msg_sms))

                
if __name__ == "__main__":
    servicio()
