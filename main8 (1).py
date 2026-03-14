from operaciones_caf import *

# 10 PERSONAS
p1 = Persona(0, "Pato", "pato@mail.com")
p0 = Persona(1, "Anna", "ana@mail.com")
p2 = Persona(2, "Luis", "luis@mail.com")
p3 = Persona(3, "Carlos", "carlos@mail.com")
p4 = Persona(4, "María", "maria@mail.com")
cli1 = Cliente(5, "Sofía", "sofia@mail.com")
cli2 = Cliente(6, "Jorge", "jorge@mail.com")
cli3 = Cliente(7, "Valeria", "valeria@mail.com")
emp1 = Empleado(8, "Pedro", "pedro@mail.com", 101, "barista")
emp2 = Empleado(9, "Lucía", "lucia@mail.com", 102, "gerente")

print("-------- PERSONAS ------------")
for persona in [p0,p1,p2,p3,p4,cli1,cli2,cli3,emp1,emp2]:
    print(persona.nombre, "con email:", persona.email)
    persona.login()

# 10 OBJETOS DE COMIDA
b1 = Bebida(201, "Latte", 50, "Grande", "CALIENTE")
b2 = Bebida(202, "Té Helado", 40, "Mediano", "FRIA")
b3 = Bebida(203, "Capuchino", 55, "Chico", "CALIENTE")
b4 = Bebida(204, "Jugo de Naranja", 35, "Grande", "FRIA")
b5 = Bebida(205, "Chocolate Caliente", 45, "Mediano", "CALIENTE")
pstr1 = Postre(301, "Brownie", 30, vegano=False, sin_gluten=True)
pstr2 = Postre(302, "Galleta", 20, vegano=True, sin_gluten=False)
pstr3 = Postre(303, "Pastel de Zanahoria", 40, vegano=False, sin_gluten=False)
pstr4 = Postre(304, "Cheesecake", 50, vegano=False, sin_gluten=False)
pstr5 = Postre(305, "Muffin", 25, vegano=True, sin_gluten=True)

print("------ COMIDA -----")
for comida in [b1,b2,b3,b4,b5,pstr1,pstr2,pstr3,pstr4,pstr5]:
    print(comida)

# funcion actualizar perfil
p2.actualizar_perfil("Luis Pérez", "luisp@mail.com")

print("------------------------")

# Crear pedidos de ejemplo
ped1 = Pedido(401, [b1, pstr1])
ped2 = Pedido(402, [b2, pstr2])
ped3 = Pedido(403, [b3, pstr3])

# Cliente realiza pedidos
cli1.realizar_pedido(ped1)
cli1.realizar_pedido(ped2)
cli1.realizar_pedido(ped3)
cli1.consultar_historial()
cli1.canjear_puntos()

print("------------")

cli2.realizar_pedido(ped1)
cli2.realizar_pedido(ped2)
cli2.realizar_pedido(ped3)
cli2.realizar_pedido(ped1)
cli2.realizar_pedido(ped2)
cli2.realizar_pedido(ped3)
cli2.consultar_historial()
cli2.canjear_puntos()

print("--------------")

# Bebida con extras
beb1 = Bebida(1, "Latte", 50, "Grande", "CALIENTE")
beb1.agregar_Extra("Leche de almendra", 10)
beb1.calcular_Precio_Final()

# Postre
postre = Postre(2, "Brownie", 35, False, True)

print("-------- EMPLEADO ---")
emp2.marcar_entrada()

print("------- INVENTARIO Y PEDIDOS ---")
inv = Inventario()
inv.agregar_Ingrediente("Latte", 5)
inv.agregar_Ingrediente("Brownie", 2)

inv.reducir_Stock("Latte", 1)
inv.reducir_Stock("Chocolate", 1)
pedido = Pedido(500, [beb1, postre])
pedido.calcular_Total()
pedido.validar_Stock(inv)
emp2.cambiar_estado_ped(pedido, "ENTREGADO")
print("---- GRACIAS POR USAR ESTE PROGRAMA, QUE TENGA LINDO DIA :) -----")