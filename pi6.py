import psutil
import time
import datetime
quantidade = 0

print("Número de CPUs: ",psutil.cpu_count()) 

while True:
  print("\nLeitura n° ", quantidade)
  date_time = datetime.datetime.now()
  print(date_time.strftime("%d/%b/%Y %H:%M\n"))

  discoG = psutil.disk_usage('G://')
  discoC = psutil.disk_usage('C://')
  swap = psutil.swap_memory() 
  ram = psutil.virtual_memory()

  print ("Memória total:" ,round(discoG.total / (1024.0 ** 3),2), "Gb (Disco G:)")
  print ("Memória usada:" ,round(discoG.used / (1024.0 ** 3),2), "Gb (Disco G:)")
  print ("Memória livre:" ,round(discoG.free / (1024.0 ** 3),2), "(Gb Disco G:)")
  print ("Percentual de memória usada:" ,discoG.percent,"% (Disco G:)\n")

  print ("Memória total:" ,round(discoC.total / (1024.0 ** 3),2), "Gb (Disco C:)")
  print ("Memória usada:" ,round(discoC.used / (1024.0 ** 3),2), "Gb (Disco C:)")
  print ("Memória livre:" ,round(discoC.free / (1024.0 ** 3),2), "Gb (Disco C:)")
  print ("Percentual de memória usada:" ,discoC.percent,"% (Disco C:)\n")

  print ("Memória swap total: " ,round(swap.percent,2),"%")

  print("Percentual de memória RAM em uso:",round(ram.percent,2),'%')

  print("Percentual de memória RAM livre:",round(ram.available * 100 / ram.total,2),'%')
  quantidade = quantidade + 1
  time.sleep(300)