import requests
import telebot
import json


#start config
#end config

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! This is CVE Crawler Bot. Type a certain CVE identifier.")
    bot.send_message(message.chat.id, "Example: CVE-1999-1032")



@bot.message_handler(regexp="CVE-")


def defined_cve(message):
    user_message = message.text
    print("Starting bot")
    respond = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=' + user_message)

    if (0 == json.loads(respond.text).get("totalResults")):
        bot.send_message(message.chat.id, "CVE not Found") 
        return 

    cve_info = json.loads(respond.text).get("vulnerabilities")[0].get("cve")
    cvss_info = json.loads(respond.text).get("vulnerabilities")[0].get("cve").get("metrics").get("cvssMetricV2")[0]
    
    if(respond):

        bot.send_message(message.chat.id, "CVE id: " + cve_info.get("id") + "\nSource :" + cve_info.get("sourceIdentifier") + "\nPublished: " + cve_info.get("published") + 
                         "\nStatus :" + cve_info.get("vulnStatus") + "\nDesription: " + cve_info.get("descriptions")[0].get("value") + "\nSVSS Data: \nAccess Vector: " + cvss_info.get("cvssData").get("accessVector") +
                         "\nComplexity: " + cvss_info.get("cvssData").get("accessComplexity") + "\nAuthentication: " + cvss_info.get("cvssData").get("authentication") + 
                         "\nConfidential Impact: " + cvss_info.get("cvssData").get("confidentialityImpact") + "\nScore: " + str(cvss_info.get("cvssData").get("baseScore")) +
                         "\nSaverity: " + str(cvss_info.get("baseSeverity")) + "\nExploitability Score: " + str(cvss_info.get("exploitabilityScore")) + "\nImpact Score: " + str(cvss_info.get("impactScore")))




bot.infinity_polling()
