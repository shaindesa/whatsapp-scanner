import re
import pandas as pd

def WhatsAppParse(textpath, limit):
    counting = False
    if limit > 0:
        counting = True

    counter = 0
    whatsapp_data = []

    with open(textpath, encoding='UTF-8') as fhand:
        for line in fhand:
            if counter > limit and counting == True:
                return whatsapp_data
            
            line.strip()

            name = re.findall("-\s(\S*):", line)
            message = re.findall("[a-z]:(.*)", line)
            date = re.findall(".*-", line)
            
            if len(name) != 1 or len(message) != 1 or len(date) != 1:
                continue

            
            whatsapp_data.append({
                "date": date[0].strip(),
                "name": name[0],
                "message": message[0]
            }
            )

            counter += 1
    
    whatsapp_frame = pd.DataFrame(whatsapp_data)
    whatsapp_frame.dropna()
    
    whatsapp_frame_datetime = whatsapp_frame
    whatsapp_frame_datetime["date"] = pd.to_datetime(whatsapp_frame["date"], format="%d/%m/%Y, %H:%M -", errors='coerce')
    whatsapp_frame_datetime.set_index("date", inplace=True)

    return whatsapp_frame_datetime