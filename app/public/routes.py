import logging

from flask import abort, render_template, current_app, redirect, url_for, request
from flask_login import current_user
from flask_mail import Message

from app.models import Post, Comment
from . import public_bp
from .forms import CommentForm
from .. import mail
from ..common.mail import send_email

logger = logging.getLogger(__name__)


@public_bp.route("/mesagges/")
def message_email():
    msg = Message('Hello', sender=("Juanjo", "juanjo@j2logo.com"), recipients=['ajpadilla88@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return 'OK'


@public_bp.route("/")
def index():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los posts del blog')
    page = int(request.args.get('page', 1))
    per_page = current_app.config['ITEMS_PER_PAGE']
    post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/index.html", post_pagination=post_pagination)


@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if not post:
        logger.info(f'El post {slug} no existe')
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id, user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)
