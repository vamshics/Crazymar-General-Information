from django.shortcuts import render, redirect
from .models import JobCre
def show(request):
    return render(request, 'create_job.html')
def sav(request):
    uid = request.POST.get('rvk')
    jbtitle = request.POST.get('jobtitle')
    cname = request.POST.get('companyname')
    Category = request.POST.get('category')
    position = request.POST.get('Position')
    vacancy = request.POST.get('No_Of_Vacancy')
    experience = request.POST.get('Experience')
    package = request.POST.get('Package')
    clogo = request.FILES.get('myfiles[]')
    jobtype = request.POST.get('Job_Type')
    qualification = request.POST.get('Min_Qualification')
    skills = request.POST.get('Skills')
    mail = request.POST.get('email1')
    phone = request.POST.get('mobile')
    landline1 = request.POST.get('landlne')
    website1 = request.POST.get('websitelink')
    address = request.POST.get('adress')
    cname1 = request.POST.get('cityname')
    state1 = request.POST.get('state1')
    ct1 = request.POST.get('country1')
    zp1 = request.POST.get('zipcode1')
    fb2 = request.POST.get('facebook1')
    gg1 = request.POST.get('ggleplus1')
    tw1 = request.POST.get('twitter1')
    lkd1 = request.POST.get('linkedin1')
    pint1 = request.POST.get('pininterest1')
    insta = request.POST.get('instagram1')
    if uid == '':
        ss = JobCre(jobtitle=jbtitle, company_name=cname, Category=Category, Position=position, NoOfVacancy=vacancy,
                   Experience=experience, Package=package, CompanyLogo = clogo, JobType=jobtype,
                   MinQualification = qualification, Skills=skills, maill1=mail,
                phoneNo = phone, landline = landline1, website = website1, addresss = address,
                city = cname1, state = state1, country = ct1, zipcode = zp1,fb = fb2, ggleplus2 = gg1, twitter = tw1,
                linkedin1 = lkd1, pininterest1 = pint1, instagramm = insta)
        ss.save()
        return render(request, 'create_job.html')
    else:
        rvk = JobCre.objects.filter(id=uid).update(jobtitle=jbtitle, company_name=cname, Category=Category, Position=position, NoOfVacancy=vacancy,
                   Experience=experience, Package=package, CompanyLogo = clogo, JobType=jobtype,
                   MinQualification = qualification, Skills=skills, maill1=mail,
                phoneNo = phone, landline = landline1, website = website1, addresss = address,
                city = cname1, state = state1, country = ct1, zipcode = zp1,fb = fb2, ggleplus2 = gg1, twitter = tw1,
                linkedin1 = lkd1, pininterest1 = pint1, instagramm = insta)
        return render(request,'create_job.html',{'ss':rvk})
def retrieve(request):
    bb = JobCre.objects.all()
    return render(request, 'file.html', {'rvk': bb})
def edit(request,id):
    vamshi = JobCre.objects.get(id=id)
    return render(request,'create_job.html',{'ss': vamshi})
def delete(request,id):
    vamshi = JobCre.objects.get(id=id)
    vamshi.delete()
    return redirect(retrieve)
