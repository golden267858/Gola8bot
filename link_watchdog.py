import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LinkWatchdog")

CONFIG_PATH = "memory/link_config.json"

def check_link(link):
    try:
        response = requests.get(link, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error checking link {link}: {e}")
        return False

def switch_link():
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    
    # Simple logic: switch to the first backup
    if config["backup_links"]:
        old_link = config["active_link"]
        new_link = config["backup_links"].pop(0)
        config["active_link"] = new_link
        
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)
        
        return old_link, new_link
    return None, None

def notify_alert(old_link, new_link):
    # This is a placeholder for sending a Burmese alert
    msg = f"⚠️ သတိပေးချက် - 引流链接 {old_link} ပျက်စီးနေပါသည်။ အသစ်အဖြစ် {new_link} ကို ပြောင်းလဲလိုက်ပါပြီ။"
    print(f"Sending to alert group: {msg}")

if __name__ == "__main__":
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    
    if not check_link(config["active_link"]):
        logger.warning(f"Primary link {config['active_link']} is down!")
        old, new = switch_link()
        if new:
            notify_alert(old, new)
        else:
            logger.critical("No backup links available!")
    else:
        logger.info(f"Link {config['active_link']} is healthy.")
