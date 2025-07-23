"""from twilio.rest import Client

account_sid = 'ACbb00a4601d77a1db52bb86a2dbcf5da8'
auth_token = '2293e9036a0a90724b5824335055bc01'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MG5888f47d5b9dbb014c3b5b41bfea365f',
  body='⚠️ ALERTE ⚠️ : ❌ Coupure de courant ⚡️',
  to='+33635796139'
)
print(message.sid)"""

import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables du fichier .env

EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECEIVERS = os.environ.get("EMAIL_RECEIVERS", "").split(",")

# Configuration email
SMTP_SERVER = "smtp.univ-paris13.fr"
SMTP_PORT = 587
#EMAIL_SENDER = "hugo.lebaud@edu.univ-paris13.fr"
#EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
#EMAIL_RECEIVERS = ["hugo.l@mac.com","greg77290@yahoo.fr"]

# Adresse à ping (Google DNS ou ton propre serveur)
PING_HOST = "8.8.8.8"

def send_email_with_attachment(subject, body, log_file_path=None):
    if EMAIL_SENDER is None or EMAIL_PASSWORD is None:
      raise ValueError("EMAIL_SENDER ou EMAIL_PASSWORD non défini dans .env")
    print("Fonction envoie email avec pièce jointe :")
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECEIVERS)

    # Texte principal
    msg.attach(MIMEText(body, "plain"))

    # Ajout de pièce jointe si demandée
    print("Ajout de la pièce jointe si demandée…")
    if log_file_path:
        try:
            with open(log_file_path, "rb") as f:
                part = MIMEApplication(f.read(), Name="log.txt")
            part["Content-Disposition"] = 'attachment; filename="log.txt"'
            msg.attach(part)
        except Exception as e:
            msg.attach(MIMEText(f"[Erreur lecture log : {e}]", "plain"))
    print("Envoi de l'email…")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            if EMAIL_PASSWORD is None:
              raise ValueError("Mot de passe non défini dans les variables d'environnement.")
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
        print("Email avec pièce jointe envoyé.")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

def wait_for_network(timeout=300, interval=5):
    """
    Attend que le réseau soit opérationnel en pingant une adresse.
    Timeout total en secondes, intervalle entre deux pings.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            subprocess.check_output(["ping", "-c", "1", "-W", "1", PING_HOST])
            print("Réseau détecté.")
            return True
        except subprocess.CalledProcessError:
            print("Réseau encore indisponible...")
            time.sleep(interval)
    print("Timeout atteint : réseau toujours indisponible.")
    return False


"""def power_monitor_loop():
    power_was_lost = True

    while True:
        time.sleep(5)
        if power_was_lost:
            print("⚡ Courant revenu, vérification réseau...")
            if wait_for_network():
                send_email_with_attachment(
                    "Alerte : Coupure de courant détectée",
                    "Une coupure de courant a été détectée. L'alimentation et le réseau sont maintenant rétablis.",
                    "fichier_log.log"
                )
            else:
                print("❌ Réseau non revenu, email non envoyé.")
            power_was_lost = False

# Lancer la surveillance
if __name__ == "__main__":
    power_monitor_loop()"""


