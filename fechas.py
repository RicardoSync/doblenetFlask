from datetime import datetime, timedelta


fecha = datetime.now()
fechaInstalacion = fecha.strftime("%Y-%m-%d")

prx = fecha + timedelta(days=31)
proximoPago = prx.strftime("%Y-%m-%d")


print(f"Fecha de instalacion {fechaInstalacion} su proximo pago es: {proximoPago}")