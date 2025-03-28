import json
from urllib import request

import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from MyApp.models import *

def login(request):
    return render(request,'Login.html')


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    try:
        ob = login_table.objects.get(username=username, password=password)
        request.session["lid"]=ob.id
        if ob.type == 'admin':
            return HttpResponse('''<script>alert("admin_login");window.location='/admin_admin_home'</script>''')
        elif ob.type=='hospital':
            return HttpResponse('''<script>alert("Hospital_login");window.location='/hospital_hospital_home'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");window.location='/'</script>''')

    except:
        return HttpResponse('''<script>alert("invalid");window.location='/'</script>''')


def admin_add_ambulance(request):
    return render(request,"admin/Add Ambulance.html")

def hospital_add_ambulance_post(request):
    VehicleNumber=request.POST['textfield']
    type=request.POST['select']
    status=request.POST['select2']
    username = request.POST['textfield10']
    password = request.POST['textfield11']

    if login_table.objects.filter(username=username).exists():
        return HttpResponse(
            '''<script>alert("Username Already Exists");window.location='/hospital_add_ambulance_hospital#a'</script>''')
    ob = login_table()
    ob.username = username
    ob.password = password
    ob.type = 'ambulance'
    ob.save()

    OB=ambulance_table()
    OB.VehicleNumber=VehicleNumber
    OB.Type=type
    OB.Status=status
    OB.LOGIN=ob
    OB.Hospital=hospital_table.objects.get(LOGIN=request.session["lid"])
    OB.save()
    return HttpResponse('''<script>alert("Ambulance Added Succefully");window.location='/hospital_view_ambulance#a'</script>''')


def admin_add_hospital(request):
    return render(request,"admin/Add Hospital.html")

def admin_add_hospital_post(request):
    name=request.POST['textfield']
    image=request.FILES['file']
    place=request.POST['textfield6']
    pin = request.POST['textfield2']
    post=request.POST['textfield3']
    email=request.POST['textfield4']
    contactNumberOne=request.POST['textfield5']
    contactNumberTwo=request.POST['textfield7']
    Latitude=request.POST['textfield8']
    Longitude=request.POST['textfield9']
    username=request.POST['textfield10']
    password=request.POST['textfield11']

    if login_table.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert("Username Already Exists");window.location='/admin_add_hospital'</script>''')


    fs = FileSystemStorage()
    fp = fs.save(image.name,image)

    OB=login_table()
    OB.username=username
    OB.password=password
    OB.type='hospital'
    OB.save()

    OB1=hospital_table()
    OB1.name=name
    OB1.image=fp
    OB1.place=place
    OB1.pin=pin
    OB1.post=post
    OB1.email=email
    OB1.contactNumberOne=contactNumberOne
    OB1.contactNumberTwo=contactNumberTwo
    OB1.Latitude=Latitude
    OB1.Longitude=Longitude
    OB1.LOGIN=OB
    OB1.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location='/admin_hospital#a'</script>''')


def admin_admin_home(request):
    return render(request,"admin/index.html")


def admin_feedback(request):
    a=feedback_table.objects.all()
    return render(request,"admin/Feedback.html",{"data":a})

def admin_notification(request):
    return render(request,"admin/Notification.html")


def admin_notification_post(request):
    notification=request.POST['textfield']
    ob=notification_table()
    ob.notification=notification
    ob.date=datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Notification send");window.location="/admin_notification"</script>''')


def admin_view_ambulance(request):
    a=ambulance_table.objects.all()
    return render(request,"admin/View Ambulance.html",{"data":a})


def admin_search_ambulance(request):
    VehicleNumber = request.POST['textfield']
    a = ambulance_table.objects.filter(VehicleNumber__icontains=VehicleNumber)
    return render(request, "admin/View Ambulance.html", {"data": a})


def hospital_view_ambulance(request):
    a=ambulance_table.objects.filter(Hospital__LOGIN_id=request.session['lid'])
    return render(request,"Hospital/View Ambulance_hospital.html",{"data":a})

def hospital_search_ambulance(request):
    VehicleNumber = request.POST['textfield']
    a=ambulance_table.objects.filter(Hospital__LOGIN_id=request.session['lid'],VehicleNumber__icontains=VehicleNumber)
    return render(request,"Hospital/View Ambulance_hospital.html",{"data":a})


def admin_hospital(request):
    a=hospital_table.objects.all()
    return render(request,"admin/View Hospital.html",{"data":a})

def admin_search_hospital(request):
    name = request.POST['textfield']
    a = hospital_table.objects.filter(name__icontains=name)
    return render(request, "admin/View Hospital.html", {"data": a})


def hospital_add_ambulance_hospital(request):
    return render(request,"Hospital/Add AmbulanceHospital.html")

def hospital_ambulance_message(request):
    ob=ambulance_table.objects.filter(Hospital__LOGIN=request.session["lid"])
    return render(request,"Hospital/Ambulance Message.html",{"ambu":ob})

def hospital_ambulance_message_post(request):
    EmergencyMessage = request.POST['textarea']
    Aambu = request.POST['select']
    ob=message_table()
    ob.AMBULANCE_id=Aambu
    ob.EmergencyMessage=EmergencyMessage
    ob.Date = datetime.datetime.now()
    ob.Time = datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Emergency Message Send");window.location="/hospital_ambulance_message#a"</script>''')








def hospital_ambulance_registration(request):
    return render(request,"Hospital/Ambulance Registration.html")

def hospital_hospital_home(request):
    um=user_message_table.objects.all()
    umc=um.count()
    request.session['umc']=umc

    a = ambulance_table.objects.filter(Hospital__LOGIN_id=request.session['lid'])
    ac = a.count()
    request.session['ac'] = ac

    am = message_table.objects.all()
    amc = am.count()
    request.session['amc'] = amc

    p = patient_table.objects.all()
    pc = p.count()

    print(pc)
    request.session['pc'] = pc






    return render(request,"Hospital/index.html")

def hospital_view_message(request):
    a = user_message_table.objects.all()
    return render(request, "Hospital/View Messages.html", {"data": a})

def hospital_patient_condition(request):
    a = patient_table.objects.all()
    return render(request,"Hospital/View Patient Condition.html",{"data":a})



def delete_patient_info(request,id):
    ob=patient_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Patient Info Deleted Successfully");window.location='/hospital_patient_condition'</script>''')





def delete_hospital(request,id):
    ob=hospital_table.objects.get(LOGIN_id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Hospital Deleted Successfully");window.location='/admin_hospital'</script>''')


def edit_hospital(request,id):
    request.session['id']=id
    ob=hospital_table.objects.get(id=id)
    return render(request,"admin/Edit Hospital.html",{'data':ob})

def edithospitalPost(request):
    ob = hospital_table.objects.get(id=request.session['id'])

    if 'file' in request.FILES:
        img=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(img.name,img)
        ob.image =fsave
    ob.name = request.POST['textfield']

    ob.place = request.POST['textfield6']
    ob.pin = request.POST['textfield2']
    ob.post = request.POST['textfield3']
    ob.email = request.POST['textfield4']
    ob.contactNumberOne = request.POST['textfield5']
    ob.contactNumberTwo = request.POST['textfield7']
    ob.Latitude = request.POST['textfield8']
    ob.Longitude = request.POST['textfield9']
    ob.save()
    return HttpResponse('''<script>alert("Edited Hospital Successfully");window.location='/admin_hospital'</script>''')


def delete_ambulance(request,id):
    ob=ambulance_table.objects.get(LOGIN_id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Ambulance Deleted Successfully");window.location='/admin_view_ambulance#a'</script>''')

def delete_ambulance_hospital(request,id):
    ob=ambulance_table.objects.get(LOGIN_id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Ambulance Deleted Successfully");window.location='/hospital_view_ambulance#a'</script>''')

def edit_ambulance(request,id):
    request.session['id']=id
    p=hospital_table.objects.all()
    ob=ambulance_table.objects.get(id=id)
    return render(request,"admin/Edit Ambulance.html",{'data':ob,'val':p})

def edit_ambulance_hospital(request,id):
    request.session['id']=id
    p=hospital_table.objects.all()
    ob=ambulance_table.objects.get(id=id)
    return render(request,"Hospital/Edit Ambulance_hospital.html",{'data':ob,'val':p})

def editAmbulancePost(request):
    ob = ambulance_table.objects.get(id=request.session['id'])
    ob.VehicleNumber =request.POST['textfield']
    ob.Hospital_id=request.POST['select']
    ob.Type = request.POST['select1']
    ob.Status = request.POST['select2']
    ob.save()
    return HttpResponse('''<script>alert("Edited ambulance Successfully");window.location='/admin_view_ambulance#a'</script>''')


def editAmbulancePost_hospital(request):
    ob = ambulance_table.objects.get(id=request.session['id'])
    ob.VehicleNumber =request.POST['textfield']
    ob.Hospital_id=request.POST['select']
    ob.Type = request.POST['select1']
    ob.Status = request.POST['select2']
    ob.save()
    return HttpResponse('''<script>alert("Edited ambulance Successfully");window.location='/hospital_view_ambulance#a'</script>''')

def trackAmbulance(request,id):
    ob=location_table.objects.get(LOGIN_id=id)
    return render(request,'admin/trackAmbulance.html',{'details':ob})


def hospital_track_ambulances(request,id):
    ob = location_table.objects.get(LOGIN_id=id)
    return render(request, "Hospital/track.html",{'details':ob})



#-----------------------------------------------------------------------------------------------------------------------

def user_registration(request):
    name = request.POST['fname']
    PhoneNumber = request.POST['phone']
    email = request.POST['email']

    username = request.POST['uname']
    password = request.POST['password']

    log = login_table()
    log.username = username
    log.password=password
    log.type = 'user'
    log.save()

    ob = user_table()
    ob.LOGIN = log
    ob.name=name
    ob.PhoneNumber=PhoneNumber
    ob.email=email

    ob.save()
    return JsonResponse({'task':'valid'})




def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd)
    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "lid": ob.id,"type":ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)






# def view_nearest_ambulances(request):
#     ob=ambulance_table.objects.all()
#     print(ob,"HHHHHHHHHHHHHHH")
#     mdata=[]
#     for i in ob:
#         data={'Ambulance':i.VehicleNumber,'Hospital':i.Hospital.name,'Type':i.Type,'Status':i.Status,'id':i.id}
#         mdata.append(data)
#         print(mdata)
#     return JsonResponse({"status":"ok","data":mdata})


from django.http import JsonResponse
from .models import ambulance_table, location_table
from django.db import connection
def view_nearest_ambulances2(request):
    try:

        try:
            id = request.POST['id']
            ambulances = ambulance_request_table.objects.filter(Status__contains='Accepted', id__gt=id).order_by('-id')
            print("hjhhj", ambulances)

            print(ambulances, "jkjkj ")
            if len(ambulances) > 0:
                return JsonResponse({"status": "ok", 'id': ambulances[0].id})
            else:
                return JsonResponse({"status": "no"})
        except:
            connection.close()
            id = request.POST['id']
            ambulances = ambulance_request_table.objects.filter(Status__contains='Accepted', id__gt=id).order_by('-id')
            print("ggg", ambulances)
            mdata2 = []

            for ambulance in ambulances:
                ambulance = ambulance.AMBULANCE_ID

                data = {
                    'Ambulance': ambulance.VehicleNumber + "Passing",
                }
                mdata2.append(data)
            print(mdata2, "jkjkj ")
            return JsonResponse({"status": "ok", "data2": mdata2, 'id': ambulances[0].id})
    finally:
        connection.close()

def view_nearest_ambulances(request):
    try:
        ambulances = ambulance_table.objects.all()
        mdata = []

        for ambulance in ambulances:
            location = location_table.objects.filter(LOGIN=ambulance.LOGIN).order_by('-date').first()

            data = {
                'Ambulance': ambulance.VehicleNumber,
                'Hospital': ambulance.Hospital.name,
                'Type': ambulance.Type,
                'Status': ambulance.Status,
                'id': ambulance.id,
                'Latitude': str(location.Latitude) if location else None,
                'Longitude': str(location.Longitude) if location else None,
            }
            mdata.append(data)


        return JsonResponse({"status": "ok", "data": mdata})
    finally:
        connection.close()


def get_username(request, lid):
    try:
        # Fetch the user from login_table
        user = get_object_or_404(login_table, id=lid)

        # Fetch the corresponding entry from user_table using the foreign key
        user_entry = get_object_or_404(user_table, LOGIN=user)

        return JsonResponse({'username': user.username, 'email': user_entry.email}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)




def sendfeedback(request):
    comp = request.POST['feedback']
    lid = request.POST['lid']
    lob = feedback_table()
    lob.USER_ID = user_table.objects.get(LOGIN__id=lid)
    lob.Feedback = comp
    lob.date = datetime.datetime.today()
    lob.save()
    return JsonResponse({'task': 'ok'})



def view_nearest_traffic_notifivcation(request):
    ob=notification_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'notification':i.notification,'date':str(i.date),'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



from .models import ambulance_request_table, ambulance_table, user_table



def user_send_ambulance_request(request):
    lid = request.POST['lid']  # User's login ID
    latitude = float(request.POST['latitude'])
    longitude = float(request.POST['longitude'])
    bypass = request.POST.get('bypass', 'false')

    user = user_table.objects.get(LOGIN_id=lid)

    # Check if there is already a pending request for the user
    existing_request = ambulance_request_table.objects.filter(
        USER_ID=user,
        Status='Requested'
    ).first()

    if existing_request:
        return JsonResponse({"status": "Already Sent!"})

    if bypass.lower() != 'true':
        # Check if the location is too close to any existing requests
        existing_requests = ambulance_request_table.objects.filter(Q(Status='Requested') | Q(Status__startswith='Accepted'))
        new_location = (latitude, longitude)
        duplicate_threshold = 10000  # Distance threshold in meters

        for request in existing_requests:
            existing_location = (float(request.latitude), float(request.longitude))
            distance = calculate_distance(new_location, existing_location)

            if distance <= duplicate_threshold:
                return JsonResponse({"status": "close"})

    # If no existing request, create a new one
    ambulance_request_table.objects.create(
        USER_ID=user,
        date=datetime.datetime.now(),
        username=user.name,
        request='Request Sent',
        Status='Requested',
        latitude=latitude,
        longitude=longitude
    )

    return JsonResponse({"status": "ok"})



def view_messages_from_hospital(request):
    ob=message_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'EmergencyMessage':i.EmergencyMessage,'date':str(i.Date),'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def send_patient_info(request):
    patient_info = request.POST['patient_info']
    lid = request.POST['lid']
    lob = patient_table()
    lob.AMBULANCE_ID = ambulance_table.objects.get(LOGIN__id=lid)
    lob.PatientCondition = patient_info
    lob.date = datetime.datetime.today()
    lob.save()
    return JsonResponse({'task': 'ok'})



from django.http import JsonResponse
import datetime
from .models import location_table, login_table

def updatelocation(request):
    print(request.POST,'locationssss')


    lid = request.POST["lid"]
    print(lid,'liddddd')
    lon1 = float(request.POST['lon'])
    lat1 = float(request.POST['lat'])
    print(lat1,'lateeeeeeeee')



    ob, created = location_table.objects.get_or_create(LOGIN_id=lid)

    ob.Longitude = lon1
    ob.Latitude = lat1

    ob.date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ob.save()

    return JsonResponse({"task": "valid", "message": "Location updated succeyssfull"})




def update_ambulance_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lid = data.get('lid')
            status = data.get('status')

            # Find ambulance by LOGIN foreign key
            ambulance = ambulance_table.objects.get(LOGIN_id=lid)
            ambulance.Status = status
            ambulance.save()

            return JsonResponse({'message': 'Status updated successfully'}, status=200)
        except ambulance_table.DoesNotExist:
            return JsonResponse({'error': 'Ambulance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)



def get_ambulance_requests(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lid = data.get('lid')

            # Get the ambulance object based on the LOGIN foreign key
            ambulance = ambulance_table.objects.get(LOGIN_id=lid)

            # Get unassigned requests OR requests accepted by this ambulance
            # requests = ambulance_request_table.objects.filter(
            #     Q(AMBULANCE_ID__isnull=True) | Q(AMBULANCE_ID=ambulance)
            # ).values()
            requests = ambulance_request_table.objects.filter(deleted=False).order_by('-date').values();
            return JsonResponse({'requests': list(requests)}, status=200)

        # except ambulance_table.DoesNotExist:
        #     return JsonResponse({'error': 'Ambulance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def ambulance_accept_request(request, request_id):
    lid = json.loads(request.body).get('lid')
    ambulance = ambulance_table.objects.get(LOGIN_id=lid)

    try:
        # Check if the ambulance already has an accepted request
        if ambulance_request_table.objects.filter(AMBULANCE_ID=ambulance, Status__startswith='Accepted').exists():
            return JsonResponse(
                {"status": "You have already accepted a request. Complete it before accepting another."})



        ambulance_request = ambulance_request_table.objects.get(id=request_id, Status='Requested')
        ambulance_request.AMBULANCE_ID = ambulance
        ambulance_request.Status = f'Accepted by {ambulance.VehicleNumber}'
        ambulance_request.save()

        return JsonResponse({"status": "Accepted","acceptedlid": lid})
    except ambulance_request_table.DoesNotExist:
        return JsonResponse({"status": "Request Already Accepted or Not Found"})



def ambulance_complete_request(request, request_id):
    lid = json.loads(request.body).get('lid')
    ambulance = ambulance_table.objects.get(LOGIN_id=lid)

    try:
        ambulance_request = ambulance_request_table.objects.get(id=request_id, AMBULANCE_ID=ambulance, Status__startswith='Accepted')
        ambulance_request.Status = f'Completed by {ambulance.VehicleNumber}'
        ambulance_request.save()

        return JsonResponse({"status": "Completed"})
    except ambulance_request_table.DoesNotExist:
        return JsonResponse({"status": "Request Not Found or Already Completed"})


def delete_ambulance_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            request_id = data.get('id')

            # Mark the request as deleted
            ambulance_request_table.objects.filter(id=request_id).update(deleted=True)

            return JsonResponse({'message': 'Request deleted successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .models import patient_table, ambulance_table

@csrf_exempt
def upload_voice_message(request):
    if request.method == 'POST' and request.FILES.get('voice_message'):
        try:
            # Get login ID (lid) from the request
            lid = request.POST.get('lid')
            print(f"Received lid: {lid}")

            # Find the corresponding ambulance using the login ID
            ambulance = ambulance_table.objects.filter(LOGIN__id=lid).first()

            if not ambulance:
                return JsonResponse({'error': 'Ambulance not found for this login ID'}, status=400)

            voice_file = request.FILES['voice_message']
            file_path = default_storage.save(f'voice_messages/{voice_file.name}', voice_file)

            # Create patient record linked to this ambulance
            patient = patient_table.objects.create(
                AMBULANCE_ID=ambulance,
                PatientCondition=file_path
            )

            return JsonResponse({'message': 'Voice message uploaded successfully!', 'file_path': file_path}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


from geopy.distance import geodesic
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from geopy.distance import geodesic

@csrf_exempt

def calculate_distance(coord1, coord2):
    distance = geodesic(coord1, coord2).meters
    return distance

def receive_user_location(request):
    if request.method == 'POST':
        print(request.POST)
        if True:
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']

            if latitude and longitude:
                ob=ambulance_request_table.objects.filter(Status__istartswith='Accepted')


                for j in ob:
                    kk=[j.AMBULANCE_ID.LOGIN.id]
                    ambulance_locations = location_table.objects.filter(LOGIN__id__in=kk).values('Latitude', 'Longitude')
                    # print(ambulance_locations)
                    print(ambulance_locations,"++++++++++++++++++++++++++++++++")
                    print(ambulance_locations,"++++++++++++++++++++++++++++++++")
                    print(ambulance_locations,"++++++++++++++++++++++++++++++++")
                    print(ambulance_locations,"++++++++++++++++++++++++++++++++")
                    print(ambulance_locations,"++++++++++++++++++++++++++++++++")
                    for location in ambulance_locations:
                        ambulance_location = (float(location['Latitude']), float(location['Longitude']))
                        distance = haversine((float(latitude),float(longitude)), ambulance_location)
                        if distance<1:
                            return JsonResponse({"task":"ok"})
                        else:
                            print('no ambulances')
            else:
                return JsonResponse({'task': 'na1', 'message': 'Invalid location data'})

    return JsonResponse({'task': 'na3', 'message': 'Invalid request method'})


import math

def haversine(coord1, coord2):
    """
    Calculate the Haversine distance between two geo-coordinates.
    Parameters:
        coord1 (tuple): (latitude, longitude) of the first point in decimal degrees.
        coord2 (tuple): (latitude, longitude) of the second point in decimal degrees.
    Returns:
        float: Distance between the two points in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = math.radians(lat1), math.radians(lon1)
    lat2, lon2 = math.radians(lat2), math.radians(lon2)

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance


import requests
from django.http import JsonResponse
from django.conf import settings
from django.conf import settings
from django.http import JsonResponse
import requests


def medical_chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        chat_history = request.POST.get('chat_history')  # Get chat history from the request

        # Construct the correct Gemini API URL with API key
        api_url = f"{settings.GEMINI_API_URL}?key={settings.GEMINI_API_KEY}"

        # Prepare the payload with chat history
        payload = {
            "contents": [{

                 "parts": [
            {"text": "You are a professional medical assistant. Provide accurate and helpful medical information and advice. If necessary, ask for more medical details like symptoms, duration, and medications."},
            *[{"text": msg} for msg in json.loads(chat_history)],
            {"text": user_message}
        ]
            }]
        }

        try:
            response = requests.post(
                api_url,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()

            response_data = response.json()

            # Extract response text
            if 'candidates' in response_data and len(response_data['candidates']) > 0:
                bot_response = response_data['candidates'][0]['content']['parts'][0]['text']
                return JsonResponse({"response": bot_response})
            else:
                return JsonResponse({"error": "No response from Gemini"}, status=500)

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"API request failed: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
