import datetime

dia= datetime.date.today()

w= dia.weekday()+1

if (w==0):
  print("feliz domingo")

elif (w==2):
  print("wohoo es martes")

elif (w==3):
  print("yayy es miercoles")

elif (w==4):
  print("es jueves :/")

elif (w==5):
  print("es VIERNES!!!!")



else:
  print("yahoo es sabado")

