from module_settings import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static' + '/images'
mysql.init_app(app)
app.secret_key = 'random string'
mail = Mail(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image Only!'), FileRequired(u'Choose a file!')])
    submit = SubmitField(u'Upload')

@app.route("/")
def root():
    try:
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            return render_template('home.html',  loggedIn=loggedIn, firstName=firstName)
        else:
            loggedIn = True
            loginclassdetails = Businesslayer_LoginClass.Businesslayer_LoginClass()
            loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
            fetchuserstatus = Businesslayer_GetStatus.Businesslayer_GetStatus()
            userStatus = fetchuserstatus.getUserStatus_BSL()
            return render_template("Profile2.html",loggedIn=loggedIn, firstName=firstName,userStatus=userStatus )
    except:
        msg = "Error in view Homepage"
        logging.info(msg, exc_info=True)

@app.route("/account/profile")
def profileHome():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        else:
            loggedIn = True
            loginclassdetails = Businesslayer_LoginClass.Businesslayer_LoginClass()
            loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
            fetchuserstatus = Businesslayer_GetStatus.Businesslayer_GetStatus()
            userStatus = fetchuserstatus.getUserStatus_BSL()
            return render_template("Profile2.html",loggedIn=loggedIn, firstName=firstName,userStatus=userStatus )
    except:
        msg = "Error in view profile"
        logging.info(msg, exc_info=True)

@app.route("/account/profile/edit")
def editProfile():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        loginclassdetails = Businesslayer_LoginClass.Businesslayer_LoginClass()
        loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
        fetchuserdata = Businesslayer_FetchUserData.Businesslayer_FetchUserData()
        profileData = fetchuserdata.getProfileData_BSL(session['email'])
        return render_template("editProfile.html", profileData=profileData, loggedIn=loggedIn, firstName=firstName )
    except:
        msg = "Error in view edit profile"
        logging.info(msg, exc_info=True)

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    try:
        if 'email' not in session:
            return redirect(url_for('loginForm'))
        if request.method == "POST":
            oldPassword = request.form['oldpassword']
            oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
            newPassword = request.form['newpassword']
            newPassword = hashlib.md5(newPassword.encode()).hexdigest()
            changemypassword = Businesslayer_ChangeMyPassword.Businesslayer_ChangeMyPassword()
            msg = changemypassword.changeMyProfilePassword_BSL(session['email'],oldPassword,newPassword)
            return render_template("changePassword.html", msg=msg)
        else:
            return render_template("changePassword.html")
    except:
        msg = "Error in view changepassword"
        logging.info(msg, exc_info=True)

@app.route("/updateProfile", methods=["GET", "POST"])
def updateProfile():
    try:
        if request.method == 'POST':
            email = request.form['email']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            address1 = request.form['address1']
            address2 = request.form['address2']
            zipcode = request.form['zipcode']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone = request.form['phone']
            user_details = []
            About = request.form['About']
            Current_Employer = request.form['Current_Employer']
            Current_Employer_start_date = request.form['Current_Employer_start_date']
            Current_Employer_end_date = request.form['Current_Employer_end_date']
            Previous_Employer = request.form['Previous_Employer']
            Previous_Employer_start_date = request.form['Previous_Employer_start_date']
            Previous_Employer_end_date = request.form['Previous_Employer_end_date']
            Education_details_1 = request.form['Education_details_1']
            Education_details_1_start_date = request.form['Education_details_1_start_date']
            Education_details_1_end_date = request.form['Education_details_1_end_date']
            Education_details_2 = request.form['Education_details_2']
            Education_details_2_start_date = request.form['Education_details_2_start_date']
            Education_details_2_end_date = request.form['Education_details_2_end_date']
            Skill_1 = request.form['Skill_1']
            Skill_2 = request.form['Skill_2']
            Skill_3 = request.form['Skill_3']
            Skill_4 = request.form['Skill_4']
            Project_Name_1 = request.form['Project_Name_1']
            Project_Details_1 = request.form['Project_Details_1']
            Project_Name_2 = request.form['Project_Name_2']
            Project_Details_2 = request.form['Project_Details_2']
            Project_Name_3 = request.form['Project_Name_3']
            Project_Details_3 = request.form['Project_Details_3']
            user_details.append(About)
            user_details.append(Current_Employer)
            user_details.append(Current_Employer_start_date)
            user_details.append(Current_Employer_end_date)
            user_details.append(Previous_Employer)
            user_details.append(Previous_Employer_start_date)
            user_details.append(Previous_Employer_end_date)
            user_details.append(Education_details_1)
            user_details.append(Education_details_1_start_date)
            user_details.append(Education_details_1_end_date)
            user_details.append(Education_details_2)
            user_details.append(Education_details_2_start_date)
            user_details.append(Education_details_2_end_date)
            user_details.append(Skill_1)
            user_details.append(Skill_2)
            user_details.append(Skill_3)
            user_details.append(Skill_4)
            user_details.append(Project_Name_1)
            user_details.append(Project_Details_1)
            user_details.append(Project_Name_2)
            user_details.append(Project_Details_2)
            user_details.append(Project_Name_3)
            user_details.append(Project_Details_3)

            updatemyprofile = Businesslayer_UpdateMyProfile.Businesslayer_UpdateMyProfile()
            msg = updatemyprofile.updateMyProfileMethod_BSL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details)
            return redirect(url_for('editProfile'))
    except:
        msg = "Error in view update profile"
        logging.info(msg, exc_info=True)


@app.route("/postStatus" , methods=['POST'])
def postStatus():
    try:
        text = request.form['inputPost']
        insertuserstatus = Businesslayer_PostStatus.Businesslayer_PostStatus()
        insertuserstatus.insertUserStatus_BSL(session['email'],text)
        return redirect(url_for('profileHome'))
    except:
        msg = "Error in view poststatus"
        logging.info(msg, exc_info=True)

@app.route("/loginForm")
def loginForm():
    try:
        if 'email' in session:
            return redirect(url_for('root'))
        else:
            return render_template('home.html', error='')
    except:
        msg = "Error in view loginform"
        logging.info(msg, exc_info=True)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            checkifuservalid = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
            value  = checkifuservalid.isValid_BSL(email, password)
            if value == True:
                session['email'] = email
                return redirect(url_for('root'))
            elif value == False:
                error = 'Invalid UserId / Password'
                return render_template('home.html', error=error)
    except:
        msg = "Error in view login"
        logging.info(msg, exc_info=True)

@app.route("/logout")
def logout():
    try:
        session.pop('email', None)
        return redirect(url_for('root'))
    except:
        msg = "Error in view logout"
        logging.info(msg, exc_info=True)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            #Parse form data
            password = request.form['password']
            email = request.form['email']
            fetchuserdata = Businesslayer_FetchUserData.Businesslayer_FetchUserData()
            profileData = fetchuserdata.getProfileData_BSL(email)
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            address1 = request.form['address1']
            address2 = request.form['address2']
            zipcode = request.form['zipcode']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone = request.form['phone']
            userType = request.form['userOptions']
            planType = request.form['planOptions']

            # if(profileData[1] == email):
                # msg = "Email already exists"
                # return render_template("register.html", error=msg, profileData=profileData[1])
            # else:
            insertuser = Businesslayer_InsertUser.Businesslayer_InsertUser()
            msg = insertuser.insertNewUser_BSL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType)
            return render_template("home.html")
    except:
        msg = "Error in view register"
        logging.info(msg, exc_info=True)

@app.route("/jobs", methods = ['GET', 'POST'])
def jobs():
    try:
        if request.method == 'POST':
            #Parse form data
            jobId = request.form['jobId']
            companyName = request.form['companyName']
            title = request.form['title']
            manager = request.form['manager']
            location = request.form['location']
            jobDetails = request.form['jobDetails']
            insertjob = Businesslayer_InsertJob.Businesslayer_InsertJob()
            msg = insertjob.insertJob_BSL(jobId,companyName,title,manager,location,jobDetails)
            fetchjobdata = Businesslayer_FetchJobData.Businesslayer_FetchJobData()
            jobData = fetchjobdata.getJobData_BSL()
            noOfJobs = len(jobData)
            return render_template("jobs.html", jobData=jobData, noOfJobs=noOfJobs, msg=msg, jobId="Job with job id:" + jobId)
    except:
        msg = "Error in view jobs"
        logging.info(msg, exc_info=True)

@app.route("/registerationForm")
def registrationForm():
    try:
        return render_template("register.html")
    except:
        msg = "Error in view registerform"
        logging.info(msg, exc_info=True)

##Added Error log

@app.route("/checkUserErrorLog")
def CheckErrorLog():
    try:
        text = open('Log1.log', 'r+')
        content = text.read()
        text.close()
        return render_template("Errorlog.html",content = content)
    except:
        msg = "Error in view ErrorLog"
        logging.info(msg, exc_info=True)
##Added Error log


@app.route("/addJobs")
def addJobs():
    try:
        fetchjobdata = Businesslayer_FetchJobData.Businesslayer_FetchJobData()
        jobData = fetchjobdata.getJobData_BSL()
        noOfJobs = len(jobData)
        if(noOfJobs == 0):
            return render_template("jobs.html",noOfJobs=noOfJobs,jobData=jobData)
        else:
            return render_template("jobs.html", jobData=jobData, noOfJobs=noOfJobs)
    except:
        msg = "Error in view jobs"
        logging.info(msg, exc_info=True)

@app.route("/messaging", methods = ['GET', 'POST'])
def messaging():
    try:
        if request.method == 'POST':
            #Parse form data
            recipientAddress = request.form['recipientAddress']
            mailSubject = request.form['mailSubject']
            email = session['email']
            mailBody = request.form['mailBody'] + " Sent by: " + email + " from FindMyEmployer"
            msg = Message(mailSubject, sender = email, recipients = [recipientAddress])
            msg.body = mailBody
            mail.send(msg)
            return render_template("messaging.html")
    except:
        msg = "Error in view messaging"
        logging.info(msg, exc_info=True)

@app.route("/messageForm")
def messageForm():
    try:
        return render_template("messaging.html")
    except:
        msg = "Error in view messaging"
        logging.info(msg, exc_info=True)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    name = session['email']
    if form.validate_on_submit():
        for filename in request.files.getlist('photo'):
            photos.save(filename, name=name + '.')
        success = True
    else:
        success = False
    path = app.config['UPLOADED_PHOTOS_DEST']  + "/"+ session['email']+ "/"
    if not os.path.exists(path):
        os.makedirs(path)
    for fname in os.listdir(app.config['UPLOADED_PHOTOS_DEST']):
        if fname.endswith('.jpg'):
            copyfile(app.config['UPLOADED_PHOTOS_DEST']  +"/" + name+ ".jpg", path + name+ ".jpg")
        elif fname.endswith('.jpeg'):
            copyfile(app.config['UPLOADED_PHOTOS_DEST']  + "/" + name+ ".jpeg", path + name+ ".jpeg")
        elif fname.endswith('.png'):
            copyfile(app.config['UPLOADED_PHOTOS_DEST'] +"/" + name+ ".png", path + name+ ".png")
    fileUploaded = False
    if glob.glob(path + name + ".*"):
        fileUploaded = True
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'] +"/" +name)
    return render_template('Uploadphoto.html', form=form, success=success,files_list=files_list,fileUploaded = fileUploaded)

@app.route('/open/<filename>')
def open_file(filename):
    file_url = photos.url(filename)
    return render_template('ViewImage.html', file_url=file_url)

@app.route('/delete/<filename>')
def delete_file(filename):
    uploaded = False
    file_path = photos.path(filename)
    os.remove(file_path)
    path = app.config['UPLOADED_PHOTOS_DEST']  + "/"+ session['email']+ "/" + filename
    os.remove(path)
    return redirect(url_for('upload_file'))

@app.route("/searchProfile", methods = ['GET', 'POST'])
def searchProfile():
    try:
        if request.method == 'POST':
            #Parse form data
            searchProf = request.form['searchProf']
            if (searchProf == ''):
                return render_template("searchProfile.html",error="Enter Name to Search", noOfProfilesFetched=0)
            else:
                fetchSearchedProfile = Businesslayer_FetchSearchedProfile.Businesslayer_FetchSearchedProfile()
                fetchSearchedProfileData = fetchSearchedProfile.fetchSearchedProfile_BSL(searchProf)
                noOfProfilesFetched = len(fetchSearchedProfileData)
                if (noOfProfilesFetched == 0):
                    return render_template("searchProfile.html", fetchSearchedProfileData=fetchSearchedProfileData, noOfProfilesFetched=noOfProfilesFetched,error="No Results Found")
                else:
                    return render_template("searchProfile.html", fetchSearchedProfileData=fetchSearchedProfileData, noOfProfilesFetched=noOfProfilesFetched)
    except:
        msg = "Error in view searchProfile"
        logging.info(msg, exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(filename='Log1.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    app.run(debug=True)
