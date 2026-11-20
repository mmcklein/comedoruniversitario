"""Reportes diarios del comedor (RF11)."""


def reporte_diario(fecha, raciones_servidas, ingresos, asistencia, merma):
    return {
        "fecha": fecha,
        "raciones_servidas": raciones_servidas,
        "ingresos": ingresos,
        "asistencia": asistencia,
        "merma": merma,
    }
