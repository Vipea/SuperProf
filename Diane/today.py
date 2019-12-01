import datetime

def tekst_vandaag():
    vandaag = datetime.date.today()
    vandaag = vandaag.strftime("%d %B %Y")
    print(f"Vandaag is het {vandaag}")

tekst_vandaag()
