import mysql.connector
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.

#Create database connection function
def getdb():
    mydb = mysql.connector.connect( host="localhost",user="root", passwd="",database="parking_db")
    return mydb
    
# Create your views here.
def index(request):
   
   sel = "select count(t_id) from type_tb"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel)
   typecount = mycursor.fetchall()

   sel1 = "select count(r_id) from rate_tb"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel1)
   ratecount = mycursor.fetchall()


   sel2 = "select count(s_id) from slot_tb"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel2)
   slotcount = mycursor.fetchall()


   sel3 = "select count(u_id) from user_tb"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel3)
   usercount = mycursor.fetchall()

   sel4 = "select count(b_id) from booking_tb "
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel4)
   bookingcount = mycursor.fetchall()

   sel5 = "select count(f_id) from feedback_tb where f_status='Show'"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel5)
   showfeedbackcount = mycursor.fetchall()

   sel5 = "select count(f_id) from feedback_tb where f_status='Hide'"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel5)
   hidefeedbackcount = mycursor.fetchall()



   sel6 = "select count(b_id) from booking_tb where b_status='Pending'"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel6)
   pendingstatuscount = mycursor.fetchall()



   sel7 = "select count(b_id) from booking_tb where b_status='Confirm'"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel7)
   confirmstatuscount = mycursor.fetchall()




   sel8 = "select count(b_id) from booking_tb where b_status='Complete'"
   # connection create object
   mydb = getdb()
   mycursor = mydb.cursor()
   #query execute
   mycursor.execute(sel8)
   completestatuscount = mycursor.fetchall()

   
   
   alldate = {

      'typecount' : typecount,
       'ratecount' : ratecount,
       'slotcount' : slotcount,
       'usercount' : usercount,
       'bookingcount' : bookingcount,
       'showfeedbackcount' : showfeedbackcount,
       'hidefeedbackcount' : hidefeedbackcount,
       'pendingstatuscount' : pendingstatuscount,
       'confirmstatuscount' : confirmstatuscount,
       'completestatuscount' : completestatuscount,

   }
   
   return render(request,'index.html',alldate);

def managetype(request):
   try:
      if request.POST:
         #variable Decleration
         tname = request.POST.get("tname")
         tstatus = request.POST.get("tstatus")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         
         #insert code
         ins = "INSERT INTO `type_tb`(`t_name`, `t_status`, `t_cdate`, `t_udate`) VALUES ('"+str(tname)+"','"+str(tstatus)+"','"+(cdate)+"','"+(cdate)+"')" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(ins)
         mydb.commit()
         return redirect('type')
      elif request.GET.get("type_del") !=None:
         type_dl = request.GET.get("type_del")
         dl = "delete from `type_tb` where t_id ='"+ str(type_dl) +"' " 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('type')

      else:
         sel = "select * from type_tb"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'type.html',{'record':myresult});

   except NameError:
        print("internal error")
   except:
        print('Error returned')   
      
def managetype_edit(request):
   try:
      if request.POST:
         #variable Decleration
         tname = request.POST.get("tname")
         tstatus = request.POST.get("tstatus")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         t_id = request.GET.get("type_edt")
         #insert code
         up = "UPDATE `type_tb` SET  `t_name`='"+str(tname)+"',`t_status`='"+str(tstatus)+"',`t_udate`='"+(cdate)+"' where t_id = '"+str(t_id)+"'" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(up)
         mydb.commit()
         return redirect('type')
      
      elif request.GET.get("type_edt") !=None:
         t_id = request.GET.get("type_edt")
         sel = "select * from type_tb where t_id = '"+str(t_id)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'type_edit.html',{'record':myresult});

   except NameError:
        print("internal error")
   except:
        print('Error returned') 


def managelogin(request):
   try:
      msg = ""
      if request.POST:
         #variable Decleration
         username = request.POST.get("username")
         password = request.POST.get("password")
       
         sel = "select * from admin_tb where a_username = '"+str(username)+"' and a_password = '"+str(password)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
        
         if (len(myresult)==0):
                msg = " Invalid Username Or Password.! "
         else:
            request.session["name"] =  username
            request.session["img"] =  myresult[0][3]
            request.session["time"] =  str(myresult[0][4])

            return redirect("index")

      return render(request,'login.html',{'msg':msg});

   except NameError:
        print("internal error")
   except:
        print('Error returned') 

def managelogout(request):
   try:
        #variable decleration
        uname = request.session["name"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        ins = "update admin_tb set a_lastseen = '"+cdate+"' where a_username = '"+uname+"'"
           
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(ins)
        mydb.commit()
        
        request.session["name"] =  None
        request.session["img"] =  None
        request.session["time"] =  None
        return redirect("login") 

   except NameError:
        print("internal error")
   except:
        print('Error returned') 


def managerate(request):
   try:
      if request.POST:
         #variable Decleration
         rtype = request.POST.get("rtype")
         rrate = request.POST.get("rrate")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         
         #insert code
         ins = "INSERT INTO `rate_tb`(`r_t_id`,`r_rate`, `r_cdate`, `r_udate`) VALUES ('"+str(rtype)+"','"+str(rrate)+"','"+(cdate)+"','"+(cdate)+"')" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(ins)
         mydb.commit()
         return redirect('rate')

      elif request.GET.get("rate_del") !=None:
         rate_dl = request.GET.get("rate_del")
         dl = "delete from `rate_tb` where r_id ='"+ str(rate_dl) +"'" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('rate')

      else:
         
         sel = "select * from rate_tb,type_tb where type_tb.t_id =rate_tb.r_t_id order by rate_tb.r_id desc"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()


         sel1 = "select * from type_tb where t_status = 'Active'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel1)
         resultype = mycursor.fetchall()
         
         alldata = {
            'record':myresult,
            'resultype' : resultype

         }

         return render(request,'rate.html',alldata);

   except NameError:
        print("internal error")
   except:
        print('Error returned') 


def managerate_edit(request):
   try:
      if request.POST:
         #variable Decleration
         tname = request.POST.get("tname")
         rrate = request.POST.get("rrate")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         r_id = request.GET.get("rate_edt")
         #insert code
         up = "UPDATE `rate_tb` SET  `r_t_id` = '"+tname+"' ,`r_rate`='"+str(rrate)+"',`r_udate`='"+(cdate)+"' where r_id = '"+str(r_id)+"'" 
         # print(up)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(up)
         mydb.commit()
         return redirect('rate')
      
      elif request.GET.get("rate_edt") !=None:
         r_id = request.GET.get("rate_edt")
         sel = "select * from rate_tb where r_id = '"+str(r_id)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()

         sel1 = "select * from type_tb where t_status = 'Active'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel1)
         resultype = mycursor.fetchall()

         alldata = {
            'record':myresult,
            'resultype' : resultype

         }


         return render(request,'rate_edit.html',alldata);

      elif request.GET.get("rate_del") !=None:
         rate_dl = request.GET.get("rate_del")
         dl = "delete from `rate_tb` where r_id ='"+ str(rate_dl) +"'" 
         #print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('rate')

   except NameError:
        print("internal error")
   except:
        print('Error returned') 

def managefeedback(request):
   try:
      if request.GET.get("f_del") != None:
         f_del = request.GET.get("f_del")
         dl = "DELETE FROM `feedback_tb` where f_id ='"+str(f_del)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('feedback')

      elif request.GET.get("f_id") != None:
         f_id = request.GET.get("f_id")
         f_status = request.GET.get("f_status")
         if f_status == 'Hide':
            f_status = 'Show'
         else:
            f_status = 'Hide'
         dl = "update `feedback_tb` set f_status = '"+f_status+"' where f_id ='"+str(f_id)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('feedback')   
      else:
         sel = "select * from feedback_tb"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'feedback.html',{'record':myresult});
   except NameError:
      print("internal error")
   except:
      print('Error returned')




def manageslot(request):
   try:
      if request.POST:
         #variable Decleration
         rtype = request.POST.get("rtype")
         slot = request.POST.get("slot")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         
         #insert code
         ins = "INSERT INTO `slot_tb`(`s_t_id`,`s_slot`,`s_cdate`, `s_udate`) VALUES ('"+str(rtype)+"','"+str(slot)+"','"+(cdate)+"','"+(cdate)+"')" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(ins)
         mydb.commit()
         return redirect('slot')
         
      elif request.GET.get("slot_del") !=None:
         slot_dl = request.GET.get("slot_del")
         dl = "delete from `slot_tb` where s_id ='"+ str(slot_dl) +"' " 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('slot')

      else:
         sel = "select * from slot_tb,type_tb where type_tb.t_id = slot_tb.s_t_id"
         
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         #return render(request,'slot.html',{'record':myresult});

         sel1 = "select * from type_tb where t_status = 'Active'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel1)
         resultype = mycursor.fetchall()
         
         alldata = {
            'record':myresult,
            'resultype' : resultype

         }
         return render(request,'slot.html',alldata);

   except NameError:
        print("internal error")
   except:
        print('Error returned') 




def manageslot_edit(request):
   try:
      if request.POST:
         #variable Decleration
         tname = request.POST.get("tname")
         slot = request.POST.get("slot")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         s_id = request.GET.get("slot_edt")
         #insert code
         up = "UPDATE `slot_tb` SET  `s_t_id`='"+str(tname)+"',`s_slot`='"+str(slot)+"',`s_udate`='"+(cdate)+"' where s_id = '"+str(s_id)+"'" 
         #print(ins)

         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(up)
         mydb.commit()
         return redirect('slot')
      
      elif request.GET.get("slot_edt") !=None:
         s_id = request.GET.get("slot_edt")
         sel = "select * from slot_tb where s_id = '"+str(s_id)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()

         #return render(request,'slot_edit.html',{'record':myresult});
         sel1 = "select * from type_tb where t_status = 'Active'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel1)
         resultype = mycursor.fetchall()

         alldata = {
            'record':myresult,
            'resultype' : resultype

         }


         return render(request,'slot_edit.html',alldata);


   except NameError:
        print("internal error")
   except:
        print('Error returned') 



def manageuser(request):
   try:
      if request.POST:
         #variable Decleration
         uname = request.POST.get("uname")
         ucontact = request.POST.get("ucontact")

         uimage = request.FILES["uimage"]
         img = FileSystemStorage()
         fimg = img.save(uimage.name,uimage)

         uaname = request.POST.get("uaname")
         upassword = request.POST.get("upassword")
         ustatus = request.POST.get("ustatus")
         cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         ins = "INSERT INTO `user_tb`(`u_name`, `u_contact`, `u_image`, `u_address`, `u_password`, `u_status`, `u_cdata`, `u_udate`) VALUES ('"+str(uname)+"','"+str(ucontact)+"','"+str(fimg)+"','"+str(uaname)+"','"+str(upassword)+"','"+str(ustatus)+"','"+(cdate)+"','"+(cdate)+"')"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(ins)
         mydb.commit()
         return redirect('user')
      elif request.GET.get("user_del") != None:
         user_del = request.GET.get("user_del")
         dl = "DELETE FROM `user_tb` where u_id ='"+str(user_del)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('user')

      elif request.GET.get("u_id") != None:
         u_id = request.GET.get("u_id")
         u_status = request.GET.get("u_status")
         if u_status == 'Active':
            u_status = 'Deactive'
         else:
            u_status = 'Active'
         dl = "update `user_tb` set u_status = '"+u_status+"' where u_id ='"+str(u_id)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('user')   
      else:
         sel = "select * from user_tb order by u_id desc"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'user.html',{'record':myresult});
   except NameError:
      print("internal error")

   except:
      print('Error returned')

def managebooking(request):
   try:
      
      if request.GET.get("b_id") != None:
         b_id = request.GET.get("b_id")
         b_status = request.GET.get("b_status")

         if b_status == 'Pending':
            b_status = 'Confirm'
         elif b_status == 'Confirm':
            b_status = 'Complete'
         else:
            b_status = 'Pending'

         dl = "update `booking_tb` set b_status = '"+b_status+"' where b_id ='"+str(b_id)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('booking')
      
      elif request.GET.get("booking_del") != None:
         booking_del = request.GET.get("booking_del")
         dl = "DELETE FROM `booking_tb` where b_id ='"+str(booking_del)+"'"
         # print(ins)
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(dl)
         mydb.commit()
         return redirect('booking')
      else:
         sel = "select * from booking_tb,user_tb,type_tb where booking_tb.b_u_id = user_tb.u_id and booking_tb.b_t_id = type_tb.t_id"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'booking.html',{'record':myresult});
      
      

   except NameError:
      print("internal error")

   except:
      print('Error returned')



def managebookingreport(request):
   try:
      if request.POST:
         sdate = request.POST.get("sdate")
         edate = request.POST.get("edate")

         sel = "select * from booking_tb,user_tb,type_tb where booking_tb.b_u_id = user_tb.u_id and booking_tb.b_t_id = type_tb.t_id and booking_tb.b_date BETWEEN '"+str(sdate)+"' and '"+str(edate)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'booking_report.html',{'record':myresult});
      return render(request,'booking_report.html',{});   
      
      

   except NameError:
      print("internal error")

   except:
      print('Error returned')



def manageuserreport(request):
   try:
      if request.POST:
         sdate = request.POST.get("sdate")
         edate = request.POST.get("edate")

         sel = "select * from user_tb where DATE(u_udate) BETWEEN '"+str(sdate)+"' and '"+str(edate)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'user_report.html',{'record':myresult});
      return render(request,'user_report.html',{});   
      
      

   except NameError:
      print("internal error")

   except:
      print('Error returned')


def managebookingstatusreport(request):
   try:
      if request.POST:
         bstatus = request.POST.get("bstatus")
         
         sel = "select * from booking_tb,user_tb,type_tb where booking_tb.b_u_id = user_tb.u_id and booking_tb.b_t_id = type_tb.t_id and b_status = '"+str(bstatus)+"'"
         # connection create object
         mydb = getdb()
         mycursor = mydb.cursor()
         #query execute
         mycursor.execute(sel)
         myresult = mycursor.fetchall()
         return render(request,'status_report.html',{'record':myresult});
      return render(request,'status_report.html',{});   
      
      

   except NameError:
      print("internal error")

   except:
      print('Error returned')
