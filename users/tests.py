from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user


# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='admin', first_name='yol', last_name='abror', email='drontend@gami,com')
        self.user.set_password('abrordaad')
        self.user.save()

    def test_logout(self):
        # 1. CustomUser Yaratdim tepada setUp da yaratildi
        # 2. self.client.login orqali login qildim
        self.client.login(username='admin', password='abrordaad')
        # 3. logout qilish uchun request yubordim
        self.client.get(reverse('users:logout'))
        # 4. login qilgan userni olaman
        user = get_user(self.client)
        # 5. userni logout qolganini tekshiramna agar is_authenticated FALSE qaytarsa test ishlagan boladi
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    # 1. test login bolmagan userni login pagega otib yuborishni tekshirish
    def test_login_required(self):
        # bu code login bolmagan userni taminlaydi chunki login qilish uchun hechqanday yangi user yaratmadim
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')
        self.assertEqual(response.status_code, 302)

    def test_profile_detail(self):
        # 1. Yangi CustomUser Yaratdim
        user = CustomUser.objects.create(
            username='admin', first_name='yol', last_name='abror', email='drontend@gami,com'
        )
        user.set_password('abrordaad')
        user.save()
        # 2. self.client.login orqali login qildim
        self.client.login(username='admin', password='abrordaad')
        # 3. CustomUser login qilgani uchun redrect qilib yubormadida malumotlarni ekranga chiqarib berdi
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        # 1. Yangi CustomUser Yaratdim
        user = CustomUser.objects.create(
            username='admin', first_name='yol', last_name='abror', email='drontend@gami,com'
        )
        user.set_password('abrordaad')
        user.save()
        # 2. self.client.login orqali login qildim
        self.client.login(username='admin', password='abrordaad')

        # 3. userni yangilash

        response = self.client.post(
            reverse('users:profile-edit'),
            data={
                "username": 'admin',
                "first_name": 'Yoldoshevsss',
                "last_name": 'Abrors',
                "email": 'python@gmail.com'
            }
        )
        # 4. yangi userni olish uchun 1 - create userda eski user saqlanib turubdi edi esa biz uzgartirdik
        # yangisini olish uchun bu code
        # user = CustomUser.objects.get(pk=user.pk)
        user.refresh_from_db()
        # 5. endi yangilangan userlarni tekshirish mumkin
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.first_name, 'Yoldoshevsss')
        self.assertEqual(user.last_name, 'Abrors')
        self.assertEqual(user.email, 'python@gmail.com')
        self.assertEqual(response.url, reverse('users:profile'))
