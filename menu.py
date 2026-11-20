"""Publicacion del menu diario y semanal del comedor (RF3)."""


def publicar_menu_diario(fecha, platos):
    return {
        "fecha": fecha,
        "tipo": "diario",
        "platos": platos,
    }


def publicar_menu_semanal(fecha_inicio, menus):
    return {
        "fecha_inicio": fecha_inicio,
        "tipo": "semanal",
        "menus": menus,
    }
