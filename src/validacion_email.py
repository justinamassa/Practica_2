def validar_email(email):
    """Valida una dirección de email según criterios básicos."""
    
    # No empieza ni termina con @ ni con .
    if email.startswith('@') or email.startswith('.'):
        return False
    if email.endswith('@') or email.endswith('.'):
        return False
    
    # Contiene exactamente un @
    if email.count('@') != 1:
        return False
    
    # Separamos en parte local y dominio
    partes = email.split('@')
    local = partes[0]
    dominio = partes[1]
    
    # Al menos un carácter antes del @
    if len(local) == 0:
        return False
    
    # Al menos un punto después del @
    if '.' not in dominio:
        return False
    
    # El dominio después del último punto tiene al menos 2 caracteres
    extension = dominio.split('.')[-1]
    if len(extension) < 2:
        return False
    
    return True
