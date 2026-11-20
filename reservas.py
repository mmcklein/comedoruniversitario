"""Reservas de raciones y control de aforo (RF4 y RF5)."""


def reservar_racion(turno, horario, reservas_turno, aforo_maximo):
    cantidad_actual = reservas_turno.get(turno, 0)
    if cantidad_actual >= aforo_maximo:
        return False, "Aforo completo"
    reservas_turno[turno] = cantidad_actual + 1
    return True, "Reserva confirmada para el turno %s a las %s" % (turno, horario)


def consultar_aforo(turno, reservas_turno, aforo_maximo):
    ocupados = reservas_turno.get(turno, 0)
    return {
        "turno": turno,
        "ocupados": ocupados,
        "disponibles": max(aforo_maximo - ocupados, 0),
    }
