from django.shortcuts import render,redirect
from Guest.models import *
from User   .models import *
# Create your views here.

def homepage(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/HomePage.html')

def myprofile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/Myprofile.html',{'dat':data})

def editprofile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        data.user_name=request.POST.get('txt_name')
        data.user_email=request.POST.get('txt_email')
        data.user_address=request.POST.get('txt_address')
        data.user_contact=request.POST.get('txt_contact')
        data.save()
        return render(request, 'User/EditProfile.html',{'msg':"Profile Updated"})
    else:
        return render(request, 'User/EditProfile.html',{'dat':data})

def changepassword(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    dbpass=data.user_password
    print(dbpass)
    if request.method=='POST':
        oldpass=request.POST.get('txt_old')
        newpass=request.POST.get('txt_new')
        cpass=request.POST.get('txt_cpass')
        if dbpass==oldpass:
            if newpass==cpass:
                if dbpass==newpass:
                    return render(request,'User/ChangePassword.html',{'msg':"Already Used Try Another"})
                else:
                    data.user_password=newpass
                    data.save()
                    return render(request,'User/ChangePassword.html',{'msg1':"Password Updated"})

                    # return redirect('User:myprofile')
            else:
                return render(request,'User/ChangePassword.html',{'msg':"Password Not Match"})
        else:
            return render(request,'User/ChangePassword.html',{'msg':"Incorrect Current Password"})  
        
    return render(request, 'User/ChangePassword.html')

def request(request):
    if request.method == "POST":
        return render(request, 'User/Request.html')
    else:
        return render(request, 'User/Request.html')


# Load the model once when the server starts
import os
import cv2
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO

MODEL_PATH = os.path.join("Assets/Model", "accedent.h5")
model = load_model(MODEL_PATH)

def predict_video(request):
    """
    Handles video input, extracts frames, predicts accident status, and stops on first detection.
    """
    if request.method == "POST" and request.FILES.get("video"):

        data=tbl_user.objects.get(id=request.session['uid'])

        uploaded_video = request.FILES["video"]
        video_path = os.path.join("temporary_videos", uploaded_video.name)  # Save temporarily
        
        # Save the uploaded video file
        os.makedirs("temporary_videos", exist_ok=True)
        with open(video_path, "wb") as f:
            for chunk in uploaded_video.chunks():
                f.write(chunk)

        # Initialize variables
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            os.remove(video_path)
            return render(request, "Engine/Prediction.html", {"error": "Unable to open video file."})
        
        frame_count = 0
        IMG_HEIGHT, IMG_WIDTH = 250, 250  # Update as per your model's input size
        detected_frame_path = None
        specific_dir = "Assets/Detection"  # Directory to save detected frames
        os.makedirs(specific_dir, exist_ok=True)

        while True:
            grabbed, frame = cap.read()
            if not grabbed:
                break  # End of video
            
            frame_count += 1
            if frame_count % 30 == 0:  # Sample every 30th frame
                # Resize the frame to model's input dimensions
                resized_frame = tf.image.resize_with_pad(frame, IMG_HEIGHT, IMG_WIDTH)
                resized_frame = resized_frame.numpy().astype("uint8")
                
                # Convert frame to batch and predict
                img_array = tf.keras.utils.img_to_array(resized_frame)
                img_batch = np.expand_dims(img_array, axis=0)
                prediction = (model.predict(img_batch) > 0.5).astype("int32")
                
                if prediction[0][0] == 0:  # Accident detected
                    # Save the frame as an image
                    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    buffer = BytesIO()
                    pil_image.save(buffer, format="JPEG")
                    buffer.seek(0)
                    detected_frame_path = f"detected_frame_{frame_count}.jpg"
                    with open(os.path.join("temporary_videos", detected_frame_path), "wb") as img_file:
                        img_file.write(buffer.read())

                    #for saving to dir
                    detected_frame = os.path.join(specific_dir, f"detected_frame_{frame_count}.jpg")
                    detected_frame = detected_frame.replace("\\", "/")
                    print(detected_frame)
                    pil_image.save(detected_frame, format="JPEG")
                    
                    break  # Stop processing after detection

        cap.release()
        os.remove(video_path)  # Cleanup temporary video file

        if detected_frame_path:
            req = tbl_request.objects.create(request_file=detected_frame,user_id=data)
            hospital = tbl_hospital.objects.get(place=data.place.id)
            tbl_requestbody.objects.create(request_id=tbl_request.objects.get(id=req.id),hospital_id=tbl_hospital.objects.get(id=hospital.id))
            authority = tbl_authority.objects.get(place=data.place.id)
            # print(authority)
            tbl_requestbody.objects.create(request_id=tbl_request.objects.get(id=req.id),authority_id=tbl_authority.objects.get(id=authority.id))
            return render(request, "User/Predict.html", {"detected_frame": detected_frame_path, "message": "Accident Detected"})
        else:
            return render(request, "User/Predict.html", {"message": "No Accident Detected"})
    
    return render(request, "User/Predict.html")

def myrequest(request):
    req=tbl_request.objects.filter(user_id=request.session['uid'])
    return render(request, 'User/MyRequest.html',{'req':req})