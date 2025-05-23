import logging
import time

# Configuration de l'enregistrement des logs
logging.basicConfig(
    filename='fichier_log.log',
    filemode='a',  # 'w' pour écraser à chaque fois
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

'''
# Exemples de logs
logging.info("Info classique")
logging.warning("Alerte")
logging.error("Erreur détectée")
logging.critical("Erreur critique !")
'''

'''logger = logging.getLogger("cooldown_logger")

# Variable globale de dernier log
last_warning_time = 0
cooldown = 10  # en secondes

def log_warning_with_cooldown(message):
    global last_warning_time
    now = time.time()
    if now - last_warning_time >= cooldown:
        logger.warning(message)
        last_warning_time = now'''