import json
import os
import subprocess
import requests
import urllib.request

from django.shortcuts import render, HttpResponse

from NflmCA import settings
from .models import *

from bs4 import BeautifulSoup


def custlist(request):
    if request.POST:
        a = request.POST['num']
        print(a)
        b = []
        sel = Order.objects.distinct().values('user').annotate(dcount=Count('user')).order_by('dcount')
        print(sel)
        for s in sel:
            b.append(s['dcount'])
        selist = set(b)
        count = Order.objects.values('user__name', 'user__phone1', 'user__id').annotate(dcount=Count('user')).order_by(
            'dcount')
        q = []
        # print(type(a))
        if int(a) == -1:
            q = count
        else:
            for z in count:
                # print(z['dcount'])
                if z['dcount'] == int(a):
                    q.append(z.copy())
                    # print('abcccccccccccccccccccc')

        print(count)
        print('q = ')
        print(q)
        context = {'count': q, 'sel': selist, 'tc': len(q)}
        return render(request, "Consumer_Analytics/Consumer_Order_List.html", context)
    else:
        sel = Order.objects.values('user').annotate(dcount=Count('user')).order_by('dcount').distinct()
        print(sel)
        b = []
        a = -1
        for s in sel:
            b.append(s['dcount'])
        selist = set(b)
        count = Order.objects.values('user__name', 'user__phone1', 'user__id').annotate(dcount=Count('user')).order_by('dcount')
        print(count)
        context = {'count': count, 'sel': selist, 'tc': len(count)}
        print(len(count))
        return render(request, "Consumer_Analytics/Consumer_Order_List.html", context)


def insta_scrape(request):
    if request.POST:
        instaid = request.POST['instaid']
        username = request.POST['username']
        uid = request.POST['un']
        pwd = request.POST['pwd']
        os.chdir("media/insta")
        subprocess.call(["instagram-scraper", "--comments", instaid, "-u", uid, "-p", pwd])
        album, created = InstaAlbum.objects.get_or_create(insta_id=instaid, username=username)
        if created:
            album.save()
        images = os.listdir(os.path.join(settings.MEDIA_ROOT, "insta/"+instaid))
        print(images[-1])
        for image in images:
            print(str(image).split(".")[-1])
            if str(image).split(".")[-1] == "json":
                file = image
                print("FFFFIIIILLLLEEEE")
                print(file)
        c = 0
        comments = json.load(open(str(instaid + "/" + images[-1]), encoding="utf-8"))
        l = len(comments)
        print(l)

        for image in images[0:-1]:
            c = c+1
            imglist = list(image)
            if imglist[-5] == "a":
                i = InstaPic(album=album, name="PP", img="insta/"+instaid+"/"+image)
            else:
                i = InstaPic(album=album, name=username + str(c), img="insta/" + instaid + "/" + image)
            i.save()

        imagesd = InstaPic.objects.filter(album=album)

        imgs = []
        for image in imagesd:
            imgs.append(image)

        imgnames = {}
        lcount = 0
        for image in imagesd:
            name = str(image.img.url)
            ini = name.split("/")
            n = ini[4]
            imgnames[str(n)] = lcount
            lcount += 1
            print(n)

        print(imgnames)

        c = 0
        while c < l:
            comment = comments[c]
            dis_url = str(comment["display_url"])
            ulist = dis_url.split("/")
            imgn = ulist[5]
            print("URL = "+str(imgn))
            print(str(imgn) in imgnames)
            if str(imgn) in imgnames:
                index = int(imgnames.get(str(imgn)))
                print("Index = "+str(index))
                if len(comment["comments"]["data"]) > 0:
                    for d in comment["comments"]["data"]:
                        # print(d["text"])
                        comm = InstaComments(pic=imgs[index], comment=d["text"])
                        comm.save()
                else:
                    print("No Comments")
            print("Comments Done.")
            if len(comment["edge_media_to_caption"]["edges"]) > 0:
                imgs[index].caption = (comment["edge_media_to_caption"]["edges"][0]["node"]["text"])
                print("Caption - " + str(comment["edge_media_to_caption"]["edges"][0]["node"]["text"]))
                imgs[index].save()
            c += 1

        os.chdir("../../")

        return render(request, "Consumer_Analytics/Insta_Form.html")
    else:
        return render(request, "Consumer_Analytics/Insta_Form.html")


def fb_scrape(request):
    if request.POST:
        print("")
        os.chdir(os.path.join(settings.MEDIA_ROOT, "fb/"))
        fb_id = request.POST["fbid"]
        base_url = "http://www.facebook.com/"
        complete_url = base_url + fb_id
        source_code = requests.get(complete_url)
        soup = BeautifulSoup(source_code.text, "html.parser")

        profile_cover = soup.find(id="fbProfileCover")
        name = ""
        link = ""
        if profile_cover is not None:
            name = profile_cover.find("h1").find("a").text
            link = profile_cover.find("h1").find("a").get("href")
            print("Name: " + str(name) + "\n")
            print("Link: " + str(link) + "\n")
        profile_pic = soup.find(id="fbTimelineHeadline")
        img1 = img2 = ["", ""]
        if profile_pic is not None:
            pp = profile_pic.find(class_="profilePicThumb").find("img").get("src")
            img1 = urllib.request.urlretrieve(pp, name + ".jpg")
            print("Profile Picture: " + str(pp) + "\n")
            print(str(img1))
        cover_pic = soup.find("img", class_="coverPhotoImg photo img")
        if cover_pic is not None:
            img2 = urllib.request.urlretrieve(cover_pic.get("src"), name + "_cover.jpg")
            print("Cover picture: " + cover_pic.get("src") + "\n")
            print(str(img2))

        # bio = soup.find(id="pagelet_bio").find("div").find("div").find("span").text
        bio = get_bio(soup, "pagelet_bio")
        hometown = get_hometown(soup, "pagelet_hometown")
        current_city = get_current_city(soup, "pagelet_hometown")
        contact = get_contact(soup, "pagelet_contact")
        favourites = get_favourites(soup, "favorites")
        eduwork = get_eduwork(soup, "pagelet_eduwork")

        # print(bio)
        print("HomeTown: " + str(hometown) + "\n")
        print("Current City: " + str(current_city) + "\n")
        print("Websites: " + str(contact) + "\n")
        print("Favourites: " + str(favourites))

        if str(source_code.status_code) != "404":
            if name != "" and link != "":
                fbp = FbProfile(name=name, link=link, profile_pic="fb/"+img1[0], cover_pic="fb/"+img2[0],
                                hometown=hometown, current_city=current_city)
                fbp.save()
                print("1st step")
                if contact != "":
                    for c in contact:
                        fbpl = FbProfileLink(profile=fbp, url=c)
                        fbpl.save()
                    print("contact saved")

                if favourites != "":
                    for fav in favourites:
                        label = fav["label"]
                        text = fav["text"]
                        fbfav = FbFavourite(profile=fbp, label=label, text=text)
                        fbfav.save()
                    print("favs saved")

                if eduwork != "":
                    if eduwork[0]["caption"] == "शिक्षण" or eduwork[0]["caption"].lower() == "education":
                        edu = eduwork[0]["data"]
                        work = eduwork[1]["data"]
                    else:
                        edu = eduwork[1]["data"]
                        work = eduwork[0]["data"]
                    print(edu)
                    print(work)
                    if edu is not None:
                        for e in edu:
                            title = str('\n'.join(e["title"]))
                            text = str('\n'.join(e["text"]))
                            addnl = ""
                            if "addnl" in e:
                                addnl = str(e["addnl"])
                            fbpe = FbEducation(profile=fbp, title=title, text=text, additional=addnl)
                            fbpe.save()
                        print("edu saved")

                    if work is not None:
                        for w in work:
                            title = str('\n'.join(w["title"]))
                            text = str('\n'.join(w["text"]))
                            addnl = ""
                            if "addnl" in w:
                                addnl = str(w["addnl"])
                            fbpw = FbWork(profile=fbp, title=title, text=text, additional=addnl)
                            fbpw.save()
                        print("work saved")
            else:
                return HttpResponse("<h1>Private Profile</h1>")
        else:
            return HttpResponse("<h1>Private Profile</h1>")

        return render(request, "Consumer_Analytics/Fb_Form.html")
    else:
        return render(request, "Consumer_Analytics/Fb_Form.html")


def get_bio(soup, element_id):
    # bio = soup.find(id=element_id)
    bio = soup.find("div", id="globalContainer").find_all("li")
    '''for b in bio:
        print(b.text)
    # .find("li", class_="fbTimelineTwoColumn fbTimelineUnit clearfix")
    # print(bio)'''
    return bio
    '''if bio is None:
        return "Nothing here."
    else:
        return bio.find("div").find("div").find("span").text'''


def get_hometown(soup, element_id):
    if soup.find(id=element_id) is not None:
        ht = soup.find(id=element_id).find("div").find("div").find("ul").find("li", id="hometown").find("a").text
        return ht
    return ""


def get_current_city(soup, element_id):
    if soup.find(id=element_id) is not None:
        cc = soup.find(id=element_id).find("ul").find("li", id="current_city").find("a").text
        return cc
    return ""


def get_contact(soup, element_id):
    if soup.find(id=element_id) is not None:
        con = soup.find(id=element_id).find_all("a")
        cons = []
        for c in con:
            cons.append(c.text)
            # print(con)'''
        return cons
    return ""


def get_favourites(soup, element_id):
    f = []
    if soup.find(id=element_id) is not None:
        favs = soup.find(id=element_id).find_all("tbody")
        for fav in favs:
            if fav.find(class_="data").find("a") is not None and fav.find(class_="label") is not None:
                l = fav.find(class_="label").text
                u = fav.find(class_="data").find("a").href
                t = fav.find(class_="data").find("a").text
                f.append({"label": l, "text": t})
        return f
    return ""


def get_eduwork(soup, element_id):
    sec = soup.find(id=element_id)
    if sec is not None:
        ed = sec.find_all("li")
        cls = sec.find("div", attrs={"data-pnref": True}).get("class")
        # print(cls)
        el = sec.find_all(class_=cls)
        # print(el)
        edw = []
        for e in el:
            if e.has_attr('data-pnref'):
                edw.append(get_eduwork_common(e))
            else:
                # print("22222")
                caption = e.find("div").text
                links = e.find_all("a")
                l = []
                for link in links:
                    text = link.text
                    url = link.get("href")
                    l.append({"text": text})
                edw.append({"caption": caption, "data": l})
        print("Education and Work: " + "\n")
        print(edw)
        return edw
    return ""


def get_eduwork_common(element):
    caption = element.find("div").text
    items = element.find_all("li")
    # print(items)
    l = []
    i = 0
    for item in items:
        # print(i)
        links = item.find_all("a")
        # print(title[1].text)
        # url = title[1].href
        title = []
        url = []
        for link in links:
            if link.text != "":
                title.append(link.text)
                url.append(link.href)
        role = item.find("span", attrs={"role": "presentation"})
        if role is not None:
            delim = role.text
            main_div = role.parent
            text = main_div.text.split(delim)
            # print(text)
            if main_div.parent.next_sibling is not None:
                addnl = main_div.parent.next_sibling.text
                # print(addnl)
                i = i+1
                l.append({"title": title, "text": text, "addnl": addnl})
            else:
                l.append({"title": title, "text": text})
        # print(title)
    return {"caption": caption, "data": l}




