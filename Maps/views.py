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

       # print("Directions from " + (orig) + " to " + (dest))
       # print("Trip Duration: " + (json_data["route"]["formattedTime"]))
       # print("Miles: " + str(json_data["route"]["distance"]))
       # print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        #Time
        Trip_Duration=json_data["route"]["formattedTime"] 
        #Distance in KM
        KM=str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        #Fuel in Liters
        Fuel=str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        
        data={
            "InputOrig":InputOrig,
            "InputDest":InputDest,
            "KM":KM,
            "Trip_Duration":Trip_Duration,
            "Fuel": Fuel
        }
        return render(request, 'Maps/home.html',data)


def about(request):
    return render(request, 'Maps/about.html', {'title': 'About'})