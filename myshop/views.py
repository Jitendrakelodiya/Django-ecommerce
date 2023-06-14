from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def Home(request):
    return render(request,"home.html")

# def (request):
#     return render(request,"about.html")

def ContactUs(request):
  if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        number = request.POST.get('number')
        print(number)
        message = request.POST.get('message')
        print(message)

        content = {
          "name":name,
          "email": email,
          "number": number,
          "message": message
        }
        print(content)

        msg_plain = render_to_string('mail/mail.html',content)
        print(msg_plain)
            
        subject = "User information mail"
        # message1 = "hello how are you"
        send_mail(subject,msg_plain,'jitendra.kelodiya2020@gmail.com',["jitendra.kelodiya2020@gmail.com"],fail_silently=False)
        print("sent succesfully")
  return render(request,"contact.html")

def AboutUs(request):

    return render(request,"about.html")  

