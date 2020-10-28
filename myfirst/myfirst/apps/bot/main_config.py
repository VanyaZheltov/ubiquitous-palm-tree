from .models import BotInfo
token = 'f9226fd7da439e5e4a443d2cab203c527fc5db6c13568d32c795128f4e88e79593fee5191215dc47aed2d'
admin_token = '74e43e6ece7717fcaf61ade275b6a30fdeae86961123e3707d7b81b5e40799128f0be4991924e5898a4ab'
confirmation_token  = BotInfo.objects.get(group_name="EnglishPush").confirmation_token
admin_conf_token = BotInfo.objects.get(group_name="Admin").confirmation_token
secret_key = 'aaQ1392dmLop'