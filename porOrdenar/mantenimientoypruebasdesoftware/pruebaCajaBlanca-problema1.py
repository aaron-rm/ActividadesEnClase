def procesar_pedido (monto, cliente_vip, stock, metodo_envio):
    if stock <= 0:
        return "Producto sin stock"
    else:
        if monto > 200:
            if cliente_vip:
                descuento = monto * 0.25
            else:
                descuento = monto * 0.10
        else:
            descuento = 0
        total = monto - descuento
        if metodo_envio == "express":
            if total > 150:
                envio = 0
            else:
                envio = 10
        else:  # envio normal
            envio = 5
        total_final = total + envio
        if total_final > 500:
            return "Requiere autorización especial"
        else:
            return f"Total a pagar: {total_final}"

while True:
    monto = float(input("Ingrese el monto del pedido: "))
    cliente_vip = bool(input("¿Es cliente VIP? (True/False): ").lower() == "true")
    stock = int(input("Ingrese la cantidad de stock disponible: "))
    metodo_envio = input("Ingrese el método de envío (normal/express): ")
    print(procesar_pedido(monto, cliente_vip, stock, metodo_envio))

