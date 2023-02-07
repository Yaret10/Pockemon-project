from src import create_app
from src.db import db
from src.models.pokemon import pockemon

app = create_app()

# db.init_app(app)
# # with app.app_context():
# #     db.create_all()
if __name__ == "___main__":
    app.run(debug=True)
    