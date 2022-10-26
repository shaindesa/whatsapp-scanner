#local imports
import parser
import graphers
import config

print("Running WhatsApp scanner. This may take a few moments...")

settings = config.GetConfig()

whatsapp_frame = parser.WhatsAppParse(settings["textpath"], settings["limit"])
gcname = settings["gcname"]

if settings["run_date_frequency"]:
    graphers.date_frequency(whatsapp_frame, gcname)

if settings["run_message_distribution"]:
    graphers.message_distribution(whatsapp_frame, gcname)

if settings["run_word_search"]:
    graphers.word_search(whatsapp_frame, settings["wordsearch"], gcname)

if settings["run_time_distribution"]:
    graphers.time_distribution(whatsapp_frame, gcname)

if settings["run_media_search"]:
    graphers.media_search(whatsapp_frame, gcname)

print("WhatsApp scan complete. See completed graphs in './out'. Display completed graphs on one page by opening './html/index.html'.")