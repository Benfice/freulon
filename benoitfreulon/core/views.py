import os
from flask import render_template,redirect, Blueprint, url_for, current_app, flash
from benoitfreulon.core.forms import MessageForm
from flask_mail import Mail, Message
from benoitfreulon import app

core = Blueprint('core',__name__)

mail = Mail(app)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/photo')
def photo():
    return render_template('photo.html')

@core.route('/street')
def street():
    street_path = os.path.join(current_app.root_path,'static/pics/street_pics')
    street_pics = os.listdir(street_path)
    street_pics.sort()
    return render_template('street.html', street_pics = street_pics)

@core.route('/portrait')
def portrait():
    portrait_path = os.path.join(current_app.root_path,'static/pics/portrait_pics')
    portrait_pics = os.listdir(portrait_path)
    portrait_pics.sort()
    return render_template('portrait.html', portrait_pics = portrait_pics)

@core.route('/event')
def event():
    event_path = os.path.join(current_app.root_path,'static/pics/event_pics')
    event_pics = os.listdir(event_path)
    event_pics.sort()
    return render_template('event.html', event_pics = event_pics)

@core.route('/web')
def web():
    web_path = os.path.join(current_app.root_path,'static/pics/web_logos')
    web_logos = os.listdir(web_path)
    web_logos.sort()
    return render_template('web.html', web_logos = web_logos)

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/contact',methods=['GET','POST'])
def contact():
    form = MessageForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message('Message from ' + name + ' - ' + email, sender = 'benfice@gmail.com', recipients = ['bfreulon@orange.fr'])
        msg.body = message
        mail.send(msg)
        flash('Sent! Thank you for your message!')
        return redirect(url_for('core.contact',form=form))
    else:
        flash('Please enter all the fields.')
    return render_template('contact.html', form=form)
