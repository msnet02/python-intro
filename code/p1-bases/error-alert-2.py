# Programa: error-alert-2.py
# Creación: 24/07/2025

def send_email(email_address, error_message):
    """Función que simula el envío de un mensaje por Email"""
    print(f"Notificación: {error_message} -> Destinatario: {email_address}")

# Main code
alert_system = 'email' # Possible values: 'console' or 'email' 
error_severity = 'medium' # Possible values: 'critical, 'medium' or 'low'
error_message = 'OMG! Something terrible happened'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    match error_severity:
        case 'critical':
            send_email('admin@example.com', error_message)
        case 'medium':
            send_email('support.1@example.com', error_message)
        case _:
            send_email('support.2@example.com', error_message)
