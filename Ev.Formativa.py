PkR = 0
OtR = 0
PvR = 0
AeR = 0
Descuento = 0
otro = ""
while True:
    if otro == "no":
        break
    print("****************")
    print("Opciones de pedidos:")
    print("1. Pikachu Roll, $4500")
    print("2. Otaku Roll, $5000")
    print("3. Pulpo Venenoso Roll, $5200")
    print("4. Anguila Eléctrica Roll, $4800")
    print("5. Terminar pedido")
    print("****************")
    op = int(input("Seleccione el producto a ingresar: "))
    if op == 1:
        cantidad1 = int(input("¿Cuantos desea agregar? "))
        PkR = PkR + cantidad1
    elif op == 2:
        cantidad2 = int(input("¿Cuantos desea agregar? "))
        OtR = OtR + cantidad2
    elif op == 3:
        cantidad3 = int(input("¿Cuantos desea agregar? "))
        PvR = PvR + cantidad3
    elif op == 4: 
        cantidad4 = int(input("¿Cuantos desea agregar? "))
        AeR = AeR + cantidad4
    elif op == 5:
            opD = input("¿Cuenta con un codigo de descuento? (si/no): ")
            if opD == "si":
                Rep = "z"
                while Rep == "z":
                    codigo = input("Ingrese el codigo de descuento: ")
                    if codigo == "soyotaku":
                        Descuento = .1
                        Rep = ""
                        print("************************************")
                        TotalProducto = PkR + OtR + PvR + AeR
                        print(f"Total de productos: {TotalProducto}")
                        print("************************************")
                        print(f"Pikachu Roll: {PkR}")
                        print(f"Otaku Roll: {OtR}")
                        print(f"Pulpo Venenoso Roll: {PvR}")
                        print(f"Anguila Eléctrica Roll: {AeR}")
                        print("************************************")
                        subtotal = (4500*PkR)+(5000*OtR)+(5200*PvR)+(4800*AeR)
                        CantidadDescuento = subtotal*Descuento
                        Total = subtotal - CantidadDescuento
                        print(f"Subtotal por pagar: ${subtotal}")
                        print(f"Descuento por codigo: ${CantidadDescuento}")
                        print(f"Total a pagar: ${Total}")
                        print("************************************")
                        otro = input("¿Desea realizar otro pedido?(si/no) ")
                        if otro == "si":
                            PkR = 0
                            OtR = 0
                            PvR = 0
                            AeR = 0
                        elif otro == "no":
                            break
                        else:
                            print("Opción no valida")
                    else:
                        print("Código no valido")
                        Rep = input("¿Desea reingresar el codigo(z) o volver al menú principal(x): ")
            elif opD == "no":
                    Descuento = 0
                    print("************************************")
                    TotalProducto = PkR + OtR + PvR + AeR
                    print(f"Total de productos: {TotalProducto}")
                    print("************************************")
                    print(f"Pikachu Roll: {PkR}")
                    print(f"Otaku Roll: {OtR}")
                    print(f"Pulpo Venenoso Roll: {PvR}")
                    print(f"Anguila Eléctrica Roll: {AeR}")
                    print("************************************")
                    subtotal = (4500*PkR)+(5000*OtR)+(5200*PvR)+(4800*AeR)
                    CantidadDescuento = subtotal*Descuento
                    Total = subtotal - CantidadDescuento
                    print(f"Subtotal por pagar: ${subtotal}")
                    print(f"Descuento por codigo: ${CantidadDescuento}")
                    print(f"Total a pagar: ${Total}")
                    print("************************************")
                    otro = input("¿Desea realizar otro pedido?(si/no) ")
                    if otro == "si":
                        PkR = 0
                        OtR = 0
                        PvR = 0
                        AeR = 0
                    elif otro == "no":
                         break
                    else:
                        print("Opción no valida")
    else:
        print("Opción no valida")