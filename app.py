from model import app,db,Flask,render_template,request,redirect
from model import Songs,audio_book,podcast

#####################################################
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%d/%m/%Y %H:%M:%S")
############################################

@app.route("/")
def home():
    return render_template("Button.html")

@app.route("/song", methods=["GET", "POST"])
def songs():
    user = Songs.query.limit(100).all()
    if request.method == "POST":
        
        name = request.form["song_name"]
        duration = request.form["Duration"]
    
        data = Songs(name,duration,date_time)
        db.session.add(data)
        db.session.commit()
        return redirect("/song")
    
        
    return render_template("index.html",users=user)
    


# update the post
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    update = Songs.query.get_or_404(id)

    if request.method == "POST":
        update.name = request.form["song_name"]
        update.duration = request.form["Duration"]
        update.time=date_time


        db.session.add(update)
        db.session.commit()

        return redirect("/song")
    return render_template("edit.html", update=update)


# delete the post


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    delete_post = Songs.query.get_or_404(id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect("/song")




@app.route("/podcast", methods=["GET", "POST"])
def pod():
    user = podcast.query.limit(100).all()
    if request.method == "POST":
        
        name = request.form["song_name"]
        duration = request.form["Duration"]
        host=request.form["host"]
        participants=request.form["participants"]
    
        data = podcast(name,duration,date_time,host,participants)
        db.session.add(data)
        db.session.commit()
        return redirect("/podcast")
    return render_template("podcast_index.html",users=user)
    


# update the post
@app.route("/pod_edit/<int:id>", methods=["GET", "POST"])
def pod_edit(id):
    update = podcast.query.get_or_404(id)

    if request.method == "POST":
        update.name = request.form["song_name"]
        update.duration = request.form["Duration"]
        update.time=date_time
        update.host=request.form["host"]
        update.participants=request.form["participants"]


        db.session.add(update)
        db.session.commit()

        return redirect("/podcast")
    return render_template("podcast_edit.html", update=update)


# delete the post


@app.route("/pod_delete/<int:id>", methods=["GET", "POST"])
def pod_delete(id):
    delete_post = podcast.query.get_or_404(id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect("/podcast")


@app.route("/audio_book", methods=["GET", "POST"])
def audio():
    user = audio_book.query.limit(100).all()
    if request.method == "POST":
        
        name = request.form["song_name"]
        author=request.form["author"]
        narrator=request.form["narrator"]
        duration = request.form["duration"]
    
        data = audio_book(name,author,narrator,duration,date_time)
        db.session.add(data)
        db.session.commit()
        return redirect("/audio_book")
    return render_template("audio_index.html",users=user)
    


# update the post
@app.route("/audio_edit/<int:id>", methods=["GET", "POST"])
def audio_edit(id):
    update = audio_book.query.get_or_404(id)

    if request.method == "POST":
        update.name = request.form["song_name"]
        update.author = request.form["author"]
        update.time=date_time
        update.narrator=request.form["narrator"]
        update.duration=request.form["duration"]


        db.session.add(update)
        db.session.commit()

        return redirect("/audio_book")
    return render_template("audio_edit.html", update=update)


# delete the post


@app.route("/audio_delete/<int:id>", methods=["GET", "POST"])
def audio_delete(id):
    delete_post = audio_book.query.get_or_404(id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect("/audio_book")


  
if __name__ == "__main__":
    app.run(debug=True)