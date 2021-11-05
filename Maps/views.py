from django.shortcuts import render
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "yPfDRcQKBMOkOjMAG3WtXIzcCmmI0t5j"



def home(request):
    InputOrig=request.POST.get('inputlocation')
    InputDest=request.POST.get('inputDestination')
    

    url = main_api + urllib.parse.urlencode({"key": key, "from":InputOrig, "to":InputDest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        directions=[]
        Trip_Duration=json_data["route"]["formattedTime"] 
        #Distance in KM
        KM=str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        #Fuel in Liters
        Fuel=str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        Manuever=json_data["route"]["legs"][0]["maneuvers"]
        if (InputDest and InputOrig is not None):
            for each in Manuever:
                directions.append(each["narrative"]+ " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        
        
        data={
            "InputOrig":InputOrig,
            "InputDest":InputDest,
            "KM":KM,
            "Trip_Duration":Trip_Duration,
            "Fuel": Fuel,
            "directions":directions
        }
    
        return render(request, 'Maps/home.html',data)


def about(request):
    return render(request, 'Maps/about.html', {'title': 'About'})