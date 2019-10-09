from flask import Blueprint, make_response, jsonify, request
from app.models import Article
from app.utilities.helpers import protected

blog = Article()

article = Blueprint('article', __name__)

@article.route('/article', methods=['POST'])
@protected
def create_article(logged_user):
    """create article method"""
    form_data = request.get_json(force=True)
    article = {
        "title": form_data["title"],
        "content": form_data["content"],
        "created_by": logged_user['email']
    }
    if blog.check_title(article["title"]):
        return make_response(jsonify({'status': 400, \
             'message': 'Article with this title already exists'}), 400)
    valid_article = blog.create_article(article)
    return make_response(jsonify({'status': 201, \
        'message': 'Created article successfully'}), 201)

@article.route('/article/all', methods=['GET'])
def get_articles():
    """ fetch all articles """
    all_articles = blog.get_all_articles()
    if all_articles:
        return make_response(jsonify({'status': 200, 'article_list': all_articles}))
