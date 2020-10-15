import psutil
import time
import datetime
quantidade = 0

p = psutil.Process()
while True:
  # Imprime o nome do usuário que está lendo as informações
  print(p.username())
  print(p.cwd())
  # psutil.test()
  
  time.sleep(500)
