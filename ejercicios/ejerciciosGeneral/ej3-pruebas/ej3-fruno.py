
def justificador(txt,width):
  # Dividir la cadena en una lista de longitud width.
  split = ["{}\n".format(txt[i:i+width].ljust(width,"-")) for i in range(0,len(txt),width)]

  # Unir la lista usando \n como union
  print(repr("".join(split)))



texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In venenatis malesuada elit,"
texto2 = "Lorem ipsum dolor sit"

#justificador(texto,30)
justificador(texto,30)