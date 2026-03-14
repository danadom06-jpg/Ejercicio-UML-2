
class Persona:
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(f"Hola {self.nombre} has iniciado sesión con exito")

    def actualizar_perfil(self, nuevo_nombre, nuevo_email):
        self.nombre = nuevo_nombre
        self.email = nuevo_email
        print(f"Tu perfil se ha actualizado correctamente {self.nombre} con email {self.email}")
class Cliente(Persona):

    def __init__(self, id_persona, nombre, email):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad=0
        self.historial_pedidos=[]

    def realizar_pedido(self,ped):
        self.historial_pedidos.append(ped)
        self.puntos_fidelidad+=10
        self.ped=ped
        print(f"Hola {self.nombre} tu pedido {self.ped} se realizo correctamente")

    def consultar_historial(self):
        print("Tu historial de pedidos:")
        for ped in self.historial_pedidos:
            print(ped)

    def canjear_puntos(self):
        if self.puntos_fidelidad>=100:
            self.puntos_fidelidad-=100
            print("Canjeaste 100 puntos por un dulce")
        else:
            print("No tienes suficientes puntos, pide mas pedidos para reunir suficienntes puntos")

class Empleado(Persona):
    r_validos=["barista", "mesero", "gerente"]
    def __init__(self, id_persona, nombre, email, id_empleado, rol):
        super().__init__(id_persona, nombre, email)
        self.id_empleado = id_empleado
        self.rol = rol
        rol = rol.lower()
        if rol not in Empleado.r_validos:
            print("Rol no válido, (recuerda que solo hay: BARISTA, GERENTE, MESERO)")
    def marcar_entrada(self):
        print(self.nombre, "marcó entrada")

    lista_inventario=[]
    def actualizar_inventario(self, inventario):
        if self.rol=="gerente":
            self.lista_inventario.append(inventario)
            print(f"El invnetario se ha actualizado")
        else:
            print("No tienes permisos")

    def cambiar_estado_ped(self,ped,nuevo_estado ):
        if self.rol in ["barista", "gerente"]:
            ped.estado=nuevo_estado
            print("Estado ENTREGADO.")
        else:
            print("Estado NO ENCONTRADO")


#MODULO DE PRODUCTOS
class Producto_base:
    def __init__(self, id_producto, nombre, precio_base):
        self.nombre = nombre
        self.id_producto = id_producto
        self.precio_base = precio_base
    def calcular_Precio_Final(self):
        return self.precio_base
    def __str__(self):
        return f"El producto {self.nombre} cuesta (${self.precio_base})"
t_validas = ["FRIA", "CALIENTE"]

class Bebida(Producto_base):
    
    def __init__(self, id_producto, nombre, precio_base, tamaño, temperatura):
        super().__init__(id_producto, nombre, precio_base)
        self.tamaño = tamaño
        if temperatura not in t_validas:
            print("Temperatura no válida (recuerda: FRIA o CALIENTE)")
        self.temperatura=temperatura
        self.modificadores=[]
 
    def agregar_Extra(self, extra_m, costo_extra=0):
        self.modificadores.append((extra_m, costo_extra))



    def calcular_Precio_Final(self):
        total = self.precio_base
        for extra_m, costo in self.modificadores:
            total += costo
        print(f"El total de tu bebida {self.nombre} es de {total}")
        return total

class Postre(Producto_base):
    def __init__(self, id_producto, nombre, precio_base, vegano, sin_gluten):
        super().__init__(id_producto, nombre, precio_base)
        self.vegano = vegano
        self.sin_gluten = sin_gluten

estados_validos=["PENDIENTE", "PREPARANDO", "ENTREGADO"]
class Pedido:
    def __init__(self, id_pedido, productos):
        self.id_pedido=id_pedido
        self.productos=productos
        self.total=0
        self.estado="PENDIENTE"

    def __str__(self):
        lista = ", ".join([p.nombre for p in self.productos])
        return f"Pedido #{self.id_pedido} ({lista}) - Estado: {self.estado}"


    def calcular_Total(self):
        total=0
        for prod in self.productos:
            total+=prod.calcular_Precio_Final()

        self.total = total
        print("Total del pedido:", total)

    def validar_Stock(self, inventario):
        disponible = True
        for prod in self.productos:
            if prod.nombre not in inventario.ingredientes:
                inventario.notificar_Faltante(prod.nombre)
                disponible = False
        if disponible:
            print("Stock disponible ")
        else:
            print("Pedido no se puede preparar")

class Inventario:
    def __init__(self):
        self.ingredientes = {}
    def agregar_Ingrediente(self, nombre, cantidad):
        self.ingredientes[nombre]=cantidad
        print("Ingrediente agregado:", nombre)
    def reducir_Stock(self, nombre, cantidad):
        if nombre not in self.ingredientes:
            self.notificar_Faltante(nombre)
            return
        if self.ingredientes[nombre]<cantidad:
            self.notificar_Faltante(nombre)
        else:
            self.ingredientes[nombre] -= cantidad
            print("Stock restante de", nombre, ":", self.ingredientes[nombre])

    def notificar_Faltante(self, nombre):
        print("Falta inventario de:", nombre)