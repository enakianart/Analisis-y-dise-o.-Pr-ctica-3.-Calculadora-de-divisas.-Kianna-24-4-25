def exchange_money():

    try:
        budget_entrada = input("Ingrese el monto de dinero que desea cambiar: ")
        budget = float(budget_entrada)

        exchange_rate_entrada = input("Ingrese la tasa de cambio actual: ")
        exchange_rate = float(exchange_rate_entrada)

        Monto_Moneda_Extranjera = budget / exchange_rate

        print (f"\nCon un presupuesto de {budget:,.2f} y una tasa de cambio de {exchange_rate},")
        print(f"el equivalente en la moneda extranjera es: {Monto_Moneda_Extranjera:,.2f}")

    except ValueError:
        print("Error: Porfis, ingrese valores numericos que sean validos para el presupuesto y la tasa de cambio.")

    except ZeroDivisionError:
        print("Error: La tasa de cambio no puede ser cero.")
    
exchange_money()
print ("Espero que haya sido de ayuda! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
