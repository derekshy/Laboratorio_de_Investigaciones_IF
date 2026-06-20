import math

h = 0.00001
k = 0.3
n = 2

angulo_previo_theta1 = math.pi / 2
angulo_previo_theta2 = 3 * math.pi / 2

w1 = 1
w2 = 2

print("h = 0.01 \nk = 4 \nn = 2 individuos \nLOS ANGULOS ESTAN EN RADIANES")

while True: #puede cambiarse este bucle, por un for (para ejecutar una cantidad finita de veces)
    resultado_t1 = angulo_previo_theta1 + (w1*h) - (h * (k/2) * math.sin(angulo_previo_theta1-angulo_previo_theta2))
    resultado_t2 = angulo_previo_theta2 + (w2*h) - (h * (k/2) * math.sin(angulo_previo_theta2-angulo_previo_theta1))

    angulo_previo_theta1 = resultado_t1
    angulo_previo_theta2 = resultado_t2

    r = math.sqrt((math.sin(resultado_t1)+ math.sin(resultado_t2)/2)**2 + (math.cos(resultado_t1)+ math.cos(resultado_t2)/2)**2) /n
    print("parametro r =", r, "Angulo Theta_1 = ",angulo_previo_theta1, "angulo_theta2 =",angulo_previo_theta2)
