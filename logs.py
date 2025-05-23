import logging
import time

# Configuration de l'enregistrement des logs
logging.basicConfig(
    filename='fichier_log.log',
    filemode='a',  # 'w' pour écraser à chaque fois
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

_last_log_time = {}
logger = logging.getLogger(__name__)  # nom = nom du fichier/module

def log_with_cooldown(level, message, cooldown=10):
    now = time.time()
    key = (level, message)
    if key not in _last_log_time or now - _last_log_time[key] > cooldown:
        logger.log(level, message)
        _last_log_time[key] = now



'''
# Exemples de logs
logging.info("Info classique")
logging.warning("Alerte")
logging.error("Erreur détectée")
logging.critical("Erreur critique !")
'''