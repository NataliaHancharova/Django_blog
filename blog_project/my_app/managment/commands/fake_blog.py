from faker import Faker
from django.contrib.auth.models import User 
from django.core.management.base import BaseCommand
import random
from my_app.models import Post, Comment

class Comanda(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(3):
            User.objects.create_user(username=faker.user_name(), 
                                 email=faker.email(),
                                 password='12345abvg')
        
        users = list(User.objects.all())

        for _ in range(10):
            Post.objects.create(title=faker.sentence(nb_words=5),
                                content=faker.paragraph(nb_sentences=10),
                                author=random.choice(users)
                                )
        posts = list(Post.objects.all())


        for _ in range(20):
            Comment.objects.create(post=random.choice(posts),
                                   author=random.choice(users),
                                   content=faker.paragraph(3)
                                   )

        self.stdout.write(self.style.SUCCESS('Seeded datd successfully'))