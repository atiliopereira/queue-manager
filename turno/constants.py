class EstadoTicket:
    PENDIENTE = 'PENDIENTE'
    LLAMADO = 'LLAMADO'
    ATENDIDO = 'ATENDIDO'
    CERRADO = 'CERRADO'
    CANCELADO = 'CANCELADO'

    LISTA_ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (LLAMADO, 'Llamado'),
        (ATENDIDO, 'Atendido'),
        (CERRADO, 'Cerrado'),
        (CANCELADO, 'Cancelado')
    )


class EstadoBox:
    LIBRE = 'LIBRE'
    OCUPADO = 'OCUPADO'
    INHABILITADO = 'INHABILITADO'
    ASIGNADO = 'ASIGNADO'

    LISTA_ESTADOS = (
        (LIBRE, 'Libre'),
        (OCUPADO, 'Ocupado'),
        (INHABILITADO, 'Inhabilitado'),
        (ASIGNADO, 'Asignado')

    )
