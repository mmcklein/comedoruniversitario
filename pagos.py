"""Pagos, tarifas y tickets con QR (RF6 y RF7)."""


def calcular_tarifa(precio_racion, es_becario):
    if es_becario:
        return round(precio_racion * 0.50, 2)
    return round(precio_racion, 2)


def registrar_pago(estudiante, monto, becario=False):
    return {
        "estudiante": estudiante,
        "monto": monto,
        "becario": becario,
        "estado": "registrado",
    }


def emitir_ticket(pago):
    contenido_qr = "COMEDOR|%s|%.2f" % (pago["estudiante"], pago["monto"])
    return {
        "pago": pago,
        "qr": contenido_qr,
    }
