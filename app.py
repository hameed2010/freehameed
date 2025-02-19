import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    import time
    import datetime
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    import datetime 
    import requests 
   
    pass


from keep_alive import keep_alive
keep_alive()
db = uu('dbs/hameeed.ss', 'rshq')\

print(db)


bot = TeleBot(token="7536129194:AAH7xiyzsadwEKvNXskin3Oo1Yjycq4JNNA")
MAX_MESSAGES_PER_DAY = 10
admin = 6698161283 
bk = mk(row_width=1).add(btn('رجوع', callback_data='back'))
with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

def extract_freepik_id(url):
    match = re.search(r'_(\d+)\.htm', url)
    if match:
        return match.group(1)
    return None
 # إذا لم يتم العثور على رقم
stypes = ['member', 'administrator', 'creator']
if not db.get('accounts'):
    db.set('accounts', [])
    pass

if not db.get("admins"):
    db.set('admins', [admin, ])
if not db.get('badguys'):
    db.set('badguys', [])

if not db.get('force'):
    db.set('force', [])
if not db.get('subscription'):
    db.set('subscription', [])    
if not db.get('token_table'):
    db.set('token_table', [])   
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    
  
    keys = mk(row_width=2)
    if user_id in db.get("admins") :
        keys_ = mk()
        btn01 = btn('🤍الاحصائيات', callback_data='stats')
        btn02 = btn("⚠️اذاعة", callback_data='cast')
        btn05, btn06 = btn('➖حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
       
        btna = btn('➕تفعيل ViP', callback_data='addsubscription')
        btnl = btn('➖الغاء ViP', callback_data='delsubscription')
        leave = btn('➖   معرفه المتبقي من الاشتراك ', callback_data='checksubscription')
        
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        
        btn03 = btn('➕اضافة ادمن', callback_data='addadmin')
        btn04 = btn('➖مسح ادمن', callback_data='deladmin')

        btn012 = btn('⚠️الادمنية ', callback_data='admins')
        btn013 = btn(' المشتركين', callback_data='subscription')
        btn014 = btn(' التوكن', callback_data='token_function')
        btn015 = btn(' التوكن الموجود', callback_data='show_all_tokens')
        keys_.add(btn03, btn04)
        keys_.add(btn012, btn11)
        
         
        
        keys_.add(btna, btnl)
        keys_.add(btn013)
        keys_.add(leave)
        keys_.add(btn014,btn015)
      
        bot.reply_to(message, messages['admin_panel_message'], reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                    check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                    keyboard = mk().add(channel_button).add(check_button)
                    bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        
        
        
        
        return bot.reply_to(message, messages['welcome_message'])
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return
    
    
   
   

    return bot.reply_to(message,messages['welcome_message'])

@bot.message_handler(func=lambda message: True)  # هذا يسمح بالرد على أي رسالة
def handle_message(message):
    user_id = message.from_user.id
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return
    sub_data = db.get(f"{user_id}_subscription")
    if  sub_data:
        

    # تحويل تاريخ انتهاء الاشتراك إلى كائن `datetime.date`
        end_date = datetime.datetime.strptime(sub_data["end_date"], "%Y-%m-%d").date()
        today = datetime.date.today()
        print(today)

        # التحقق مما إذا كان الاشتراك لا يزال نشطًا
        if today > end_date:
            bot.reply_to(message,messages['subscription_expired_message'])
            return 

        # جلب عدد الرسائل المرسلة اليوم
        user_messages = db.get(f"{user_id}_messages")
        
        if not user_messages:
            user_messages = {}  # إذا لم تكن هناك بيانات، قم بتعيينها كقاموس فارغ

        messages_today = user_messages.get(str(today), 0)

        # التحقق من الحد اليومي
        if messages_today >= MAX_MESSAGES_PER_DAY:
            bot.reply_to(message, messages['download_limit_message'])
            return 
        global session_cookie
        id=extract_freepik_id(message.text)
        if id==None:
            print(id)
            bot.reply_to(message, messages['invalid_link_message'])
            return
        if download_resource(id, message, user_id):
            user_messages[str(today)] = messages_today + 1
            db.set(f"{user_id}_messages", user_messages)
            bot.reply_to(message, f"📂 ملفك أصبح جاهز ✅ المتبقي لديك لتحميل ({max(0, MAX_MESSAGES_PER_DAY - messages_today - 1)}) لهذا اليوم.")
            return
        else:
            bot.reply_to(message, messages['registration_success_message'])
            return
    #بدون اشتارك
    user_messages = db.get(f"{user_id}_messages")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)  # حساب اليوم التالي
    formatted_date = tomorrow.strftime("%d/%m/%Y")
    if  user_messages:
        
        user_messages = {}
        messages_today = user_messages.get(str(today), 0)
        if messages_today >= 1:
            bot.reply_to(
        message,
        f"🚫 نعتذر، لقد تم منعك من الإرسال حتى {formatted_date} الساعة 13:31. "
        "يتطلب الاشتراك لإكمال طلب الملفات الإضافية.\n\n"
        "للاشتراك، يمكنك التحدث مع أحد المشرفين أو الضغط <a href='https://t.me/freepikprem1'>هنا</a>.\n\n"
        "شكرًا لتفهمك!",
        parse_mode="HTML"
    )
            message_text = """
    👤 باسم: عصماء علي

    💳 الحسابات المتاحة:
    - حساب يمني: <b><code>3066613975</code></b>
    - حساب سعودي: <b><code>3073514826</code></b>
    - حساب دولار: <b><code>3120895458</code></b>

    📤 بعد الإيداع:
    قم بإرسال صورة الإيداع إلى ⇇ @eitabbbb
    """
            bot.reply_to(message, message_text, parse_mode="HTML")
            return
        id=extract_freepik_id(message.text)
        print(id)
        if id==None:
            bot.reply_to(message, messages['download_limit_message'])
            return
        if download_resource(id, message, user_id):
            user_messages[str(today)] = messages_today + 1
            db.set(f"{user_id}_messages", user_messages)
            bot.reply_to(message, f"📂 ملفك أصبح جاهز ✅ المتبقي لديك لتحميل ({max(0, 1 - messages_today - 1)}) لهذا اليوم.")
            return
        else:
            bot.reply_to(message, messages['registration_success_message'])
            return

                
    
def download_resource(resource_id, message_id, user_id):
    token_data = db.get('token_table')
    tokens_string = ", ".join(map(str, token_data))
    url = f"https://api.freepik.com/v1/resources/{resource_id}/download"
    headers = {"x-freepik-api-key": tokens_string}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data_dict = json.loads(response.text)
        info = data_dict.get('data', {})
        filename = info.get('filename')
        file_url = info.get('url')

        if not filename or not file_url:
            print("❌ فشل في جلب بيانات الملف.")
            return False

        print(f"🔗 رابط الملف: {file_url}")
        
        file_response = requests.get(file_url, stream=True)
        file_response.raise_for_status()

        with open(filename, "wb") as file:
            for chunk in file_response.iter_content(1024):
                file.write(chunk)

        print(f"✅ تم تحميل الملف: {filename}")

        with open(filename, "rb") as file:
            bot.send_document(user_id, file)

        print(f"📤 تم إرسال الملف إلى المستخدم {user_id}")

        os.remove(filename)
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ أثناء التحميل: {e}")
        return False
    except Exception as e:
        print(f"⚠️ خطأ غير متوقع: {e}")
        return False
@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    user_id = call.from_user.id
    cid, data, mid = call.from_user.id, call.data, call.message.id
    count_ord = db.get('orders') if db.get('orders') else 1
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addadmin':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'token_function':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, token_function, type)
    if data == 'delsubscription':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من اشتراك',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)
    if data == 'addsubscription':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)   
    if data == 'checksubscription':
        type = 'check'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد معرفه اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type) 
    if data == 'show_all_tokens':
        token_data = db.get('token_table')  # جلب جميع التوكنات

        if not token_data or token_data == []:
            bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
            return
        else:
            
            bot.edit_message_text(chat_id=cid, message_id=mid, text=token_data)

            return
             # تنسيق القائمة
             

    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    if data == 'subscription':
        get_subscription = db.get('subscription')
        if get_subscription:
            if len(get_subscription) >=1:
                txt = 'المشتركين : \n'
                for ran, admin in enumerate(get_subscription, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد مشتركين بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد مشتركين بالبوت')
            return
    if data == 'check_subscription':
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
                if str(x.status) not in stypes:
                    bot.answer_callback_query(call.id, '❌ لا تزال غير مشترك، يرجى الاشتراك ثم إعادة المحاولة.')
                    return
        bot.answer_callback_query(call.id, '✅ تم التحقق من اشتراكك بنجاح!')
        bot.edit_message_text('✅  تم التحقق من اشتراكك، يمكنك الآن استخدام البوت.', chat_id=cid, message_id=mid)
    if data == 'banone':
        if cid in db.get("admins") :
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") :
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") :
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    
    if data == 'setforce':

        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@uf3_8 @uf3_8',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True
def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, f'• رجاء ارسل القناة بشكل صحيح')
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return

def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def subscription(message, action):
    try:
        user_id = int(message.text)
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إرسال **ID** المستخدم بشكل صحيح!")
        return

    if action == 'add':
        # تحديد تاريخ البداية والنهاية
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=30)

        # حفظ بيانات الاشتراك
        db.set(f"{user_id}_subscription", {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        })

        bot.reply_to(message, f"✅ تم تفعيل الاشتراك للمستخدم **{user_id}** حتى {end_date}")
        try:
            bot.send_message(user_id, f"🎉 تهانينا! تم تفعيل اشتراكك حتى {end_date}.\n"
                                      f"يمكنك الآن تحميل   10 ملفات  يوميًا. ✅")
        except Exception as e:
            print(f"⚠️ فشل إرسال الرسالة للمستخدم {user_id}: {e}")

    elif action == 'delete':
        if db.exists(f"{user_id}_subscription"):
            db.delete(f"{user_id}_subscription")
            bot.reply_to(message, f"❌ تم إلغاء اشتراك المستخدم **{user_id}** بنجاح.")
        else:
            bot.reply_to(message, f"⚠️ لا يوجد اشتراك لهذا المستخدم.")

    elif action == 'check':
        sub_data = db.get(f"{user_id}_subscription")
        if sub_data:
            bot.reply_to(message, f"📅 اشتراك المستخدم **{user_id}** نشط حتى {sub_data['end_date']}.")
        else:
            bot.reply_to(message, f"⏳ لا يوجد اشتراك نشط لهذا المستخدم.")

def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
def token_function(message, type):
    user_id = message.text  # السماح بأي نص وإزالة المسافات الزائدة

    if type == 'add':
        db.set('token_table', [user_id])  # استبدال التوكن الحالي بالتوكن الجديد
        bot.reply_to(message, f'• تم تعيين التوكن الجديد بنجاح ✅\n• التوكن: {user_id}')

    elif type == 'delete':
        token_data = db.get('token_table') or []  # جلب التوكن الحالي
        if user_id not in token_data:
            bot.reply_to(message, '• هذا التوكن غير موجود')
        else:
            db.set('token_table', [])  # إزالة التوكن
            bot.reply_to(message, '• تم ازالة التوكن بنجاح ✅')
def casting(message):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return

try:
    bot.infinity_polling()
except:
    pass   
