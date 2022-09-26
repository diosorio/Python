#creamos la función add y le pasaremos el parámetro "a"
def add(a):
    """
    add 1 to a
    """
    b = a + 1 #al parámetro a le sumamos 1 y guardamos su valor en la variable b
    print(a, "if you add one, is:", b)
    return(b)

#invocamos la función, pasandole 23 al parámetro "a"
add(23) 
